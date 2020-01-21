# Attribute Injection

- In this next activity you will using persistent XSS to deliver a malicious JavaScript payload, via attributes, to break HTML qoutes.  

### Gruyere

- Open your Gruyere instance by opening: https://google-gruyere.appspot.com/start

- Click **Home**. Then, click **New Snippet**. Add one such as "Hello world" and save.

- Click **Home**. Find your snippet. Note the font color.

- Click on **Profile**. Change the Color to "red". Return **Home**, and note how the font color changes.

- Right-click your name, then select **Inspect Element**.

- Where did the color you entered on your profile get echoed onto the page?

- Inject a quote through the **Color** option in your profile. Use this to get an `onmouseover="alert(1)"` attribute into the page.
  - **Hint**: You'll have to save this payload through the Color field on your Profile. Use the right quote type.

