## Student Activity: Decoding Hex Data in Tracy's iPhone

### Instructions 

Welcome to the exercise.  In this Guided Practice, you will practice decoding using hex code strings.

#### Part 1

Using pen, paper and the [standard ASCII table](http://www.asciitable.com) decode the following Hex strings to ASCII.

1. `48 65 6c 6c 6f 20 57 6f 72 6c 64`

2. `54 65 73 74 69 6e 67 20 31 32 33 21`

3. `41 6e 64 72 65 77`

4. `31 20 32 20 33 20 34 20 35 20 36`


Check your answers using the [Hex-to-Ascii Converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html)


#### Part 2

Next, we'll look at a Hex dump from Tracy's iPhone

1. Locate and export Tracey's browsing history from her phone, located in the `vol_vol5/mobile/Library/Safari/History.plist` directory.

2. In order to read the file you will need to use a new program called `xxd`. Use the command `xxd <filename>` in the terminal to do so. 

3. Does this file contain any web URLs?

    * Hint: Look for the `http://` sequence in **Hex**.

4. Record what you find in the *Group Evidence Worksheet*.

Assignment Complete!
