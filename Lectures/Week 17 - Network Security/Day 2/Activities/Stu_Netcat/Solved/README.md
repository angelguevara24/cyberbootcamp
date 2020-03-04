# Connecting with Ncat
In this exercise, you will:
- Use Ncat as a server to listen for connections on a port
- Use Ncat as a client to connect to a port
- Explore Ncat's access control features

The goal of this activity is to give you experience with using Ncat to:
- Start listeners
- Connect to devices
- Test access control rules

---

This exercise requires Docker. To get started, make sure you're in `Stu_Netcat/Resources`, and run:

  ```bash
  # Remove running containers
  docker rm -vf $(docker ps -a -q)

  # Make sure you're in `Stu_Netcat/Resources`
  docker-compose up -d
  ```

You'll need to connect to three machines in this exercise. The commands to do so are:

  ```bash
  # Connect to Kali
  docker exec -it Kali bash

  # Connect to Target_1
  docker exec -it Ncat bash

  # Connect to Target_2
  docker exec -it Attacker bash
  ```

- Verify the IP addresses for each machine:
  - **Solution**
    - `ifconfig`

**Good luck!**

## Instructions
### Simple Connection
Get started with a simple "sanity check" drill.

- Attach to the Ncat machine, and start an Ncat listener.
  - **Solution**
   - `docker exec -it Ncat bash`
   - `ncat -lvp 2222`

- Open a new Terminal window and attach to the Kali machine, then connect to the listener.
  - **Solution**
    - `docker exec -it Kali bash`
    - `ncat <Ncat machine IP> 2222`

### Allow and Deny
Refer to the documentation at: <https://nmap.org/ncat/guide/ncat-access.html>

- Stop the ncat connection on both machines.
  - **Solution**: `Ctrl + C` on both machines.

- Restart the ncat on on the `Ncat` machine, but only allow connections from the local subnet.
  - **Solution**: `ncat -l --allow 172.27.0.0-255` (verify you are using the correct Network)

- Open a third Terminal window and connect to the `Attacker` machine.
  - **Solution**
    - `docker exec -it Attacker`

- Then, use Ncat to connect to the `Ncat` server.
   - **Solution**: `ncat <Ncat machine IP>`

- Stop Ncat and verify your new machine's IP Address.
  > **Solution**: `Ctrl + C` then `ifconfig`

- Return the the terminal for the `Ncat` machine and start a listener that _denies_ connections from the IP Address of the `Attacker` machine.
  > **Solution**: `ncat -lvp 2222 --deny <Attacker machine IP>`

- Attempt to connect to the Ncat listener first from the `Attacker` machine and then from the `Kali` machine. Simply observe the result, then move on.
  > **Solution**: The connection should be allowed from the `Kali` machine, but denied from the `Attacker` machine.


## Questions
- What is the advantage of using "allow" rather than "deny"?
  - **Solution**: Using "allow" instead of "deny" allows you to specify _exactly_ who can connect, and deny everyone else, which offers strong access controls.

- What is the advantage of using "deny" rather than "allow"?
  - **Solution**: Using "deny" allows _anyone_ to request access, which is a requirement for public servers, which can't know the IP Address of legitimate clients ahead of time.

- Identify one circumstance in which using "allow" instead of "deny" isn't feasible.
  - **Solution**: Using "allow" to control access to a web server is impossible, because you can't whitelist the IP Address of new users you haven't seen yet.

- Describe one situation in which Ncat would be useful to a security policy administrator.
  - **Solution**: Ncat is useful for verifying access control rules with real connections.
