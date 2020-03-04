## Studying Shellshock

In this activity, you will learn how to:

- Identify if a server is vulnerable to Shellshock.
- Write custom Shellshock payloads.
- Articulate which HTTP headers can serve as command injection points. 

### Instructions
- Find a tool that determines if a server is vulnerable to Shellshock.

   **Hint**: Research Nmap scripts: <https://nmap.org/nsedoc/>. 
   
- Write Shellshock payloads that:

    - Read `/etc/passwd`.
    
    - Use `curl` to download a malicious file from `http://evil.site/mal.php`.
    
    - Open an Ncat connection to your port 4444.
    
    - Send a reverse shell to your port 4444.

- Refer to the following Wikipedia article on CGI. Scroll down to **Request specific variables**:  <https://en.wikipedia.org/wiki/Common_Gateway_Interface#Example>

    - The examples demonstrated command injection via the `User-Agent` header. Which other headers are vulnerable?
