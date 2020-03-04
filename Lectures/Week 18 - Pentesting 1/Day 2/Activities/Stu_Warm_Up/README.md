## Student Activity: Nmap Warm-Up

In this activity, you'll use the Nmap documentation to learn useful new flags. 

- Refer to the following documentation as you work through the following questions: <https://nmap.org/book/man-port-scanning-techniques.html>

- For this activity, you will need to use your locally hosted VM. 

**Instructions:**
 
Complete the following and save it in a text document for notes:

- Write an Nmap command to perform a ping sweep of the range `10.0.0.0` to `10.0.0.254`.
    
    **Hint**: Use `-sP`.

- Write an Nmap command to perform a service/version scan of the live hosts you discover. Save the results as XML to `/tmp/results.txt`.

    **Hint**: Use `--help`.

Complete the following on your locally hosted VM:

- Read about the `--top-ports` feature: <https://danielmiessler.com/blog/nmap-use-the-top-ports-option-for-both-tcp-and-udp-simultaneously/>.

- On your locally hosted VM, write an nmap command using the top `--top-ports` argument to scan the top 20 ports of `scanme.nmap.org`. Save the results as a "normal" file.

- Use `--top-ports` to scan the top 100 ports of the live hosts you discovered above. Save the results to an XML file.
  
