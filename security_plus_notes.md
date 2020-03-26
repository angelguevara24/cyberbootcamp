### Risk Mangement:

>**Security Controls:**

 + **Admin Control:**
  - Controls actions that people take towards Security
    + Laws
    + POlices
    + Guidelines
    + Best practices
  
 + **Tecnical controls:** 
    + Refers to techincal action towards security: 
    + Firewall polices
    + Password links
    + Authentication
    + Authorization
    + Encryption
  
 + **Physical controls:**
    + Refers top actions taken to proetect a secure area: 
    + Gates
    + Control access
    + Keys
    + Guards 
 
 
 ### Security Controls Functions:
 
 + Deterrent: it deters the actor from attempting the threat action.
 + Preventite: it deters the actor from performing the threat action.
 + Detective: recognizes an actor's thread ot actions.
 + Corrective: It tries to mitigate a thread action that already happened
 + Compensating: it provides alternative way to apply ot fix any of the above. 
 
 
 **Security control Examples:**
 
 **Firewall install:**
 
 SC Fuctions | Adminstrative | Technical | Physical
 :-----: | :-------------: | :---------: | :--------:
 Deterrent | 
 Preventiative | [x] | [x]|
 Detective |
 Compensanting | 
 Corrective |
 
    
    
>Defense depth:

+ Diversity: Ir refers multiple tools, concepts or protocols to a determine activty. Example: Running Internet off of different service providers. Running your distribution layer between 2 different vendors, Cisco and Junos
+ Redundancy: It applies the same concept or tool over and over again to make sure its service keep running. Example: Failover FWs both supplies the same services over and over, but one of them is on a standby mode waiting for the active unit to fail.
 
>Security Controls ---> Security Governance: 

+ Laws and regulations
 + Regulations:
   - HIPA
 + Standards:
   + NIST
+ Common Sense and experience:
  + As a professional just apply best known practices, and polices that are general knowledge in the industry, 
  
  
 
 ## msfconsole starting DB: 
  
  https://www.kali.org/docs/tools/starting-metasploit-framework-in-kali/

```
sudo service postgresql start
#
sudo msfdb init
#
msfconsole
#
db_status
```
**Create a workspace:**

```
workspace -a <name_workspace>
```

## nmap most common flasg: 

```
-n (no DNS resolution)
-Pn (no Ping)
-sT (Full TCP hand-shk)
-sS (TCP sync only)
-sU (UDP scan)
-T{1-4} controls the speed of the scan
```

##Password List Kali:

```
/usr/share/wordlists
```
