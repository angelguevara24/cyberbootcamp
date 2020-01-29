## Login Bypasses

### Instructions

### Classic Login Bypasses

Navigate to: DVWA and click on the **Brute Force** tab. 
- Try to log in as `admin` with an arbitrary password.

Try to log in as:
  - `admin"`.
  - `admin'`.
  - Based on the error output, which type of quote do you think the SQL statement uses?

  **Solution**: The error output suggests that the server is using a single quote

- Add an `or` statement to your injection. 
  - If the server uses double quotes, your query should now look like: `admin" or <Condition>`, where `<Condition>` is your always-true condition, such as `'2'='2'`.

   **Solution**: Try: `admin' or '1'='1` 
---

For this next part please close the DVWA window/tab and instead, take a closer look at common SQL statements. 

Suppose the SQL statement on the server looks like the below, where the username you submit to the form gets substituted in `$USERNAME`.

  ```sql
  SELECT * FROM users WHERE username='$USERNAME' and password='$PASSWORD'
  ```

What does the statement look like if you substitute your payload for `$USERNAME`?
  - **Solution**: It looks like: `SELECT * FROM users WHERE username='admin' or '1'='1'' and password='$PASSWORD'`

You might notice an extra quote. How could you modify your payload to remove it?
  - **Solution**: Update the payload to `admin' or '1'='1'`!

  ```sql
  SELECT * FROM users WHERE username=admin' or '1'='1' and password='$PASSWORD'
  ```



