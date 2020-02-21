## Student Activity: Warm-Up

### Instructions 

Welcome back! In this guided practice, you review the steps from Day 1 for creating a new case. We've added some new steps too. 

Please ask your TA for help if you need it.

#### Getting Started

1. Log into CybrScore

1. Start the Kali VM.

1. Open the `Show Applications` menu located at the bottom of the tool bar on the left hand side. 

1. In the search box type `Autopsy`. Click to load the program. 

1. Start a new case using the following information:

* **Case name**: 2012-07-18-National-Gallery
	
* **Case number**: A123456
	
* The **image file** is the same as Day 1: *tracy-phone-2012-07-15.final.E01*
	
  - Located in the `/root/corpus` directory
	
* **Extension Mismatch Detector**: Check all file types
	
* **Keyword Search**: Just select **URL**

1. Select **Finish**.

    * The files will now be analyzed by Autopsy. When this process is finished, the file will be ready. This may take some time.   
		
    * The **progress bar** in the right hand area of the screen will indicate when the ingest is complete. 
				
1. When the ingest is complete, locate the **Encryption Detection** area in the Directory Tree and open the *documents.zip* file to view the data in the image.

1. The image starts with the **Directory Sources** tree.

1. In the tree, you will see *tracy-phone-2012-07-15-final.EO1*, which is the iPhone image file.
	
   * Don't worry if you do not understand everything in the image file. You'll learn more during the instruction and activities.
	
#### Look at Tracy's Browsing History

This example shows how to navigate to an evidence file without traversing the evidence tree. All you need to know is the file name.

1. From the Tools menu, select `File Search by Attribute`.

1. Click the box next to Name and type `History.plist`.

1. Click the Search button.

1. Now select `History.plist` from the `Listing` pane.
  - **Note:** You only need the `/Safari/History.plist`

1. Select the Indexed Text tab in the Data Content pane list off five searches that she preformed on her phone.

#### Look at File Metadata

Next, we'll look at the file metadata. We need this information for our evidence reporting.

* Select the File Metadata tab in the Data Content pane to see the md5 hash, creation date, file name, and location. 

That completes the activity. Great job finding your first pieces of evidence! 
	
