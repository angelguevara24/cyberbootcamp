# SQL Injection Warm-Up

## Instructions
- Consider the following URL: `https://vulnerable.site?id=1`. How would you test this URL for a SQL injection vulnerability?

- Consider the following URLs: 
  - `https://vulnerable.site?id=1%20AND%201=1`.
  - `https://vulnerable.site?id=1%20AND%201=2`.
  - If the first URL works and the second causes an error, what can you conclude?

- Fill out the query below to select `login` and `password` information from `users`.

  ```sql
  SELECT name, age FROM users
  UNION
  -- Your SQL here
  ```

