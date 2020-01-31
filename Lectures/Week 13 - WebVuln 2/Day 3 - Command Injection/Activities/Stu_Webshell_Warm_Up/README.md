# Webshell Warm-Up
In this exercise, you'll review fundamental concepts around webshells.

## Constructing Commands
Suppose the following PHP webshell lives at `https://vulnerable.site/shell.php`.

  ```php
  <?php
    echo system($_GET["command"]);
  ?>
  ```

How would you construct a URL to:
- Dump `/etc/passwd`?
- Determine if `ncat` is installed?
- List all files in the current directorty?

## Bypassing Filters
Suppose the web application you're assessing has a photo upload feature.
- State one technique for preventing users from uploading webshells.
- Is there any way to bypass your suggested fix? Why or why not?

## Thinking Critically
- Can you use a webshell to run commands with `sudo`? Why or why not?
- Can you use a webshell to add or modify a user, or change group membership? Why or why not?
- Can you use a webshell to open an interactive shell to an attacking machine? Why or why not?
