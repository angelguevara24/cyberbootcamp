## ARP & Rarp

**ARP** 

- **Based on the information displayed in Wireshark, what is the purpose of ARP?**

![images](images/barp.png)

- ARP a.k.a Address Resloution Protocol, matches the IP address of a machine, to a MAC address of the machine. 

- **What are the IP and MAC addresses of device sending ARP requests and responses**
- The gateway address 192.168.0.2 with the mac of d8:5d:e2:78:ee:3d and the computer with the IP address of 192.168.0.7 with the Mac address of 8c:85:90:c0:6e:ec
- On your personal computer open CMD (Windows Users) or your terminal (Mac users) and type the command `arp -a`. And answer the following
   - **Why are there ARP configuration stored onto your computer?**
   - ARP has a table where it stores it's cache memory for future reference. 
   - **Why are there Static and Dynamic ARP configurations?**
   - The *dynamic* portion of the ARP table is only set there for a period of time before self deliting. This is to avoid excessive usage of memory on the computer. The *static* portion of the ARP table, is for when you have two hosts that talk to each other often, the static ARP cache will already have the IP address and hardware address information saved. 
   - **Will a host update it's ARP cache for every ARP request?** 
   - A host will update its ARP cache, only if the ARP request is for its IP address. Otherwise, it will discard the ARP request.

**RARP**

- Look at the RARP pcap file entitled "rarp.pcap file. "

  ![images](images/rarp.png)

- **Based on the information displayed in Wireshark, what is the purpose of RARP?**

- RARP is short for Reverse Address Resolution Protocol, thats the information about a Mac address, and pairs it with an IP address. 



