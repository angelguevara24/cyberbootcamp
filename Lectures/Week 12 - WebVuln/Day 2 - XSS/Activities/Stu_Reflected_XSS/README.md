# Reflected XSS

### XSS Game
Navigate to XSS Game at: <https://xss-game.appspot.com/level1>

- In the search bar, type: `hello`, then press **Search**.

Take note of where the search term appears:
  - On the error page
  - In the URL query parameters

 This reflection of user input into the page is a major vulnerability.

The first step in searching for reflected XSS is to test if you can insert HTML, instead of normal text.

Click **Try Again** to return to the vulnerable application's home page, then submit: `<h1>haxxed</h1>`

- Note that this inserts the word `haxxed` as an HTML heading—_not_ "normal text"!

This tips us off to the possibility of injecting a script tag. Enter: `<script>alert('you got hacked!')</script>`

This vulnerability _reflects_ the user's input to the page. 

- Note that the URL reads: 

     `https://xss-game.appspot.com/level1/frame?query=<script>alert('you got hacked!')</script>`
  
- Identify the query string: 

     `?query=<script>alert('you got hacked!')</script>`

You can test for XSS by directly manipulating this string. 

- Change the URL to the following, then refresh the page: 

    `https://xss-game.appspot.com/level1/frame?query=<script>alert('this is a new alert!')</script>`

### Gruyere
**Note**: Use Firefox/Foxy Proxy for this exercise.

- Launch a Gruyere instance by navigating to the following site: <https://google-gruyere.appspot.com/start>

- Navigate to: <https://google-gruyere.appspot.com/{YOUR_GRUYERE_ID}/nonexistent>
  - What appears on the page here?
  - Change `nonexistent` in the link to deliver the payload you used on on the PortSwigger site.

- Launch Burp Suite, and ensure that Interceptor is on.

- Send the request to Repeater, and use it to deliver the same XSS payload.

### Port Swigger Academy

Navigate to https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded and complete the lab **Reflected XSS into HTML content with nothing encoded.


