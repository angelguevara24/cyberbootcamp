# Reading SQL

In this exercise, you'll read SQL that
- Creates databaess and tables
- Adds data to the tables
- Retrieves all records in the database

## Questions

Refer to the SQL fiddle at the following link: <https://www.db-fiddle.com/f/n9oBdA64n45LX6qQjCibBA/0>

Use the code therein to answer the questions below.

---

Based on the code in the left pane, how would you write SQL to...
- Create a database named `exploits`?
  > **Solution**: `CREATE DATABASE exploits;`
- Create a table named `hackers`, with `id` and `nickname` columns?

   >**Solution**
   > ```sql
   > CREATE TABLE hackers (
   >   id int,
   >   nickname varchar(255)
   > );
   > ```

- Add the the following to the `hackers` table:
  - 1, 'hackerken'
  - 2, 'janepety4'

   >**Solution**
   > ```sql
   > INSERT INTO hackers 
   > VALUES (1, 'hackerken'),
   >        (2, 'janepetya')
   > ```

As a bonus: How do you suppose you could modify the SELECT query in the right pane to extract _only_ the name of each vulnerability? What about just name and disclosure date?

  > **Solution**: SELECT name FROM vulnerabilities;
  