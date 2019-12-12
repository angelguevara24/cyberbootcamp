# Firewall Policies

In this exercise, you'll work with a partner to design and implement a firewall policy. You will:
- Audit the services each machine furnishes
- Determine which ports should be exposed
- Design and document a firewall policy for each machine
- Implement the policy on each machine

The goal of this activity is to expose you to the full process around developing access control policies—from determining what should be available, to implementing controls that expose only these precise resources.

## Part 1

**Instructions:**

In this activity you have been put in charge of maintaing your companies firewall policy. Listed below are three systems that will need access to the internet. Your job is to read each description, verify the **services** and choose which **ports** that each system uses. 

    
**User Data API**
    
- **Description**: Web server that provides access to organization's IAM database. This machine runs an HTTP and HTTPS server, which should be available to all machines on the subnet. There is also an SSH listener, which should only allow access from the command server. Disable connections to all other running services.     

  - **Service(s)**: 
    
  - **Port(s)**: 
  
**User Database**
  
- **Description**: MySQL server containing user data for IAM policies. Should _only_ be accessible by the User Data API server.
  
  - **Service(s)**: 
  
  - **Port(s)**: 
  
**Command Server**
  
- **Description**: Server responsible for controlling whether other servers on the network are up or down. Allows administrators to log in remotely to issue commands. Block all requests to the telnet server that _do not_ come from the local subnet. Allow outgoing SSH and telnet connections to other machines within the subnet.
  
  - **Service(s)**: 
  
  - **Port(s)**: 

## Part 2 

**Implementing Access Controls**

  Refer to these UFW documents:
  [Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands) and [How to Setup a Firewall with UFW](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)

  - Next, create a policy for each of the systems above using `ufw` to set the appropriate rules for each system. Specifically for each system, complete the following:
    
    - Enable UFW.
     
    - Set a default rule to deny all incoming and outgoing traffic.
      
    - On each machine, create rules exposing the ports you identified above.
          
        **Note**: You should allow _both_ incoming _and_ outgoing connections to each port.
      
    - Save each machine's configuration in a file called: `/tmp/<machine_name>.policy`.
    


**Generating Documentation**

  - Finally, create and move into a directory called `Policies` and copy over the policy files and benchmark you created.
