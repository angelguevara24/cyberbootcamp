
### Start gAWK-ing Activity!

## Setup
* For this activity, move into the Stu_Awk directory and locate the '17-18-Breaches.txt' file.
* **File:** [activities/Stu_Awk/Stu_Awk.zip](activities/Stu_Awk/Stu_Awk.zip)

* **Instructions:**

* Using the **17-18-Breaches.txt** file create various `AWK` commands that accomplish the following:

**Solutions**

Start by navigating to the Ins-Awk directory in your command line:

* Print only the first field of the 17-18-Breaches.txt.
  > **Solution**: `awk -F"\t" '{print $1}' 17-18-Breaches.txt`

* Print only the breaches from 'web' companies.
  > **Solution**: `awk '/web/' 17-18-Breaches.txt`

* Out of the web companies that were breached, print only the company name
  > **Solution**: `awk -F"\t" '/web/{print $1}' 17-18-Breaches.txt`

* Print all the breaches from 2017
  > **Solution**: `awk '/2017/' 17-18-Breaches.txt`

* For the companies that had breaches in 2017, print only the company name and the number of records lost.
  > **Solution**: `awk -F"\t" '/2017/{print $1, $3}' 17-18-Breaches.txt`

* For the companies that had breaches in 2018, save the company name, Company type and number of breaches to a new file named 2018Breaches.txt
  > **Solution**: `awk -F"\t" '/2018/{print $1, $4, $3}' 17-18-Breaches.txt > 2018Breaches.txt`
