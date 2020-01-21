## Injection

**Definition**

Injection attacks occur when the user is able to input untrusted data tricking the application/system to execute unintended commands.

**Example**

A hacker could inject code that is then processed onto a remote server to retrieve confidential information. 

**Countermeasure**

Input sanitization: Implement whitelisting approach at server side for what all can be accepted.

Use of safe API’s and parametrized queries.


## Broken Authentication

**Definition**

Broken authentication occurs when the application mismanages session related information such that the user’s identity gets compromised. The information can be in the form of session cookies, passwords, secret keys etc.

**Example**

A few examples are:

- Passwords, session IDs, and other credentials are sent over unencrypted connections, leaving them vulnerable to MITM attacks.
- Session IDs are exposed in the URL, leaving them to "shoulder surfing" attacks.
- User authentication credentials are not protected/encrypted/hashed when stored, leaving them vulnerable to injection attacks.

**Countermeasure**

Use of multifactor authentication. 

Use of encryption of data-in-transit.

Encrypting stored passwords.

Input sanitization.

Using secured cookies.


## Sensitive data exposure

**Definition**

Attackers can sniff or modify the sensitive data if not handled securely by the application. A few examples include use if weak encryption keys, use of weak TLS.

**Example**

In the previous example, we talked about how data, when unencrypted could leave it exposed to MITM attacks. For example, if I were to log onto "**http**://fakeblock.com" and a hacker was running a packet sniffing program such as wireshark, they would be able to capture my credentials in plain text due to the lack of security associated with using the "http" protocol. 

**Countermeasure**

Encrypt all data in transit and at rest.

Use secure protocols and algorithms.

Disable caching of responses with sensitive data. Hackers might get the cached copies and steal the information from them.


## XML External Entities 

**Definition**

An application is vulnerable to XXE attacks if it enabled users to upload a malicious XML which further exploits the vulnerable code and/or dependencies.

**Example**

Extensible Markup Language (XML) is a language that sets rules for encoding documents in a format that is both human-readable and machine-readable. Similar to injection attacks malicious users would be able to inject code to retrieve confidential information from the remote server. 

**Countermeasure**

Avoid serialization of sensitive data. 

Implement whitelisting approach at server side to prevent malicious XML upload.

Use of WAF to detect and block XXE.

Code review. 


## Broken Access control

**Definition**

Broken access control occurs if a user is able to access unauthorized resources, this can be access to restricted pages, database, directories etc.

**Example**

This could take many forms such as privilege escalation or privilege creep.

**Countermeasure**

Invalidate tokens and cookies after logout.

Forced login/logout after a password change.

Server side resource restriction e.g. directories.

Restrict access to all resources basis roles.


## Security misconfigurations
Introduction

**Definition**

Developers and IT staff ensure functionality and not the security. The configurations are done on the application server, DB server, proxy, applications and other devices need to be in line with the security requirements. 

**Examples**

A worker could accidentally place a private directory listed onto the company website. 
Use of default passwords.
Use of outdated technology


**Countermeasure**

Have a hardening process in place for both hardware and applications. Do ensure that defaults are changed.

Install only the required features from a framework.

Review the security of the configurations at fixed intervals.


## Cross Site Scripting 

**Definition**

Cross-site scripting occurs when an attacker is able to insert untrusted data/scripts into a web page. The data/scripts inserted by the attackers get executed in the browser can steal users data, deface websites etc.

**Example**

Similar to injection attacks, an attacker could inject javascript or SQL code that is processed onto a remote server to retrieve confidential information. 

**Countermeasure**

Output encoding and escaping untrusted characters.

Enabling Content-Security-policy (CSP).


## Insecure Deserialization

**Definition**

Some of the applications save data on the client side and they may be using object serialization. Applications which rely on the client to maintain state may allow tampering of serialized data.

**Example**

When save data is saved onto a local hard drive, this allows the user to insert there own code into the data to be taken back to the server. 

**Countermeasure**

Encryption of the serialized data.

Deserializers to run with least privileges


## Using Components with known vulnerabilities

**Definition**

If any components with known vulnerabilities are used by the application, this may lead to security breaches or server takeover. The components can be coding frameworks, libraries, vulnerable functions, network frameworks etc.

**Example**

As of April 11, 2017 Windows has stopped providing security updates and hot-fixes to their operating system. However vulnerabilities that affect the current generation of use also affect past generations. This means that although our new computer is fixed, older models like the Windows Vista computer would be vulnerable. 

**Countermeasure**

Frequent patching process.

Subscribe to various forums which share the latest vulnerabilities along with the CVE numbers and mitigation techniques/fixes. Check if the vulnerability affects the devices/software in your inventory and fix them.


## Insufficient logging and monitoring

**Definition**

With all the countermeasures in place attacks still happen and that gets noticed only after an incident has happened. If undetected the attackers could have compromised the systems long back and gained persistence. 

**Example**

If a company does not have an intrusion detection system, or monitor the one the have closely, then it would be difficult to say when an attacker has penetrated the defences, what they did when they were there, and if they are still there. 

**Countermeasure**

24x7 monitoring of application traffic and log analysis.

Effective Security Incident and response procedures to be in place and practice. 
