## Solution Guide: Digital Forensics in the Cloud Review

### Solutions

1. Examine the  study in the [Digital_Forensics_in_Cloud.pdf](Digital_Forensics_in_Cloud-1.pdf) with your group.

   * Start by reviewing the [*Digital_Forensics_in_Cloud.pdf*](Activities/Stu_Cloud_Forensics/Unsolved/Resources/Digital_Forensics_in_Cloud-1.pdf) case study with the students.

   - Poll groups to review their findings. 

      - Did students find that cloud forensics was different than other areas? 
      - How did the differences affect chain of custody?


2. Are there components that make digital forensics in the cloud different from other forensic areas? If so, list at least four.
  
   - There is no physical access to the computer where the crime took place.
   - If the crime takes place on a cloud server, a malicious user can claim that everyone in the world with internet access should be a suspect. 
   - When the crime takes place on a cloud server, it's difficult to pinpoint where their data ends and where another company, that police do not have a warrant for, begins. 
   - Because many people will often use the same cloud server, there are SLA's that have to be recognized when dealing with other companies.
   - Volatile memory, such as RAM, would be lost if the cloud server is rebooted.
   - It would be difficult to trace which cloud server is storing the users data.


3. How do the differences affect the chain of custody?

    - It's difficult to pinpoint where, and which cloud server has been compromised. This would also present the problem of the cloud server being in another county's jurisdiction.

### Additional Review / Follow Up

* Emphasize the importance of maintaining a chain of custody in forensic cases. If you have experience with chain of custody in your career, please provide some best practices. 

* Point out some of the challenges in maintaining chain of custody in cloud forensics, such as:

  * **No physical access**: The exact location of where the data may not be known.

  * **Preserving the evidence**: Isolating and securing the evidence is challenging when data is located in multiple locations.

  * **Data integrity**: Evidence may be captured live and the evidence could be altered if not collected correctly.

* Discuss other issues:

  * **Trustworthiness**: As stated in the case study, investigators must trust the Cloud Service Provider (CSP).

  * **Resource sharing**: Mallary knew that some hardware and software had been shared by many users, thus claiming that their instance had been comprised by someone else.

  * **Recovery of deleted data**: Investigators must request backups from CSPs in order to obtain deleted files.
  
Address any questions before moving on. 