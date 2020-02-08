## SIEMS Day 2:  Guided Practice - Warm-Up Exercise
--------

### Instructions

- Welcome Back! In this Guided Practice you will prepare for a technical interview about using Splunk Enterprise.   

- Start by downloading the **[tutorialdata.zip](Resources/tmp/tutorialdata.zip)** file.  It will be used in the hands-on exercise.

- **Hands-on Exercise using SPL to Execute Searches:**

  You might be asked to demonstrate how to use SPL to perform searches related to **website performance** and **threat detection**.

  To prepare you will use the **tutorialdata.zip** file. This file contains the machine data from the **buttercupgames** website. 

    * Log into the Splunk Web Interface. 

    * When uploading the tutorialdata.zip file, save the `host` parameter as `quiz`

    * Execute the following searches specifying `All Time` for the time range.

    * Be prepared to answer what each command does, and how many events were found. 

* Here are the four SPL search commands.  They use wildcard, logical and relational operators and Boolean expression from the Day 1 Lesson.

    - `host=quiz sourcetype=access_* AND (status=500 OR status=404)`

    - `host=quiz source=*mailsv/secure.log failed password`

    - `host=quiz source=*www1* useragent=*`

    - `"?msg=Credit*" AND file="error.do" AND source!=*www2*`
