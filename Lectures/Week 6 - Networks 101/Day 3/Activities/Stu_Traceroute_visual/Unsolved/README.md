# Traceroute

In this exercise, you'll practice running the `traceroute` command on three other domain names.

In particular, you will:
- Open up **Terminal** (Mac) or **Command Prompt** (Windows)
- Use `traceroute` to view the path taken to get to each of the three domain names
- Visually traceroute to three domain names, and then will copy and paste the results into [Traceroute Mapper](https://stefansundin.github.io/traceroute-mapper/) to visually see the path the traffic takes around the world to its destination.
- Answer serveral questions for each of the three domain names you `traceroute`

This exercise is intended to link your existing knowledge of network devices with the new concepts of how routers are used when communicating between devices.

## Setup

This exercise requires either **Terminal** (Mac) or **Git Bash** (Windows). Access to the web based tool called [Traceroute Mapper](https://stefansundin.github.io/traceroute-mapper/). 

- Open up **Terminal** (Mac) or **Git Bash** (Windows)
  - This should drop you into a command prompt. Once you're in, follow the instructions below.


## Instructions

  - In this activity, you will `traceroute` to three domains using either **Terminal** (Mac) or **Git Bash** (Windows).

  - The three domains are:
      - hockey.org.au
      - sacfis.co.za
      - cybersecurity-switzerland.ch

   - For each domain name perfom a `traceroute` first.
   - Then for each domain name, answer the following questions:
       - Which hop took the longest time?
       - Were any hops skipped?
       - Where were there dropped packets?
   - Then copy the results of the traceroute (example below):

   ![](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Instructional/1-Lesson-Plans/Unit07-Revised-NetworkSecurity/3/Images/GP-Visual-Plotting-traceroute-hockey-au.png)
   - Paste what you copied into the text area at the [Traceroute Mapper](https://stefansundin.github.io/traceroute-mapper/) page and lick **Map it!**

   - After you click **Map it!** you should see a visual representation of the hops the `traceroute` took in the map

   - Once you visually see the hops based on the map, answer the following questions:
       - How many different countries did the traffic pass through to get to the destination?
       - How many hops were within the same country?

   - **BONUS**
      - To explore more on your own, try a few more domains of your choice and see if you can find any where the `traceroute` completes.

**Good luck!**
