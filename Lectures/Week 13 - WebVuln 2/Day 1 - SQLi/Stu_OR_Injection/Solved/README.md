## OR Injection

### Instructions

DVWA uses the ID value you submit to complete the following query:

  ```sql
  SELECT first_name, last_name FROM users WHERE user_id = '$id';
  ```

So, if you submit an ID of `1`, it runs the query:

  ```sql
  SELECT first_name, last_name FROM users WHERE user_id = '1';
  ```

Keep this in mind as you work through the instructions below.

---

Login to your Virtual Machine and start the DVWA database using the command `dvwa_start`. 

Modify the SQL payload above so that it results in the query below:
  
  - **Solution**: `1' OR '1'='1`. Note that there is **no beginning or final quotation mark.**

  ```sql
  SELECT first_name, last_name FROM users WHERE user_id = 1' OR '1'='1;
  ```

Use the `DVWA:SQL Injection` web form to submit your portion of the payload. How many users are in the database?
  
  - **Solution**: `1' OR '1'='1; There are five users.`

Finally, launch Burp Suite, and:
  - Navigate to the SQL injection page on DVWA.
  - Intercept a request to this page.
  - Send the request to Repeater.
  - Replace the value of the `id` parameter in the intercepted request with your payload.
  - Press **Go**, and inspect the response. You should get the same result you got with the previous two methods.
