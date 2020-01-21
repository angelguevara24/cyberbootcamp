# Reflected XSS

### DVWA

- Deliver an XSS payload via the Name form.
  > **Solution**
  >  - Navigate to the path `/vulnerabilities/xss_r`.
  >  - In the form, submit: `<script>alert(document.cookie)</script>`

- Deliver the same payload directly through the query parameter.
  - After your payload fires, look at the page HTML via `view-source`. Search for the payload you sent with `Ctrl + F`.
  > **Solution**
  >  - Navigate to the path `/vulnerabilities/xss_r?name=<script>alert(document.cookie)</script>`.

- When you've gotten a payload to work, set your security level to **Medium**.

- Try to drop the same XSS payload you did before. It shouldn't work.
  - How do you think the XSS was prevented from firing?
  - Use `view-source` to inspect the HTML. What do you notice?
    > **Solution**: The payload was prevented from firing because the developer filtered out the `script` keyword. Thus, your HTML tag was dumped as `&lt;script&gt;`, which the browser does _not_ interpret as HTML!

- Click **View Help** and highlight the solution to the **Medium** challenge. Use this hint to modify your previous payload and bypass the filter.
  > **Solution**: Mix the case in your `script` tag: `<sCrIpt>alert(document.cookie)</SCript>`

### Gruyere
**Note**: Use Firefox/Foxy Proxy for this exercise.

- Launch a Gruyere instance by navigating to the following site: <https://google-gruyere.appspot.com/start>

- Navigate to: <https://google-gruyere.appspot.com/{YOUR_GRUYERE_ID}/nonexistent>
  - What appears on the page here?
  - Change `nonexistent` in the link to deliver the payload you used on DVWA.
    > **Solution**: The word `nonexistent` appears on the page. You can fire the payload with: `https://google-gruyere.appspot.com/{YOUR_GRUYERE_ID}/<script>alert(document.cookie)</script>`

- Launch Burp Suite, and ensure that Interceptor is on.

- Send the request to Repeater, and use it to deliver the same XSS payload.

> **Solution**: 
> - Add `/<script>alert(document.cookie)</script>` to your request line. Your new line should look like this:
>   - `GET {YOUR_GRUYERE_ID}/nonexistent/<script>alert(document.cookie)</script> HTTP/1.1`
> - Click on the HTML tab, right-click and scroll down to "Show response in browser". 
> - Copy the URL and turn Intercept off. 
> - Open your webbrowser and paste the URL in the search bar to see the cookie.
