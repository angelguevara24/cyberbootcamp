## Juice it for all it's worth


In this next activity you will be taking on the roll of a black hat penetration tester. You will be given a lists of tasks that you need to complete using the skills you've picked up this past week. 
This is a challenging lab, but hints will be provided to you. It's encouraged that you try your best and work with a neighbor _before_ looking at the hints.

---

### Set Up

Install OpenVPN onto your VM by running the following commands:
- `apt-get update`
- `apt install openvpn`.

Set up an account with tryhackme.com. 
- On the side panel under **Learn** click on **Access**, then click on the green button entitled **Download your config file**.
- Return to your terminal, and in the same directory as your config file run the command `openvpn <your config file>`.
  - You will know if this has succeeded when terminal has completed sending updates and you read `Initialization Sequence Completed`.
- Return to  https://tryhackme.com/access and verify that the subsection **Connected** under **Network Information** has a green checkmark. 
  - If not, reload the page. 
- Navigate to https://tryhackme.com/room/juiceshop and click **[Task 1] Connect To Our Network** Then click **Deploy**. Enter the IP address that is then assigned to you, into the toolbar. 

Move onto the instructions. 

### Instructions

Welcome to the OWASP Juice Shop. This shop was designed by the OWASP organization based off of thier **OWASP Top 10 Vulnerabilities List**. Your job is to exploit the the juice shop's vulnerabilities, using your newly developed skills and tools from the past two weeks. To get started, complete each exploit below:

- Locate the `Score board`
  - **Hint:** This needs to be done first to understand the rest. 
- Confidential Document
- Error Handling
- Redirects Tier 1 **Please Skip**
- Score Board
- XSS Tier 0
- XSS Tier 1
- Zero Stars


Try to score as many points as you can before time runs out!
