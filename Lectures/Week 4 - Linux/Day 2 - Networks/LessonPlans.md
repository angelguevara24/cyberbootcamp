# PwnRepo


## ifconfig

If config is one of the most basic commans you'll be utalizing, and it's crutical in understanding and interacting with active network interfaces. 

What is an Interface? An interface is place where a device connects to a network. 

Loopback interface - so it can talk to programs on the same computer. 

And (usually) each interface may have different destinations, and it's important for your computer to know where to talk to next if it doesn't know who it needs to talk to. 

An interface needs to know three things:
    
* Its IP address. Without this, it doesn't know what traffic is for it and what isn't for it. 
* A default gateway. This is where you send traffic that isn't local to you. It's usually the IP address of your router, or firewall, or whatever will be forwarding your traffic on to some other network that is beyond what is local.
* Subnet Mask: Determines what gets sent to the default gateway vs what is local traffic. Your printer, your TV, your mom's computer, whatever. 
    * If your subnet mask is incorrect you'll either be sending traffic that's supposed to be local out to computers outside your network or sending traffic ment for the internet will be sent locally, trying to use something like ARP, and timing out.

So, let's use your network here, or your home network, it's pretty simple. Probably just one or two networks. Let's say your computer wants to hit Google. It can easially determine if it's going to send the connection through your network or if it's able to send it locally. 

So your computer says:
1. I wanna talk to Google, so I'm going to use my LAN interface, and going to send traffic to my default gateway. 
2. Your home router has a little bit more of a complicated decision. It has to figure out if this is on its home network (192.168.1.something) or does it need to go somewhere else. It's not, so I'm going to use MY default gateway, which is your ISP's router. 
3. Your ISP has to figure out is this other customer traffic that has to go through one of my other interfaces to talk to customers or do I need keep going. 
4. During all of this, each router asks itself "Do I know where to send this? No? I'm gonna send it to my gateway."
5. Eventually, you'll get to a router that knows every direction/decision. It has no default gateway. This is called a backbone router. It is a router that knows, given any IP address, where the packet needs to go. 

## Trace Route

## Changing your IP address

This can be important for not only trying to discuise yourself (though it's by far the best way) but more importantly it will help you access other networks while appearing as a trusted device on those networks. For example, if there's a DOS attack, you can spoof your IP so that the attack appears to come from another source, thus helping you evade IP capture during forensic analysis. It can also be helpful if you're doing some things like firewall configurations and you need to be on a machine on the same subnet, and other administrative or engineering tasks. 

Do change your IP, we'll use the **ifconfig** command.

```ifconfig eth0 192.168.181.115```

If all worked well, that's it. 

You can also change your network mask and broadcast address with something like this: 
```ifconfig eth0 192.168.181.115 netmask 255.255.0.0 broadcast 192.168.1.255```


## MAC Addresses

The MAC is a unique identifier assigned to a network interface controller. 

MAC addresses are used to identify machines within the same broadcast network on layer 2, while IP addresses are used on layer 3 to identify machines throughout different networks.


Why modify your MAC?

1. Increase anonymity
2. Inpersonate other devices
3. Bypass filters

If we bring up **ifconfig** we can see what our MAC addresses are. 

1. We can change it manually by doing the following: `ifconfig eth0 down ` to take down the interface

2. Now that the interface is disabled, we can modify it's options. So let's do `ifconfig eth0 hw ether 00:11:22:33:44:55`

3. Let's now enable the interface with `ifconfig eth0 up`

4. Now that we know how to do it manually, let's write a script to do it for us.

## Our Program

Our program needs to be able to execute terminal/Linux commands the same way we're typing them into the terminal. In Python, there is a module called **subprocess** that allows us to execute system commands. If we're on a Mac, it'll run Mac commands, if we're in a Linux box, it'll run Linux commands, etc. Information on this module is here: https://docs.python.org/2/library/subprocess.html

From this module, the function that we want to use is called **call** This allows us to run system commands, in the foreground, and waits for the command to finish exedcuting before it continues to the next line. This is very important because we don't want our program to try to do other stuff while it tries to wait for the previous command to run, like disabling the interface. 

If we look at the documentation, we see there's two ways to run this. We're gonna do the following
```
    import subprocess
    subprocess.call("COMMAND", Shell=True)
```

Subnet - a general term used to describe a range of IP addresses that can be represented as a network address and size 


https://www.ipaddressguide.com/ip

