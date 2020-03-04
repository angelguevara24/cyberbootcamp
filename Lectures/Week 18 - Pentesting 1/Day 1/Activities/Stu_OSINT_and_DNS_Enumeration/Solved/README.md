# OSINT and DNS Enumeration
In this exercise, you will:
- Familiarize yourself with Netcraft
- Use the Harvester to enumerate DNS data and collect emails

### Instructions
### Netcraft
- Select your Kali instance, and launch a web browser.

- Navigate to: <https://searchdns.netcraft.com/>

- Find all subdomains belonging to the organizations below. Keep track of how many subdomains you find for each organization.
  - Tesla
  - SpaceX
  - Amazon
  - Offensive Security
  > **Solution**: You'll find 2 subdomains for Tesla; 2 for SpaceX; 1 for Offensive Security; and 93 for Amazon.

### The Harvester
- Select your Kali instance, and launch a Terminal.

- Use the Harvester to enumerate emails and subdomains for each of the above organizations. Compare the number of subdomains discovered to those retrieved by Netcraft. Do you notice discrepancies?
  > **Solution**: You should notice additional results from the DNS enumeration. E.g., my enumeration of `theharvester -d tesla.com -l 200 -b google` yields the following subdomains:
  > - 3.tesla.com:104.124.64.70
  > - forums.tesla.com:104.124.64.70
  > - inside.tesla.com:209.133.79.21
  > - ir.tesla.com:104.122.169.102
  > - shop.tesla.com:104.124.64.70
  > - www.tesla.com:104.124.64.70

- Repeat the above searches, but change the search engine. Use each of the below in _different_ commands:
  - Baidu
  - Bing
  - Google Plus
  - PGP

- Which search engines produced the best results for emails? What about for DNS subdomains?

  > **Solution**: On my runs, Baidu and Bing produced good results for emails for all organizations. Google produced the best DNS enumeration results.
