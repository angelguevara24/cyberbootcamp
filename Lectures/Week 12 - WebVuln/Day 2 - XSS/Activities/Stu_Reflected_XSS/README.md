# Reflected XSS

### DVWA

Log into DVWA on your Ubuntu VM

- Select `XSS (Reflected)` tab in the side navigation menu. 

- In the form's name field, deliver a XSS attack that steals the `document.cookie` by submitting an input which contains JavaScript.
  - Deliver the same payload directly as a URL query parameter.

- After your payload fires, look at the page HTML via `view-source`. Search for the payload you sent with `Ctrl + F`.

- When you've gotten a payload to work, set your security level to **Medium**.

- Try to drop the same XSS payload you did before. It shouldn't work.
  - How do you think the XSS was prevented from firing?
  - Use `view-source` to inspect the HTML. What do you notice?

- Click **View Help** and highlight the solution to the **Medium** challenge. Use this hint to modify your previous payload and bypass the filter.

- Share your working payload in Slack.

### Gruyere
**Note**: Use Firefox/Foxy Proxy for this exercise.

- Launch a Gruyere instance by navigating to the following site: <https://google-gruyere.appspot.com/start>

- Navigate to: <https://google-gruyere.appspot.com/{YOUR_GRUYERE_ID}/nonexistent>
  - What appears on the page here?
  - Change `nonexistent` in the link to deliver the payload you used on DVWA.

- Launch Burp Suite, and ensure that Interceptor is on.

- Send the request to Repeater, and use it to deliver the same XSS payload.
