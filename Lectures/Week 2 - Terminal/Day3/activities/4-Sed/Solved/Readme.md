### He sed, She sed Student Activity.

## Setup
* For this activity, move into the Stu_Sed directory and locate the 'lights.txt' file.

* **Instructions:**

  * Using the **lights.txt** file create a sed command that accomplishes the following:

    1. Changes `dark` to `bright` where it makes sense to do so.

    2. Changes `bright` to `dark` where it makes sense to do so.

    3. Changes `but` to `and` in the first sentence.

    4. Changes `on` to `off` at the end of the second sentence.

* The final command should output:
 - When the light was on the room was bright and when the room was dark the light was off.
 - They left the light on so she turned the light off.

## Activity

* Run the command to display the contents of the 'light_dark.txt' file.
 - `cat lights.txt`

* Notice that the story doesn't quite make sense because the state of the light is opposite of what it should be.

* Create a sed command that changes the first instance of `dark` to `bright`.
  > **Solution**: `sed 's/dark/bright/ lights.txt'`
* Create a sed command that changes the first instance of `bright` to `dark`.
  > **Solution**: `sed 's/bright/dark lights.txt'`
* Create a sed command that changes the first instance of `but` to `and`.
  > **Solution**: `sed 's/but/and/' lights.txt`
* To fix the last line, create a sed command that changes only the second instance of `on` to `off`.
  > **Solution**: `sed 's/on/off/2' lights.txt`
* Now, combine all of these commands into one command that fixes the entire file.
  > **Solution**: `sed -e 's/but/and/' -e 's/on/off/2' -e 's/bright/dark/' -e 's/dark/bright/' lights.txt`
* Finally, save the result of this command to a new file called `new_lights.txt`
  > **Solution**: `sed -e 's/but/and/' -e 's/on/off/2' -e 's/bright/dark/' -e 's/dark/bright/' lights.txt > new_lights.txt`
