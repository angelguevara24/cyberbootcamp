## SQL Warm-Up

### Instructions

Load the fiddle at: <https://www.db-fiddle.com/f/upnxDj1JbZyQeG7BKNqAUL/0>

#### SELECT WHERE with Conditions
- Select all users whose last name is `Doe`.
- Select all users whose last name is `Doe` _or_ `Competent`.
- Select all users whose first name is `Jane` _and_ whose password is `asdf772nx`.

#### Questions

The Queries below seem strange, but you'll use them in your SQL injections. For now, just try to understand why they produce the results they do, not why you'd write queries like this.

  ```sql
  -- This is Query #4. What is the result? What does the OR clause do?
  SELECT * FROM site_data.users WHERE first='Jane' OR '1'='1';

  -- TODO: This is Query #5. What is the result? What does the AND clause do?
  SELECT * FROM site_data.users WHERE first='Jane' AND password='uwasf';
  
  -- TODO: This is Query #6. What is the result? What does the AND clause do?
  SELECT * FROM site_data.users WHERE first='Jane' OR '1'='1' -- AND password='uwasf';
  ```
