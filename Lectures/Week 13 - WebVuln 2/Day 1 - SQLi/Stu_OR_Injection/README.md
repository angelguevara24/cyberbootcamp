## OR Injection

### Instructions

DVWA uses the ID value you submit to complete the following query:

  ```sql
  SELECT first_name, last_name FROM users WHERE user_id = '$id';
  ```

So, if you submit an ID of 1, it runs the query:

  ```sql
  SELECT first_name, last_name FROM users WHERE user_id = '1';
  ```

Keep this in mind as you work through the instructions below.


Login to your Virtual Machine and start the DVWA database using the command `dvwa_start`. 

Modify the SQL payload above so that it results in the query below:

  ```sql
  SELECT first_name, last_name FROM users WHERE user_id = '' OR '1'='1';
  ```

Use the `DVWA:SQL Injection` web form to submit your portion of the payload. 
  
- How many users are in the database?

Next, submit your payload directly through the URL.
  - **Hint**: Your URL looks something like: `http://localhost/vulnerabilities/sqli?id=1` (on a Mac). Replace the `1` at the end with your payload.
  - If you need to write a space, use `+` or `%20`. E.g., to submit `super fake data`, you'd do: `http://localhost/vulnerabilities/sqli?id=super+fake+data`, or `http://localhost/vulnerabilities/sqli?id=super%20fake%20data`.

Finally, launch Burp Suite and:
  - Intercept a request to the SQL injection page on DVWA.
  - Send the request to Repeater with `Ctrl + R`.
  - Replace the value of the `id` parameter in the intercepted request with your payload. Remember to use `+` or `%20` to encode spaces.
  - Press **Go**, and inspect the response. You should get the same result you got with the previous two methods.
