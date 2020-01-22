## Web Vuln Homework  

Your homework this week will involve exploiting Juice Shop, with a focus on XSS and SQL injection.

Once you have found the Score Board, complete as many of the XSS challenges as you can within Juice Shop. 

![](images/1.PNG)

As you work on this exercise, feel free to utalize any resources available to you (including your classmates and instructional staff).

The activities are ranked in hardness from 1 to 6, and as you explore these vulnerabilities you can select the difficulty of the challenges you want to see by clicking on the stars themselves. 

## 1 Star Activities

Confidential Document 
 - 


 ## SQL Injection
 
 ### One Star Challenges
 * Provoke an error that is not very gracefully handled
 
 ### Two Star Challenges
 * Log in with the administrator's user account
    <details>
       <summary>Hint</summary>
        If you can't find it, the e-mail is admin@juice-sh.op
     </details>
 
 ### Three Star Challenges
 * Log in with Bender's user account
    <details>
       <summary>Hint</summary>
        You need to log on as an administrator first. 
     </details>
 * Log in with Jim's user account. 
    <details>
       <summary>Hint</summary>
        There are two ways to do this. The more fun way involves dumping all the user credentials via SQL injection. A walkthrough for that is in hints/sqlinjection.md if you need an assist. 
        
     </details>

 ## XSS Attacks
 * Perform a reflected XSS attack
     <details>
       <summary>Hint</summary>
        Done from the track orders page
     </details>
 *  Perform a DOM XSS attack
 * Perform an XSS attack with ```<script>alert(`xss`)</script>``` on a legacy page within the application.

    <details>
       <summary>Hint</summary>
        When logged in as any user, done from the user's profile page. 
     </details>


