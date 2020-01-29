## SQL Warm-Up

### Instructions
Please navigate to the fiddle at: <https://www.db-fiddle.com/f/upnxDj1JbZyQeG7BKNqAUL/0>

#### SELECT WHERE with Conditions
Load the fiddle at the above link. Then:
- Select all users whose last name is `Doe`
  - **Solution**: `SELECT * FROM site_data.users WHERE last='Doe';`

- Select all users whose last name is `Doe` _or_ `Competent`
  - **Solution**: `SELECT * FROM site_data.users WHERE last='Doe' OR last='Competent';`

- Select all users whose first name is `Jane` _and_ whose password is `asdf772nx`.
  - **Solution**: `SELECT * FROM site_data.users WHERE last='Jane' AND password='asdf772nx';`

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

**Solutions**

- The first query retrieves the record for `Jane Doe`. The `OR` clause just says: Do _not_ return a result of this condition is false. Since `'1'='1'` is always true, it doesn't change the result.

- The second query retrieves no record. This is what would happen if someone tried to log into Jane's account with the wrong password.

- The third query retrieves the record for Jane. This is the same as the first query, since the AND clause is commented out. This means it does nothing in this query.

You'll see why strange queries like this are useful when you study Login Bypasses.
