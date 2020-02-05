## Solved

Remember, there are  different ways to accomplish each of these tasks. 

- - -
Create a user account on the Juice Shop website before starting the test. 

<details><summary>Locate the Score board</summary>
<p> 

**Hint:** What happens if you try directory traversal in the URL?
- **Solution:** type <ipaddress>/#/score-board
![Images/dom](Images/score.png)

</p> 
</details>

<details><summary>Locate the Admin Section</summary>
<p> 

**Hint:** What happens if you try directory traversal in the URL?
- **Solution:** type `<ipaddress>/#/administration`. 

![Images/administration.png](Images/administration.png)

</p> 
</details>


<details><summary>Confidential Document</summary>

<p> 

**Hint:** Do you find anything interesting when you spider the website?
- **Solution:** BurpSuite shows there are several FTP documents you access.  Navigate to `<ipaddress>/ftp/acquisitions.md`.
![Images/document](Images/document.png)
</p> 
</details>


<details><summary>Error Handling</summary>
<p> 

**Hint:** Any request that cannot be processed by the server will be flagged as a global error. 
- **Solution:** Navigating to `<ipaddress>/#/administration` without admin privileges raises the error. 

</p> 
</details>


<details><summary>XSS Tier 0</summary>

<p> 

**Hint:** Review this link here https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)
- **Solution** Search for an item. Click on the item, in the search bar uptop you will see `search=apple`. Replace your item with the code `<iframe src="javascript:alert('xss')">`. 
![Images/reflected](Images/reflected.png)

</p> 
</details>

<details><summary>XSS Tier 1</summary>

<p> 

**Hint:** Review this link here https://www.owasp.org/index.php/DOM_Based_XSS
- **Solution:** In the search bar type `<iframe src="javascript:alert('xss')">`. 
![Images/dom](Images/dom.png)
</p> 
</details>

<details><summary>Zero Stars</summary>

<p> 

**Hint:** Can you use BurpSuite to _forward_ the request?
- **Solution:** Capture the request using BurpSuite, change your rating to 0, then click **Forward**. 
![Images/zero](Images/zero.png)
</p> 
</details>
