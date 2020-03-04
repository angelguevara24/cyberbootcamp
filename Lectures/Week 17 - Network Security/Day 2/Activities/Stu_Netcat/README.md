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
  # Connect to listener
  docker exec -it Kali bash

  # Connect to client
  docker exec -it Ncat bash

  # Connect to second client
  docker exec -it Attacker bash
  ```

- Connect to each machine using a seperate Terminal window.
- Be sure to check the IP Address of each machine as soon as you attach to it.

**Good luck!**

## Instructions
### Simple Connection
Get started with a simple "sanity check" drill.

- On the `Ncat` machine, start an Ncat listener.
  - You can use any port number above `1024`.

- Using the `Kali` machine connect to the listener.
  - Send a few text messages between the two.

### Allow and Deny

Refer to the documentation at: <https://nmap.org/ncat/guide/ncat-access.html>

- Return to your the `Ncat` machine, and stop the listener.

- Restart the listener, but only allow connections from the local subnet.
  - **Note**: If your IP Address is `172.54.0.2`, the local subnet is `172.54.0-255`.

- Now, on the `Attacker` machine, use Ncat to connect to the listener.
  - Simply observe the result, then move on.

- Stop the Ncat connection on both machines.
- Obtain the IP Address of the `Attacker` machine.

- Attach to the `Ncat` machine, and use `ncat` to start a listener that _denies_ connections from the `Attacker` machine.

- Attempt to make an Ncat connection, first from the `Attacker` machine, and then again from the `Kali` machine. Simply observe the result, then move on.

## Questions
- What is the advantage of using "allow" rather than "deny"?

- What is the advantage of using "deny" rather than "allow"?

- Identify one circumstance in which using "allow" instead of "deny" isn't feasible.

- Describe one situation in which Ncat would be useful to a security policy administrator.
  - **Note**: A security policy administrator is an individual who decideds which devices can access which resources.
