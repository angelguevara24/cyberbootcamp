# Conditional Statements and Updates

## Instructions

Navigate to the SQL fiddle at: <https://www.db-fiddle.com/f/vEMPnPCQzQSraM4EBLMyDm/1>

### Updating Records
Update the name of the Heartbleed record to: `HEARTBLEED!`

Update the name of the Shellshock record to: `Bash Bug`

  > **Solution**
  > ```sql
  > UPDATE vulnerabilities SET name='HEARTBLEED!' WHERE id=1;
  > UPDATE vulnerabilities SET name='Bash Bug' WHERE id=3;
  > ```


### Conditional Selections

Select the `name` and `disclosure` of the record(s) whose `id` is 2 _or_ whose name is `Bash Bug`.

Select the record whose `name` is `Petya` _and_ whose `disclosure` is `2016-03-01`.

  > **Solution**
  > ```sql
  > SELECT name, disclosure FROM vulnerabilities WHERE id=2 OR name='Bash Bug';
  > SELECT name, disclosure FROM vulnerabilities WHERE name='Petya' AND disclosure='2016-03-01';
  > ```

### Limits
**Note**: Consider this challenge a bonus. Refer to the documentation at: <https://www.w3schools.com/sql/sql_top.asp>

Select the record whose `id` is 2 _or_ whose name is `Bash Bug`, but retrieve only _one_ record. How does this compare to the results you get without `LIMIT`?
  > **Solution**
  > ```sql
  > SELECT name, disclosure FROM vulnerabilities WHERE id=2 OR name='Bash Bug' LIMIT 1;
  > SELECT name, disclosure FROM vulnerabilities WHERE name='Petya' AND disclosure='2016-03-01';
  > ```
  >
  > The results of this query are different because there is only _one_ result, instead of two, as produced by the original SQL.
