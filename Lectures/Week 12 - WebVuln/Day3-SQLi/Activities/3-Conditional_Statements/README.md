# Conditional Statements and Updates

## Instructions

Navigate to the SQL fiddle at: <https://www.db-fiddle.com/f/vEMPnPCQzQSraM4EBLMyDm/1>

### Updating Records
Update the name of the Heartbleed record to: `HEARTBLEED!`

Update the name of the Shellshock record to: `Bash Bug`

### Conditional Selections

Select the record whose `id` is 2 _or_ whose name is `Bash Bug`.

Select the record whose `name` is `Petya` _and_ whose `disclosure` is `2016-03-01`.

### Limits
**Note**: Consider this challenge a bonus. Refer to the documentation at: <https://www.w3schools.com/sql/sql_top.asp>

Select the record whose `id` is 2 _or_ whose name is `Bash Bug`, but retrieve only _one_ record. How does this compare to the results you get without `LIMIT`?
