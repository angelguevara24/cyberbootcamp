## User Creation 

Building on the previous Validate Password activity, in this activity you will now create a command-line application which allows users to create new usernames, passwords, and email addresses for a fake account.  Users will only be able to create accounts if their password meets the password length. It should also print out the account information to the terminal. 


### Instructions

* Use the script file provided. We've added a lot of the code to get you started.

* Your application should have the following features.
  
    * A function called `collect_user_information` that will prompt the user for their username, password, and email address. It should return this information in a list that contains those three values.

    * The above returned list should be passed into a function called `create_user` that checks if the password entered is valid.
                
    * If the password is valid, it will create a new dictionary for the user with their information. The dictionary should have keys for username, password, and email with the associated values that the user entered. It should then print a message to the screen with this information.
          
    * If the password is not valid, it will print a message to the screen letting the user know that their password isn’t valid.
