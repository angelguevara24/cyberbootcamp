## Student Activity: Introduction to Autopsy 

### Instructions 

In this activity, you will load evidence into Autopsy for analysis. Please follow the directions in the checklist. Ask your TAs for assistance if needed.

#### Prepare the Data

1. Start the **Digital Forensics - Autopsy** lab instance located in CybrScore. 

1. Start the Kali-Linux-VM.

1. Open a terminal window.

1. Generate **md5** and **sha256** hashes for the evidence. This will be used to validate that nothing was changed during the investigation.
  - **Note:** The tracy-phone-2012-07-15.final.E01 is located in your `/corpus` directory. 

   * Run `md5sum tracy-phone-2012-07-15.final.E01 > tracy.original.md5log.txt`

   * Run `sha256sum tracy-phone-2012-07-15.final.E01 > tracy.original.sha256log.txt`

#### Get Started: Create a Case

1. Open the application menu on the bottom left of the tool bar. 

1. Type Autopsy and click on the application to start it. 

1. The splash screen displays. Select **New Case**.

### Step 1: Set Up the Case Information

1. Enter a **Case Name**: *day-month-year*-National-Gallery

1. Enter a **Base Directory**: `/root/casedata`

1. Enter a **Case Type**: Single-user

1. Select **Next**.

#### Enter the Optional Information:

1. Enter a **Case Number**: 1Nat347B

1. Enter **Name**, **Phone**, **Email**, and **Notes**. 

1. Enter the **Organization** that will provide more information if necessary.

   * Select **Manage Organizations** and then **New**.

   * Enter the **Organization Name** and **Point of Contact** information.

1. Select **Finish**.

### Step 2: Select Types of Data

1. Select **Disk Image or VM File** and **Next**.

1. Browse to where the evidence files are located on */root/corpus*.

   * Select *tracy-phone-2012-07-15.final.E01*.

1. Select an **E01 file** and **Open**.

1. Select **Time zone** and leave **Sector size** at **Auto Detect**.

1. Select **Next**.

### Step 3: Configure Ingest Modules

1. Set the **Additional Ingest Settings**:

   * **Keyword Search**

   * **Extension Mismatch Detector**

1. Select **Finish**.

*  Autopsy will analyze the files. When this process is finished, the file is ready. 

* This will take some time. A progress bar is located in the bottom right hand corner of the window. You can click on it to see the status.

 ### Step 4: View Output from Autopsy

 * When the ingest process is complete, locate the **Encryption Detection** area in the **Directory Tree** and open the *documents.zip* file to view the data in the image.

* Congratulations! You've finished the activity!
