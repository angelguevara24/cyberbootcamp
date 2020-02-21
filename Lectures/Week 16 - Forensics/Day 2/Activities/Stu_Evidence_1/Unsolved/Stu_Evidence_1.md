## Student Activity: Is This Tracy's iPhone?

### Instructions

In this activity, you will analyze the contents of Tracy's iPhone image to begin to establish your forensics case.

You will search the iPhone databases and files to determine if Tracy is the owner of the device. 

You can use **Google** to gather more information about the iPhone structure as well as other information you will find in the image.

* Document your findings in the [Evidence Worksheet Document](Activities/Stu_Evidence_1/Unsolved/Stu_Evidence_1_Worksheet.docx) worksheet.

* It is important to capture the file metadata using the **File Metadata** tab.

* You will need to use the **Keyword Search** in order to find the information that you are looking for. 
  * **Hint:** Remember that text is viewed using the **Indexed Text** tab in the **Data Content** pane.


#### Get Started

1. Start the Kali Linux VM.

1. Open a terminal window.

1. Navigate to the `autopsy-files/autopsy-4.10.0/bin` directory.

1. Start Autopsy: ` ./autopsy` 


#### Information of Interest on Tracy's Phone

Use the [iPhone Image File Layout](Activities/Stu_Evidence_1/Unsolved/Stu-iPhone-Image-FileLayout.pdf) file to search the iPhone databases and files for the following information:

* MD5 hash of the iPhone disk image

* Device Information:   
 
    * Device model

    * Device serial number

    * OS Version #

    * Installation timestamp

    * Integrated Circuit Card ID (ICCID) number

    * International Mobile Equipment Identification (IMEI) number - you will need to use Keyword Search in Autopsy to find this, it is not in the standard log files.

* Tracy's personal information: 

    * Tracy's phone number

    * Tracy's email Address

* Be sure to document all of your evidence!
