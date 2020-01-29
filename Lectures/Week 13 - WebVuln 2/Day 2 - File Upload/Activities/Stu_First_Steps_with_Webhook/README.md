# First Steps with Webhook

In this activity, you will exploit an RFI vulnerability using webhooks and BurpSuite.
You will need to open two web browsers for this activity. In one of them, navigate to `http://dvwa.com`. in the other, navigate to your personal Webhook URL.
You will also create a malicious file that you will upload to DVWA.

Use Firefox to navigate to: <https://webhook.site>.

This will give you a unique URL. You will need this later on when you make your file. 

Enable Foxy Proxy, and intercept a request (click **Open In New Tab**) to your unique Webhook URL. Send this request to the Burp Repeater. 
  - Be sure to disable the interceptor after you capture the request.

Then, follow the instructions below.

## Instructions

- Send the intercepted request to Repeater, and press **Go**. Compare the request in Repeater to the Webhook log (which is on the webhook page in Firefox) to familiarize yourself with reading captured requests.

- In Repeater, go to the headers tab and add the following Header: `Cookie: PHPSESSID=FakeSessionID`. Then, press **Go**. Go back to your open webhooks page, and find the cookie that you just passed.

- Create a file called `webhook.php`, Add an image tag like the one below.

  ```html
  <img src="<Your Webhook URL>?example=parameter" >
  ```
  - Replace the word `parameter` with your name. 

- Upload your file with the RFI vulnerability at `localhost/hackable/uploads/`. 

- Browse over to the PHP file by going to `localhost/hackable/uploads/` and then click on your `webhook.php` file. This will launch your PHP script!

- Return to your Webhook log, and find the most recent request. Identify the query parameter that was sent. (It should show `Query strings` then the info directly below that.)
