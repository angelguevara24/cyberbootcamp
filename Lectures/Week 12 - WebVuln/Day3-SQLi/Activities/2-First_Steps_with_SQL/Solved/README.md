# First Steps with SQL

## Instructions
Navigate to the SQL fiddle at: <https://www.db-fiddle.com/f/n9oBdA64n45LX6qQjCibBA/1>

### Making Selections
Begin by selecting all data from the `vulnerabilities` table. 

Then, retrieve only the `name` and `disclosure` columns.

Record your each of your SQL queries below.
- **All-Data Query**: `SELECT * FROM vulnerabilities;`
- **Name and Disclosure Query**: `SELECT name, disclosure FROM vulnerabilities;`
- **Heartbleed Query**: `SELECT * FROM vulnerabilities WHERE id=1`

### Inserting Data
Insert the following data into the `vulnerabilities` table.
- (3, 'Shellshock', '2014-09-24')
- (4, 'Stagefright', '2015-08-05')

> **Solution**
> ```sql
> INSERT INTO vulnerabilities
> VALUES (3, 'Shellshock', '2014-09-24'),
>        (4, 'Stagefright', '2015-08-05');
> ```

### Deleting Records
Delete the Petya record.

> **Solution**
> ```sql
> DELETE FROM vulnerabilities WHERE id=2;
> ```

### More Selections
Use a WHERE clause to select the Heartbleed record.
- Double-check that the record you retrieve has the updated name!

> **Solution**
> ```sql
> SELECT * FROM vulnerabilities WHERE id=1;
> ```

Use a WHERE clause to select the Petya record. 
- This should produce an error, since you deleted this record.

> **Solution**
> ```sql
> SELECT FROM vulnerabilities WHERE id=2;
> ```
