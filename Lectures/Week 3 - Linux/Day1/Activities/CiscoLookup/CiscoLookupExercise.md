# PwnRepo

Let's say you were tasked with finding all the domain names and sub domain names from a website like cisco.com and then their corresponding IP addresses. This could be an extremely complex and tedious task if we had to do it manually, either by right clicking and viewing the page source or manually clicking on every link. 

We can use bash to turn this into a simple task.

1. We'll start by downloading the cisco.com index page by using the command **wget www.cisco.com**

2. If we **cat** the file we can only get an idea of how large the file is but we can also see how the links are built within the HTML of the page. Take a moment and find a few examples of links in the file. 

3. Ask the students if there's anything that all of the links have that are the same, that we could search for. What we're looking for is **href=**. So let's update our command to `cat index.html | grep "href="`

4. The output we're looking at is still a bit of a miss, but we've been able to identify at least part of the data we want to extract. But there is still a lot of HTML information within this file and we're gonna want to get rid of it. 

5. Now we're introduce the **cut** command. What cut does is prints selected part of line from output, and we can use things like a delimiter to specify what exaclty we want to cut.

6. Explain that a delimiter is a character that is used to break up text streams (or data streams). One of the easiest ways to think of them is all the different forms of puncutiaton and include ` , ; " ' {} | /\ ` and the space. 

7. Update your previous command to the following: `cat index.html | grep "href=" | cut -d / -f1` and explain that the **-d "/"** specifies our delimiter and the ** -f1** specifies field one. The results of this will show you what is considered field one. Run the command and explain it.

8. Field 1 is everything in front of (but not including) the first **/**. So update your command to show `-f2` and run it to show field 2. `cat index.html | grep "href=" | cut -d / -f2` 

9. This updated comand shows only field 2, and in a few instances there are some letters/characters like the **c** in field two. So this still isn't the best, so let's tweak our command to show field 3. `cat index.html | grep "href=" | cut -d / -f3` 

10. The output here is far from optimal, but it does look better. Our text now includes several domain names, but it also includes some useless information. So let's see if we can clean up this list to include only domain names. So let's filter out the text for all the lines that do not contain **cisco.com** with the command `cat index.html | grep "href=" | cut -d / -f3 | grep "cisco.com"`

11. Now we're cooking. Every entry here is related to cisco.com, but we also see some other stuff we don't want. Like some special characters or things like double quotes. So let's use **cut** again to get rid of it. Due to character escaping, we'll want to wrap our " in a ' (single quote): `cat index.html | grep "href=" | cut -d / -f3 | grep "cisco.com" | cut -d '"' -f1`

12. Now we have a clean list but there's a lot of duplicates. So introduce the **sort** command with the **-u** option for unique: `cat index.html | grep "href=" | cut -d / -f3 | grep "cisco.com" | cut -d '"' -f1 | sort -u`

13. Now we have a nice short list of domains that were extracted from the index.html file.

14. By using some regular expressions and the grep -o command, you can get pretty much the same thing by typing the following command `grep -o '[A-Za-z0-9_\.-]*\.*cisco.com' index.html | sort -u`

15. So now that we have a nice neat list of things, let's pipe this output into a file for further processing. Let's call it cisco.txt: ``cat index.html | grep "href=" | cut -d / -f3 | grep "cisco.com" | cut -d '"' -f1 | sort -u > cisco.txt` and then cat the file to make sure it's what you expect.

16. Our situation asked us to not only extract the domain names, but also their corresponding IP addresses. We're going to do this with a simple bash **for** loop, and the Linux **host** command. 

17. To start, let's see what the **host** command does. Let's look at `host --help` and `man host`

18. After that, let's look at `host www.cisco.com` and identify the IPV4 address. We also want to look at the line to see if there's a way we can seperate it from the others, and there is, because it's the only like that contains **has address**

19. So, let's see if we can **grep** just that line: `host www.cisco.com | grep "has address"`

20. Let's see if we can use the **cut** command again to get just the field we want. Our syntax is going to end up being `host www.cisco.com | grep "has address" | cut -d "" -f4`

21. Now that we know how to extract what we want, let's open up a txt file and write a short script that will get all of the domain names and then lookup their corresponding IP addresses.

22. Let's use the **nano** text editor to create the file **cisco.sh**

23. Let's start our txt file with our first line that will specify the script that it should always be run with bash rather than another shell.

```
#!/bin/bash
```

24. Next, we're goign to add a for loop that will read each one of the lines in the cisco.txt file 
```
#!/bin/bash

for url in $(cat cisco.txt);do
```

25.  And then for each one of them, use the host command to see what their host information is
```
#!/bin/bash

for url in $(cat cisco.txt;)do
host $url
```

26. Now, we know we can clean up what is displayed 
```
#!/bin/bash

for url in $(cat cisco.txt;)do
host $url | grep "has address" | cut -d " " -f4
done
```

27.  Let's save our script, and then give it executable permissions. `chmod 755 cisco.sh`

28. And then let's execute it with `./cisco.sh`

29. And for the pro's out there, here's the whole thing in one line of bash: `for url in $(grep -o '[A-Za-z0-9_\.-]*\.*cisco.com' index.html | sort -u); do host $url | grep "has address" | cut -d " " -f4;done`

30. Granted, this bash one liner is a long stretch, it does demonstrait how versitile bash can be. 