# SQL Injection Warm-Up

## Instructions
- Consider the following URL: `https://vulnerable.site?id=1`. How would you test this URL for a SQL injection vulnerability?
  > **Solution**
  >  - Start by injecting quotation marks (`'` and `"`). If these produce errors, the server may be vulnerable to injection.
  >  - If you suspect there's a vulnerability, you should try an OR and AND injection.

- Consider the following URLs: 
  - `https://vulnerable.site?id=1%20AND%201=1`.
  - `https://vulnerable.site?id=1%20AND%201=2`.
  - If the first URL works and the second causes an error, what can you conclude?
  > **Solution**
  >   - If the first URL works and the second causes an error, we can conclude that the database ran the full SQL statement in the URL. 
  >   - If the AND comparison is true, it will work as normal. If it is false, it will cause an error. Only servers that are vulnerable to injection will work this way.

- Fill out the query below to select `login` and `password` information from `users`.

  ```sql
  SELECT name, age FROM users
  UNION
  SELECT login, password FROM users
  ```
