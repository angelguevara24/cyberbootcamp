# Brute Force Intrusion

In this exercise, you'll practice
- Scripting request replays with Burp Intruder
- Launching brute-force attacks against weak login logic

## Instructions

**Note**

Navigate to `http://localhost/vulnerabilities/brute`

- Submit an arbitrary username and password, and send the intercepted request to Intruder.

- Parameterize the username and password in the request, and select **Cluster Bomb** as the attack type.

- Add a handful of potential usernames and passwords as Intruder payloads, then run the attack.
  - **Note**
    - The credentials `admin:password` will work, but add a few others so you can see what an unsuccessful login attempt looks like.
    - Use the username/password lists maintained by Daniel Miessler: <https://github.com/danielmiessler/SecLists>

- Review each response from the server, and identify the successful username/password combination.

- Next, navigate to `/security.php`, and set your security level to **Medium**. 

- Attempt the brute-force attack again. What's different?
