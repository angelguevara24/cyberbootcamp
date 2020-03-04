# Port Scanning
This exercise requires Docker. To get started, make sure you're in `Stu_Scanning_Ports/Resources`, and:

  ```bash
  # Remove running containers
  docker rm -vf $(docker ps -a -q)

  # Make sure you're in `Stu_Scanning_Ports/Resources`
  docker-compose up -d
  ```

To connect to the Target machine:

  ```bash
  # Connect to the Target machine
  docker exec -it Target bash
  ```

To connect to the Kali machine:

  ```bash
  # Connect to the Kali machine
  docker exec -it Kali bash
  ```

## Instructions
### Capturing Port Scans
Refer to the documentation at: <https://nmap.org/book/man-port-scanning-techniques.html>

Read the sections on SYN, TCP Connect, and UDP scans.

- What is NMap's default scan type?

- Why is a SYN scan stealthy?

- What's the difference between SYN and TCP Connect scans?

- What's the difference between UDP and SYN/TCP Connect scans?

- What advantage does a UDP scan afford over SYN/TCP Connect scans?

### Capturing Scan Types
Next, you'll compare and contrast these scan types by:
- Starting `tcpdump` on the scanning machine
- Running each scan against the target
- Analyzing each capture in Wireshark

Note that you can use the name `Target` _in place_ of an actual IP Address when scanning with NMap.

Follow the instructions below.

- Open two command lines on your host machine. Arrange them side by side. Run the command to attach to `Kali` in one and attach to `Target` in the other.
  - This way, you can attack the `Target` machine and capture the attack at the same time.

- On the `Target` machine, start `tcpdump`, and save its output to `/tmp/syn.pcap`.

- On the `Kali` terminal, run a SYN scan against the target.

- After the scan completes, return to the `Target` machine terminal where `tcpdump` is running, and end the capture by pressing `Ctrl + C`.

- Again on the `Target` machine, start another capture, and save its output to `~/tmp/connect.pcap`.

- Back on the Kali terminal, run a TCP Connect scan against the target.

- After the scan completes, return to the `Target` machine where `tcpdump` is running, and end the capture by pressing `Ctrl + C`.

- Start a third capture, and save its output to `/tmp/udp.pcap`.

- In the `Kali` terminal, run a UDP scan against the target.

- After some time, use `Ctrl + C` to stop the scan. Then return to the `Target` machine where `tcpdump` is running, and end the capture by pressing `Ctrl + C`.

- List the files in `tmp`. You should see your three PCAP files.

### Copying Capture Files from the Container

- Next, you'll move the captures onto your Wireshark machine.
- Use `exit` to leave the docker container for both the `Kali` and `Target` machines. You can close one of the terminal windows.

- Create a new directory, such as `~/PortScanCaptures`, and move into it.

- Run `docker ps` and copy the string on the far left listed under `CONTAINER ID` (it should look like `4db7b469ab6c`, but yours will be different). You'll need to paste it in the next commands.

- Run the following commands, replacing `<CONTAINER ID>` with the value you copied above:
  - `docker cp <CONTAINER ID>:/tmp/syn.pcap .`
  - `docker cp <CONTAINER ID>:/tmp/connect.pcap .`
  - `docker cp <CONTAINER ID>:/tmp/udp.pcap .`

- Run `ls` in the current directory. You should see your three capture files.

### Analyzing Scan Types

- Answer the following questions for each capture:
  - How many bytes did the scanner transfer during the scan?
  - How many packets were transferred during the scan?

- Open the `syn.pcap` with Wireshark. 

- Look in the **Info** column on the far right for the first TCP packet. What TCP flag(s) do you see in the first packet?
- Look in the **Info** column on the far right. What TCP flag(s) do you see in the last packet?

- Enter the filter: `tcp.port == 80`.
  - What flag do you see in the first packet?
  - What flag do you see in the second packet?
  - Which flags do you see in the last packet(s)?

Right-click on the first TCP packet in the capture, and click **Follow Stream**.

## Questions

- Identify one advantage of SYN scans over Connect scans.
- Identify one disadvantage of UDP scans over TCP scans.
- Identify one advantage of UDP scans over TCP scans.
