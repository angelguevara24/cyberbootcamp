### 1.  Guided Practice: Leaky HTTP Traffic (0:08)

---

**Instructions** 

  * In this partner activity, you’ll use Wireshark to retrieve a user’s username and password being communicated through an insecure website

  * Initiate a Wireshark capture.

  * Open a Chrome window using incognito mode (`Ctrl+Shift+N` or `Cmd+Shift+N`).

  * Navigate to the webpage http://zero.webappsecurity.com/. Attempt to login using a dummy username and password. 

  * Return to your Wireshark window and stop the capture. 

  * See if you can identify the packet relevant to your form submission. (Hint: Google GET and POST requests.)

  * Once you identify the relevant row, see if you can extract from the packet data the username and password you entered. 

  * Turn to the internet to find out how this plaintext password communication can be avoided (hint: HTTPs)
