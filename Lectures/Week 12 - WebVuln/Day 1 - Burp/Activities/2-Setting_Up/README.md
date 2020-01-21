# Setting Up

In this exercise, you will set up DVWA for the day's exercises. Then, you'll verify that your Foxy Proxy and Burp Suite installations behave as expected.

## Instructions

### If you don't have FoxyProxy

- From Kali, open up Firefox. Click on **Settings** and then **Add-Ons**

- Type **FoxyProxy** in the search bar.

- Click on the option for **FoxyProxy Basic**
  ![](images/1.png)

- Once the page loads, click on **Add to Firefox** and then **Add** again when prompted.
  ![](images/2.png)

- Once it's added, you should see a new icon on your browser window. 
  ![](images/3.png)

### Configuring Burp Suite
- Launch Burp Suite, ignore the upgrade for now if asked (you can do it later if you want) but click **OK** when prompted for "not tested" box.

- Go ahead and create a **Temporary project** when asked and then use the further default settings.

- Switch back to your Firefox browser. 
- Configure the proxy:
  - Click on the `FoxyProxy` icon on the toolbar and then `Options`
  - Click `Add` and fill in the following:
    - **Title or Description** = BurpSuite
    - **IP address, DNS name, server name** = 127.0.0.1
    - **Port** = 8080
  - Click `Save`
  ![](images/4.png)

  - Click on `FoxyProxy` then `Use proxy BurpSuite for all URLs (ignore patterns)`
  ![](images/5.png)

  - Leave Burp open, and navigate to `http://burp`

  - Click on the **CA Certificate** button in the top right corner of the webpage. Save the file when prompted.

  - When it's done saving, click on the **Settings** option in Firefox, and then go to **Preferences**. 

  - If you have a search bar, search for **Certificates** and then **View Certificates**. 

  - Click the **Import** button at the bottom, then navigate to your Downloads folder and select the **cacert.der**. Click **Open**. 

  - Click the first box **Trust this CA to identify websites** and then click **Ok**, and then **Ok** again.

  - Verify you can get to Google without any problem. 

- Navigate to **DVWA Security**. Verify that Burp Suite intercepts your request (you don't have to do anything with it yet—just make sure the interceptor is working).