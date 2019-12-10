# Interpreting Snort Rules
In this exercise, you'll:
- Interpret the rules that fired in the previous exercise
- Interpret new rules
- Use the Snort documentation to research additional rule options

Refer to the Snort rule options documentation as you follow the instructions below: <http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node31.html>

**Good luck!**

## Instructions
Explain the below ICMP Echo Reply rules. Be sure to identify the:
- Action
- Protocol
- Source/destination addresses
- Meaning of each new rule option

```bash
    alert icmp $EXTERNAL_NET any -> $HOME_NET any (
    msg:"PROTOCOL-ICMP Echo Reply"; 
    icode:0; itype:0; 
    metadata:ruleset community; 
    classtype:misc-activity; 
    sid:408; 
    rev:8;)

    alert icmp $EXTERNAL_NET any -> $HOME_NET any (
    msg:"PROTOCOL-ICMP Echo Reply undefined code"; 
    icode:>0; 
    itype:0; 
    metadata:ruleset community; 
    classtype:misc-activity; 
    sid:409; 
    rev:10;)
```
---
Explain the ICMP Unusual PING rule below. Be sure to identify the:
- Action
- Protocol
- Source/destination addresses
- Meaning of each new rule option

```bash
    alert icmp $HOME_NET any -> $EXTERNAL_NET any (
    msg:"PROTOCOL-ICMP Unusual PING detected"; 
    icode:0; 
    itype:8; 
    fragbits:!M; 
    content:!"ABCDEFGHIJKLMNOPQRSTUVWABCDEFGHI"; depth:32;
    content:!"0123456789abcdefghijklmnopqrstuv"; depth:32;
    content:!"EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"; depth:36;
    content:!"WANG2";
    content:!"cacti-monitoring-system"; depth:65;
    content:!"SolarWinds"; depth:72;
    metadata:ruleset community; 
    reference:url,krebsonsecurity.com/2014/01/a-closer-look-at-the-target-malware-part-ii/;
    reference:url,krebsonsecurity.com/2014/01/a-first-look-at-the-target-intrusion-malware/;
    classtype:successful-recon-limited;
    sid:29456;
    rev:2;)
```

- There are multiple `content` options in this rule. 
  - **Important Note**: There's an exclamation mark in front of each content string. Use the documentation to find out what this means.
  - Why do you suppose this rule includes so many?
---
Explain the rule below. Be sure to identify:
- Action
- Protocol
- Source/destination addresses
- Meaning of each new rule option

  ```bash
      alert tcp $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS (
      msg:"SQL PK-CMS SQL injection attempt"; 
      flow:to_server,established; 
      content:"/default.asp?"; 
      fast_pattern; 
      nocase; 
      http_uri;
      content:"pagina="; 
      distance:0; 
      http_uri; 
      metadata:service http; 
      reference:url,github.com/BuddhaLabs/PacketStorm-Exploits/blob/master/1309-exploits/pkcms-sql.txt;
      classtype:web-application-attack;
      sid:32768;
      rev:1;)
  ```


- Based on the reference URL, which exploit does this rule monitor for?
