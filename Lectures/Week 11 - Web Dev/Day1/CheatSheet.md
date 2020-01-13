# Day 1 Cheat Sheet — Introduction to the Modern Web

## Key Terms

- **Attack Surface**: the sum of all points or vectors the attacker can try to enter or extract data in an environment.
  > **Example**: There are network and software attack surfaces that are available to unauthenticated users.
  
- **Risk Assessment**: evaluating the potential risks with an environment
  > **Example**: Organizations conduct risk assessments to understand the assets with the highest risk to then implement security controls to protect them.
  
- **Penetration Testing**: the practice of testing a web application, network, or computer system to discover security vulnerabilities that can be exploited by an attacker.
  > **Example**: Companies conduct penetration tests, also called pen tests, to see where their weaknesses are so controls can be put in place to address the vulnerabilities, reducing risk.
    
- **Security Engineering**: a specialized role focusing on engineering aspects of security 
  > **Example**: There are network and software attack surfaces that are available to unauthenticated users.
    
- **IoT Devices**: the Internet of Things (IoT) is a network of nonstandard computing devices that connect wirelessly and transmit data.
  > **Example**: refrigerators, smart TVs, wearables, smart applications, etc.
    
- **Threat Actors**: an entity that has the potential to impact an organizations security
  > **Example**: criminals, hacktivists, state-sponsored attackers and insiders
    
- **Phishing**: the act of sending email in a fradulent manner to trick the recipient to reveal personal information like credit card numbers or passwords.
  > **Example**: phishing emails look like they are coming from your bank or other company you may do business with asking you to click on a malicious link to login or even download malware.
    
- **Spear-phishing**: similar to phishing but more focused on an individual or group of individuals 
  > **Example**: certain departments are usually targeted with phishing emails
    
- **SQL Injection**: type of computer attack where malicious code is embedded in an application that uses a SQL database as the backend.
  > **Example**: In 2017, SQL Injection attacks were the number one application security risk based on the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project).
    
- **HyperText Transfer Protocol (HTTP)**: protocol used by the World Wide Web and defines what actions browsers and servers take as well as how messages are transmitted and formatted.
  > **Example**: http is plaintext transmissions of data whereas HTTPS is a secure (encrypted) transmission.
    
- **Clients/End Devices**: these are the devices, or hosts like workstations and laptops (and even mobile devices) that connect to servers and other networking devices
  > **Example**: Clients like laptops and workstations connect to web servers hosting a web site
    
- **Routers**: network devices used to route traffic and connect two or more different networks together
  > **Example**: Your ISP provides you with a router to access the internet between your home network and the internet (which is another network).
  
- **Access Point**: wireless devices used by clients to connect to the network. 
  > **Example**: some routers also have a wireless access point build into them
    
- **Proxy Servers**: servers that sit in between the users (clients) and the internet
  > **Example**: user requests to go to a website but it's the proxy server that actually makes the requset out to the internet on behalf of the user/client.
      
- **Servers**: computers that have a specific role or purpose for clients/users
  > **Example**: web servers, database servers, email servers, etc.
      
- **OSI Model**: the open systems interconnection model (OSI model), which is a conceptual framework, describes the functions of a telecommunication or networking system
  > **Example**: There are seven layers of the OSI model: Physical Data Link, Network, Transport, Session, Presentation, and Application.
      
- **Application Layer**: the seventh layer of the OSI model indicating the interface methods used by hosts in a communications network.
  > **Example**: File Transfer (FTP), Email (SMTP), Web surfing (80) are all application layer protocols.
      
- **Gateway**: a router or computer that is the last "hop" on a network before it goes out to the internet
  > **Example**: in a local area network (LAN), the default gateway is usually the router, as it's the way out to the internet from the LAN.
      
- **Incident Detection System**: security device or solution that monitors network traffic for anomalies and sends an alert if one is detected.
  > **Example**: Not to be confused with an Incident Prevention System (IPS) which also looks for anomalies like an IDS but it actually takes actions to "prevent" issues.
      
- **Firewall**: a software or hardware devices used to allow or deny traffic to/from a network based on rules and policies.
  > **Example**: windows firewall (software), hardware firewall (CheckPoint)
      
- **Cross-site Scripting (XSS) attacks**: type of injection attack where malicious scripts are injected into otherwise valid and trusted websites.
  > **Example**: In 2017, XSS attacks were the number seven application security risk based on the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project).
        
- **Request/Response Cycle**: when a client, like a browser, issues a request to a server
  > **Example**: browser to web server to fetch a web page.
          
- **Client/Server Architecture**: the relationship and system of client (user device) connection to servers that host a particular service like email, web, or database.
  > **Example**: browsers (client) requests webpages on web servers (server)
          
- **HTTP Request**: information (a packet, usually consists of binary data) that one computing device sends to another computing device to communicate.
  > **Example**: An HTTP client sends an HTTP request to a server in the form of a request message
          
- **GET Request**: client requests information from a server.
  > **Example**: client initiates a GET request for a web page
          
- **POST Request**: the opposite of a GET request, when a client sends a request that the web server should accept
  > **Example**: submitting a form on a web page or uploading a file.
          
- **Query Parameters**: a specific set of parameters attached to the end of a URL
  > **Example**: many url requests after submitting a web form add query parameters at the end once submitted
          
- **Headers**: displayed in the request and response messages of message headers for HTTP
  > **Example**: There are four types of HTTP message headers: general, request, response and entity.
            
- **Request line**: contains the request type; the name of the requested resource; and the version of HTTP in use
  > **Example**: can also contain query parameters, which allow the client to send data to the server.
            
- **User-Agent**: tells the server that this request is coming from a particular browser
  > **Example**: `User-Agent: Mozilla/4.0` tells the server that this request is coming from a Mozilla 4.0 browser.
            
- **HTTP Response**: a packet of info sent by a server to a client in response to an earlier request initiated by the client.
  > **Example**: HTTP Responses consist of a status line, headers, response body, and blank line.
            
- **Status Line**: containing the response status code
  > **Example**: here is a list of all the [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) and their definitions.
            
- **HTTP status code 200**: indicates "success" or "ok"
  > **Example**: the server came back that the status of the connection is good
              
- **HTTP status code 300**: indicate "multiple choices"
  > **Example**: the server can respond to the request in more than one way
              
- **HTTP status code 400**:  indicate "client errors"
  > **Example**: the client sends a badly formatted request
              
- **HTTP status code 500**: indicate "server errors"
  > **Example**: the server application failed somehow
                
- **cURL**: a command-line utility for sending HTTP requests
  > **Example**: simplest use of cURL simply fetches the HTML for a web page using a GET request `curl example.com`
                
- **HTML**: the code used to define the structure and content of a web page
                
- **CSS Stylesheets**: describe the appearance and layout of web page
  > **Example**: CSS rules come in three main flavors: Simple Tag Rules, Class Rules, and ID Rules.
                
- **Javascript**: JavaScript (JS) is the programming language used by browsers to manipulate web pages.
  > **Example**: allows us to create interactive pages that update dynamically.
                
- **Rich Media**: such as images, videos, and audio
                
- **Simple Tag Rules**: used to change the way the browser renders a tag everywhere on the page
  > **Example**: set the background of every paragraph tag (`<p>`) to blue.
                
- **Class Rules**: allow developers to change how specific elements on the page appear.
  > **Example**: if a developer puts the CSS class `.blue-background` on five different elements, each of those elements will have a blue background.
                  
- **ID Rules**: allows developers to change how one specific element on the page appears.
  > **Example**: IDs are similar to classes, but can only be used for a single element on the page.
                  
- **AJAX**: allows web applications to send and request data from servers on the web.
  > **Example**: used on legitimate sites like BuzzFeed to load more and more content as users scroll down the page (“infinite scroll”).
                  
- **JSON**: JavaScript gave rise to JSON, or JavaScript Object Notation, one of the most popular ways for clients and servers to format request/response data
  > **Example**: syntax is identical to the syntax used to create objects in JavaScript (which are equivalent to dictionaries in Python).
                  
- **Wireshark**: world's widely-used network protocol analyzer
  > **Example**: lets you see what is going on on your network at a very granular level.
                    
- **Snort**: open source intrusion prevention system (IPS) capable of real-time traffic analysis and packet logging for Linux and Windows to detect emerging threats
  > **Example**:easy to install and configure for a simple NIPS solution
                    
- **Clickjacking**: trick a user into clicking on a button or link on another page when they were intending to click on a different part of the page
  > **Example**: routing users to another page, most likely owned by another application, domain, or both.
                    
- **Same-Origin Policy (SOP)**: the sum of all points or vectors the attacker can try to enter or extract data in an environment.
  > **Example**: prevents pages from loading malicious resources from foreign hosts
                    
- **Cross-Origin Resource Sharing (CORS)**: Browsers allow servers to bypass the SOP with a special mechanism
  > **Example**: allows browsers to perform cross-origin GET and POST requests.
                    
- **CORS Preflight Request**: when trying to load a resource from a different domain, a browser will first send a CORS Preflight Request
  > **Example**: a request that uses special headers to ask if the server understands cross-origin requests.                  
                    
- **Developer Tools**: used for inspecting the requests/responses used to load all the resources for a given web page.
  > **Example**: With these tools, you can View and modify HTML/CSS, Run your own JavaScript on a web page, and inspect network activity, such as requests/responses.
                    
- **Network Inspector**: tool used to further inspect requests and responses.
  > **Example**: tabs within the tool: elements, console, sources, network and security
                    
- **Time to First Byte (TTFB)**: how long it took to receive the response
  > **Example**: measures the length of time from the user or client making an HTTP request to the first byte of the page being received by the client's browser.
                      
- **Latency**: a time delay between the cause and the effect of some physical change in the system being observed
  > **Example**: running a ping command on a domain name will show the time (in milliseconds) it takes to complete a request/response.
                      

## Key Commands

### cURL

`cURL` is a tool to transfer data from or to a server, using one of the supported protocols without user interaction.

```bash
# Fetch HTML 
curl example.com
```
This fetches the HTML for a web page using a GET request

```bash
# Views the request/response text 
curl -v example.com
```
This views the request/response text by adding the "v" flag

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-v</code> verbose, shows more details output.
  </ul>
</details>

###

```bash
# View the response headers 
curl -I example.com
```
This views the response headers only, use the "I" flag

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-I</code> only see the response headers
  </ul>
</details>

###

```bash
# Setting a request type and URL 
curl --request GET --url example.com
```
This explicitly sets a request type and URL with the --request and --url options

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>--request</code> set the request type
    <li><code>--url</code> set the URL
  </ul>
</details>

###

```bash
# Viewing available options
curl --help
```
This views all available options for cURL command

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>--help</code> shows help file
  </ul>
</details>

###

```bash
# Send a GET request with parameters
curl --request https://postman-echo.com/get?name=<yourname>&location=<yourlocation>
```
This sends a GET request to the /get endpoint with the following parameters: name, location

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>--request</code> set the request type
    <li><code>name</code> your name
    <li><code>location</code> your current city
  </ul>
</details>

###

```bash
# Send a GET request with parameters and show both request and response headers
curl -v --request https://postman-echo.com/get?name=rodric&location=atlanta
```
This sends a GET request to the /get endpoint with the following parameters: name, location but also prints out both request and response headers

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-v</code> shows more detailed info like both request and response header
    <li><code>--request</code> set the request type
    <li><code>name</code> your name
    <li><code>location</code> your current city
  </ul>
</details>

###

```bash
# Send a POST request with parameters
curl -v --request POST --url https://postman-echo.com/post --data 'name=<yourname>&location=<yourlocation>'
```
This sends a POST request to the /post endpoint using the same data as query parameters before, but using cURL's --data option instead

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-v</code> shows more detailed info like both request and response header
    <li><code>--request</code> set the request type
    <li><code>--url</code> specific custom URL
    <li><code>--data</code> specify parameters
  </ul>
</details>
