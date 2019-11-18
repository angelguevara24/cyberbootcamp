# Hybrid Cryptosystems

In this activity, you'll use a hybrid cryptosystem to exchange encrypted messages with your partner. You will need to work in pairs to complete the activity, please contact your instructors if you cannot find a partner.

To achieve this, you will:
- Use OpenSSL to generate an RSA keypair. This takes care of the **asymmetric** half of the hybrid system.
- Send your public key to your partner.
- Create a symmetric key so you can encrypt messages with AES.
- Use the symmetric key to encrypt a message.
- Use your asymmetric, _private_ key to encrypt your symmetric key.
- Send _both_ the encrypted message _and_ the encrypted symmetric key to your partner.

On the other side, your partner will:
- Use your public key to decrypt the symmetric key
- Use the symmetric key to decrypt the message

This seems like a lot of steps, but we'll walk you through it.

Not many people understand hybrid encryption schemes like this, and even fewer have actually gone through the motions of using one. Consider this a major milestone in your cybersecurity career!

## Instructions

To complete the homework, you'll need to take a screenshot of each step and submit a PDF file containing all of the screenshots. There are reminders for each step but be sure to stop and take a screenshot before moving on to each next section! 

### Make a Confession

- To get started, create a new directory, called `~/Documents/HybridCryptosystems`, and change into it.

- Create a new file in this directory, and call it `dirty_little_secret`. Use it to save a (dirty, little) secret message.

- Take a screenshot.

### Generate an RSA Keypair

Next, you'll generate an RSA keypair through the following steps.

- Create a 2048 bit RSA private/public keypair with:

    - `openssl genrsa -des3 -out private.pem 2048`

- Extract the public key from this keypair with:

  - `openssl rsa -in private.pem -outform PEM -pubout -out public.pem`

- Take a screenshot of your terminal with the commands from above.

### Trade Public Keys

- Next, send your partner your public key via Slack.

  - **Make absolutely sure you're _not_ sending your private key.** Run: `cat public.pem`, and ensure the file says `BEGIN PUBLIC KEY` at the top, and `END PUBLIC KEY` at the bottom.

  - **Be sure to rename your partner's public key to**: `partners_public.pem`. If you don't do this before you move it into your activity folder, you'll overwrite your own!

  - _After_ you've renamed your partner's key, move it into ~/Documents/HybridCryptosystems.

- Take a screenshot of your partner's key in ~/Documents/HybridCryptosystems.

### Generate an AES Key

In this section, you'll use OpenSSL to generate a symmetric key, which you'll use to encrypt your message.

You'll also generate something called an **Initialization Vector**, or IV. This is simply a special, random number that AES needs to get started encrypting your data securely.

- To generate a symmetric key and IV, run the following.

  - `openssl enc -aes-256-cbc -nosalt -k password -P | tee secrets`

  - Take a screenshot of your terminal after running the above command.

- Open up the file `secrets`. You'll see two lines. The first has your `key`, and the second, your `iv`.

  - Create a file called `symmetrickey.dat`. Copy and paste your key from `secrets` into `symmetrickey.dat`. Make sure you _do not_ copy the `key=`: _Only_ copy the string to the right of the equals sign.

  - Create a file called `iv.dat`. Copy and paste the IV from `secrets` into `iv.dat`. As before, _only_ copy the string to the right of the equals sign.

- Take a screenshot of your `symmetrickey.dat` and `iv.dat` files either in your terminal or file finder.

### Encrypt Your Message

Now that you have a symmetric key, you can use it to encrypt messages!

- To encrypt your message, run:

  - `openssl enc -nosalt -aes-256-cbc -in dirty_little_secret.txt -out dirty_little_secret.enc -base64 -K <key> -iv <IV>`

  - In place of `<key>` and `<IV>`, copy and paste the key from your `symmetrickey.dat` and `iv.dat` files, respectively.

  - The `-base64` option simply ensures you can open your encrypted file in a text editor and see letters, instead of wingding gibberish.

- This creates an encrypted version of your message in the file `dirty_little_secret.enc`.

- Check to make sure everything went well by running: `cat dirty_little_secret.enc`.

- Take a screenshot of your terminal, including both commands in this section.


### Encrypt Your Symmetric Key

Next, you'll use your partner's public key to encrypt your symmetric key. 

This way, your partner can use their _private_ key to decrypt the symmetric key, which they can then use to decrypt your message.

- To encrypt your symmetric key, run:

  - `openssl pkeyutl -encrypt -in symmetrickey.dat -inkey partners_public.pem -pubin -out symmetrickey.enc`

- You might be wondering if you have to encode the IV. The answer is—**no**!

- Take a screenshot of your terminal.

### Trade Files

- Now, you can send `symmetrickey.dat.enc`, `iv.dat`, and `dirty_little_secret.enc` to your partner.

- When you get your partner's files, **rename them to**: `partners_dirty_little_secret.enc`, `partners_symmetric_key.enc`, and `partners_iv.dat`.

- Take a screenshot of your partner's files in your terminal or file finder.

### Decrypt!

- Finally, move into `~/Documents/HybridCryptosytems`.

- Remember, the steps to decrypt the data are:

  - Use your partner's public key to decrypt `partners_symmetric_key.enc`.

  - Use the decrypted symmetric key to decrypt `partners_dirty_little_secret.enc`.

- To decrypt the symmetric key, run the following commands.

  - `openssl pkeyutl -decrypt -in partners_symmetric_key.enc -inkey private.pem -out partners_symmetric_key.pem`

- Now you have your partner's symmetric key, ready to go!

- To use the symmetric key to decrypt their secret message, run:

  - `openssl enc -aes-256-cbc -d -nosalt -in partners_dirty_little_secret.enc -base64 -K <partner's symmetric key> -iv <partner's IV>`

  - As with encryption, copy and paste your partner's symmetric key where the `<partner's symmetric key>` placeholder is, and your partner's IV where `<partner's IV>` appears.

- If all went well, you should now be able to read your partner's dirty little secret!

- Take a screenshot of your terminal with the commands from this section and take a screenshot of your partner's decrypted file.

### Submit

- Create a PDF with all of the screenshots you took of each submit. 

- Submit the PDF file to BCS.

### PAIN

Remember...**Cryptography is all about PAIN**.

This seems like an involved process—and it is—but _exactly_ these steps are happening all around you, _all_ the time. 

As you've now learned, there's a lot of room for error in processes like this. But, exactly this process is the whole reason we can browse the web securely, so it's important we get it right.

If you were still wondering why we recommend you never roll your own crypto...Well. **Now you know!**

