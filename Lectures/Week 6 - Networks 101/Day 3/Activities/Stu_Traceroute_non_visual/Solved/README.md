# Traceroute

In this exercise, you'll practice running the `traceroute` command on three different domain names provided below.

In particular, you will:
- Open up **Terminal** (Mac) or **Command Prompt** (Windows)
- Use `traceroute` to view the path taken to get to each of the three domain names
- Answer serveral questions for each of the three domain names you `traceroute`

This exercise is intended to link your existing knowledge of network devices with the new concepts of how routers are used when communicating between devices.

## Setup

This exercise requires either **Terminal** (Mac) or **Git Bash** (Windows). 
Open up **Terminal** (Mac) or **Git Bash** (Windows)

This should drop you into a command prompt. Once you're in, follow the instructions below.


## Instructions

  - In this activity, you will `traceroute` to three domains using either **Terminal** (Mac) or **Git Bash** (Windows).
       > **NOTE**: `traceroute` results can vary depending on the originating network and destination network 

  - The three domain names are:
      - centurylink.com
      - social-engineer.com
      - pcmag.com
 
  - Run these steps for each of the three domain names listed above
      - Open up **Terminal** (Mac) or **Git Bash** (Windows)
      - Use the appropriate `traceroute` command based on the operating system being used
        > **Solution**: (Mac) `traceroute <domainname.com>` or (Windows) `tracert <domainname.com>`
      - For example, if using a Mac, here is the syntax and output when performing a `traceroute` to centurylink.com:
        > **Solution**: `traceroute centurylink.com`
        ![](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Instructional/1-Lesson-Plans/Unit07-Revised-NetworkSecurity/3/Images/traceroute_non_visual_centurylink.png)

   - As you are performing a `traceroute` for each domain, answer the following questions:
      - Which hop took longest time?
      - Were any hops skipped?
      - Where were there dropped packets?
      - Did the traceroute complete?

   - **BONUS**
      - To explore more on your own, try a few more domains of your choice and see if you can find any where the `traceroute` completes.

**Good luck!**
