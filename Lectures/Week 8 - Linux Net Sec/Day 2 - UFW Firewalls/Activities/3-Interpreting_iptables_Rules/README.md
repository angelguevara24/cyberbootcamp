# Interpreting iptables Rules

In this exercise, you'll combine research with what you know about `iptables` to interpret common firewall rulesets, extracted from real configurations.

You'll be presented a series of `iptables` rules, each of which comes with a set of questions. Some answers you'll already know from lecture. Others, you'll have to research.

Any questions you need to research can be found in the `iptables` user manual, which you can access on the command line with: `man iptables`.

Recall that you can search the manpages for a specific flag with:
  - `man iptables`
  - `/-[flag]`

So, if you want to find out what the `-F` flag does, you'd open the `iptables` manual, then type: `/-F`, and hit enter. Press 'n' to scroll through search results, and you'll hae your answers in no time.

**Good luck!**

## Instructions

### Flushing the T...able?

- Sysadmins often write scripts that set up their `iptables` rules automatically. One of the first things many administrators do before configuration is clear all existing rules, so they can start fresh.

- The snippet below contains a series of commands from a configuration script that clear `iptables` rules. Read them, and use the manpages to answer the questions below.

  ```
  # Clear existing rules
  iptables -F
  iptables -F -t nat
  iptables -X
  iptables -P INPUT DROP
  iptables -P OUTPUT DROP
  iptables -P FORWARD DROP
  ```
#### Questions

- What do the manpages say about the `-F` flag?

- What do the manpages say about the `-t` flag? What does `nat` represent in the second line of the above snippet?
  
- What do the manpages say about about the `-X` flag? 

- What do the manpages say about about the `-P` flag? 

- Using the above, explain, in English, what the following lines from the configuration do.
  - `iptables -F`: 
  - `iptables -P INPUT DROP`: 
  - `iptables -P OUTPUT DROP`: 
  - `iptables -P FORWARD DROP`: 

#### INPUT Rules

- Review and research the snippet, then answer the questions below.

  ```
  # The subnet this server lives on
  SUBNET = 192.168.10.0/24

  # State rules
  iptables -A INPUT -m state --state INVALID -j LOG --log-prefix "DROP INVALID "
  --log-ip-options --log-tcp-options
  iptables -A INPUT -m state --state INVALID -j DROP
  iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
  
  # ACCEPT rules
  iptables -A INPUT -i eth1 -p tcp -s $SUBNET --dport 22 --syn -m state  --state NEW
   -j ACCEPT
  iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
  ``` 

#### Questions

- What do the manpages say about the `-A` flag?

- What do the manpages say about the `-m` flag?

- After  the `--state` flag in the first three rules, we see a few different values: INVALID, ESTABLISHED, and RELATED. NEW is also a possible value, which you'll see in the next section. Refer to the section on **The Connection Tracking Module** in this document, and define each below: <https://www.booleanworld.com/depth-guide-iptables-linux-firewall/>.
  - INVALID: 
  - ESTABLISHED: 
  - RELATED: 
  - NEW: 


- According to the manpages, `-j` specifies a chain to _jump_ to if the packet matches the rule `-j` appears in.
  - Look at the first rule in the `# State` section above. Suppose a packet matches this rule. Given the `-j` flag, what will the firewall do with the packet next?

- The rules in the `# ACCEPT` section are a little more complicated. Let's work through them together.

- Consider the first: `iptables -A INPUT -i eth1 -p tcp -s $SUBNET --dport 22 --syn -m state  --state NEW`
  - `-A INPUT` says: "Append this rule to the end of the INPUT chain."
  - `-i eth1` says: "Apply this rule to packets coming in from the `eth1` network interface."
  - `-p tcp` says: "Apply this rule to packets sent over `tcp`."
  - `-s $SUBNET` says: "Only accept TCP packets sent from the local subnet..." (continued below)
  - `--dport 22` says: "...connecting to port 22..." (continued below)
  - `--syn` says: "...if they have _only_ the `SYN` flag set."
  - `-m state --state NEW` says: "Only accept packets that meet these conditions if they meet the previous conditions _and_ are starting a new connection."

- In English, this rule says:
  - "I'm adding a rule to the input chain. The rule is: _Only_ allow TCP packets to connect to port 22 on this server if they are initiating a NEW connection; have _only_ the SYN flag set; and come from within the local subnet."
  - Port 22 is for SSH, so we could also say: "I'm adding a rule to the input chain. The rule is: _Only_ allow TCP packets to connect to port 22 on this server if they are initiating a NEW connection; have _only_ the SYN flag set; and come from within the local subnet."

- Given the above explanation, what do you think the final rule specifies?
  - Research what the ICMP protocol is used for.
  - The final rule says: "Accept all ping messages sent to this server."
    - Ignore the `echo-request`; this is a minor detail we needn't concern ourselves with right now.
