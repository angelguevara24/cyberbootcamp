## Digital Forensics Homework 

* Lab Environment:

	* Kali Linux
	
	* Autopsy 10.0


Welcome to the HomeWork Assignment for Digital Forensics!

There are two choices for the assignment.  You may try both but ONLY submit one assignment.

The files for the assignment are located in the VM in the `autopsy-files/homework` folder.

## Option 1:

## Homework Objective

The goal of this homework exercise is to continue to document the Autopsy case and look for additional information in other directories in the image file.

* Look for information in other directories in the image.

   * Images in the `mobile/media/dcim/100appple` folder 

   * Call log in `call_history.db`

   * WiFi locations in `root/Library/Caches/locationd/consolidated.db`

      **Note:** Put the GPS coordinates into Google Maps to see the locations.

   * AddressBook in `vol5/mobile/Library/AddressBook`

* Document any additional information in the Evidence Worksheet.

* Update the *Evidence Worksheet* to include the equipment and tools you used to gather and analyze the evidence. For example, Autopsy, the operating system (Kali Linux), text editors (nano), etc.

* Congratulations...You've finished the assignment! 

## Option 2:

## Homework Objective

The goal of this homework exercise is to sharpen your skills in locating and identifying data in a forensic image. This is an important skill when tasked with locating and decoding data such as `executable code` or a `malicious document` embedded in an image or network log.  The assignment continues the Hex decoding Guided Practice but this time we look at Unicode notation.


* Here are the files for the exercise: 

	* RussianTeaRoom.zip (560 KB) - This file contains the `Autopsy` case file and `Encase image` file.
	
	* menu.pdf (56.0 KB) - This file contains the Russsian Tea Room menu.
	
	* RussianTeaRoom-UTF-16-decipher.xls (12 KB) - This file contains a blank Excel for recording the answers.
	
	* Unicode-Tutorial.md - Short tutorial
	


## Scenario: The Case of the Little Russian Team Room

![Images/boris-natasha-1.jpg](Images/boris-natasha-1.jpg)

The evil Boris and Natasha have escaped from jail and are up to their old tricks. They have stolen the new menu from *The Little Russian Tea Room* and will sell it to the highest bidder. Your task is to reconstruct the menu from an Encase image of their hard drive. 

Here are the menus in Russian and English:

* ЗАКУСКИ (Appetizers)
* СУП (Soup)
* БЛИНЫ (Pancakes)
* ПИРОЖКИ И ПЕЛМЕНИ (Meat pies and dumplings)
* МЯСО И РЫБА (Meat and fish)
* СЫР И МОЛОЧНЫЕ (Cheese and milk products)
* НАПИТКИ (Beverages)
* СЛАДКОЕ (Dessert)

 The complete menu is [*here*](menu.pdf).

The English and Russian text for the menus are both available in the hard drive image.  However, only the *English* text is readable.  Your goal is to find the **Russian text** because this is what Boris and Natasha placed on their hard drive.

**Hint 1:** The strings in the Encase image are Hex and represent the UTF-16 format.  

## Getting Started:

 It's IMPORTANT that you are familiar **Hex** and **UTF-16 encoding and decoding**.  Please review this [*tutorial*](Unicode-Tutorial.md) and the practice exercises. It will help in locating the menus on the hard drive image.
																				
	
## Start the Investigation

Your task is to *find*, *decode* and *document* **six of the menus** from the hard drive image using the Unicode Cyrillic and Latin character (cipher) set.

* Launch **Autopsy** and select `Open Case`.

* Open the `RussianTeaRoom` folder and select `RussianTeaRoom.aut`

* Add the `Russian-TeamRoom.E01` Encase image file to the case.

* This is a sample of the hex data in the Autopsy `RussianTeaRoom` case file.

	![Images/hex-data.png](Images/hex-data.png)	
	
### Document Your Findings


Download the [*spreadsheet*](RussianTeaRoom-UTF16.xlsx) to document the following information from the Encase image for the investigation. 

1. Find and document the **complete file location** for six (6) menus in the image. 

	* **Hint 2:** There may be *multiple* locations for the same file.

2. Document the **menu items** in Cyrillic (e.g., бифштеке)and English (e.g,  steak) for the following menus:

	* Pancakes (Menu #3)
		
	* Meat and Fish (Menu #5)
	
	* **Hint 3:** Use the **Hex** and **String** tabs in **Data Content** window in Autopsy to view the data.

	![Images/string-dump.png](Images/string-dump.png)

	Include:

	* *starting location in the hex dump* (e.g., 0x00000010).
		
	* *hex string* for a menu name or menu item (e.g., `00 42 00 65 00 76 00 65 00 72 00 61 00 67 00 65 00 73`). 
		
	* *UTF-16 escape sequence* for a menu name or menu item (e.g., `\u0042\u0065\u0076\u0065\u0072\u0061\u0067\u0065\u0073`).


## What to Submit for the Assignment

* Please submit the completed **TeaRoom-UTF-16-decipher.xls** file.

	* `<yourfirstname_yourlastname>_RussianTeaRoom-UTF16.xls`

* Congratulations...You've finished the assignment! 






	
