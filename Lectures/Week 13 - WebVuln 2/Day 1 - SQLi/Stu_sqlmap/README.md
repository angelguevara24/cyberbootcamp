## Dumping Databases with sqlmap


### Enviroment

In this lab you will be using DVWA that has been installed onto your Linux enviroment. You can turn on DVWA by typing: `dvwa_start` into your terminal.

**Note:** You will need your session ID from DVWA in order to complete this lab. Because this lab is not testing you on SQL injections, the following instructions have been given to you:
- Navigate to `XSS stored` in DVWA. 
- Inside the **Name** field put your name, and inside the **Message** field type: `<script>alert(document.cookie)</script>` then click on **Sign Guestbook**. 
- Make sure to have your ad blocker turned off.


### Instructions


Browse the site, and look at the URL bar. Find the page that accepts a GET query parameter.
  - Record this URL when you find it.

Use SQLMap to test the URL for a SQL injection vulnerability.
- Because we are attacking a page that requires a username and password, SQLmap will not work. But because we already have inside website we can insert our cookie information for SQLmap to be able to log in. 

Use: `sqlmap -u "http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=your session ID; security=low"`

- `-u` Target URL
- `--cookie` Your cookie information 


Next, use a UNION-based injection to perform the following tasks, and 
  - Grab the database banner
  - List all available databases
  - List the tables of the `dvwa` database
  - List the columns of the `users` table
  - Dump the `login` and `password` columns of the `users` table

Record the results of your information gathering below.
  - **Banner**: _____
  - **User(s)**: _____
  - **Databases**: _____
  - **Tables in `dvwa`**: _____
  - **Columns in `users`**: _____

How many users are registered on this site? What are their username/passwords hashes?

What is one of the passwords that you dumped?
  - **Hint**: Google is your friend! Alternatively, SQLMap can crack it for you...
