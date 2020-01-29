## Login Bypasses

### Introduction

#### Classic Login Bypasses

Navigate to: DVWA and click on the **Brute Force** tab. 
- Try to log in as `admin` with an arbitrary password.

Try to log in as:
  - `admin"`.
  - `admin'`.
  - Based on the error output, which type of quote do you think the SQL statement uses?

Add an `or` statement to your injection. 
  - If the server uses double quotes, your query should now look like: `admin" or <Condition>`, where `<Condition>` is your always-true condition, such as `'2'='2'`.

Suppose the SQL statement on the server looks like the below, where the username you submit to the form gets substituted in `$USERNAME`.
  
  - What does the statement look like if you substitute your payload for `$USERNAME`?
  
  - You might notice an extra quote. How could you modify your payload to remove it?

  ```sql
  SELECT * FROM users WHERE username='$USERNAME' and password='$PASSWORD'
  ```

