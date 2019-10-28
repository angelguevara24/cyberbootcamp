# PwnRepo

Now, let's write something which will ping a certain IP range and inform us which IP addresses respond to our request. AKA, a ping sweeper.

We can do this quiet easilly with a simple bash script. 

First, let's look at the PING command itself. Notice hos when you ping something, it just goes on and on and on forever, where in a Windows based enviroment it pings three times and then stops. If we want to use this command in our scipt we'll have to figure out how to limit the number of ping requets sent to every IP. 

Look up the **man** page for ping and see if you can determine how to limit how many pings go out. 

Create a bash script called `ping-loop.sh` with the following informatio:

```
#!/bin/bash

for ip in $(seq 200 210); do
echo 192.168.31.$ip
done
```

Once executed, we see that this script just echos the IP's we want to ping. Good, so far so good.

Now that we are happy with our loop we can add the ping command to our loop. Let's modify our script with the ping command instead of the echo command.

```
#!/bin/bash

for ip in $(seq 200 210); do
ping -c 1 192.168.31.$ip
done
```

So, this works but it takes a long time to complete but also has a very messy output. Let's deal with the output first:

Let's use grep and try to get something that is indicative of a live IP. How about the "bytes from" response. We can even use **cut** and the space as a delimiter. So let's include that

```
#!/bin/bash

for ip in $(seq 200 210); do
echo 192.168.31.$ip | grep "bytes from"  | cut -d " " -f4 | cut -d ":" -f1
done
```

Our output looks good, but it still slow. Let's fix that.

The reason it takes so long to finish is that we're running the ping command on each given IP in sequence. So if we're pinging 10 IP's, and it takes 1-2 seconds, it will take 20 seconds to finish.

Let's run the looped ping commands to run almost in parralelle. We can get these commands to run in the background. So we'll add an **&** to our previous code to force that command to the background.


```
#!/bin/bash

for ip in $(seq 200 210); do
echo 192.168.31.$ip | grep "bytes from"  | cut -d " " -f4 | cut -d ":" -f1 & 
done
```

Now that's working, we can tweak our IP range to 245 to get all the IP's in our range. 

That's a quick and dirty bash script. Hopefully this will inspire you to spend a little time looking into things like this. 