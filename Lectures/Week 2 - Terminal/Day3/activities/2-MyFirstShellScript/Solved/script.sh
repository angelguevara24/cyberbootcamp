# Create a folder called Summary
mkdir Summary

# Combine all files in the Files folder into a single file called MySummary.txt
cat Files/*.txt > MySummary.txt

# Move the MySummary.txt file into the Summary folder.
mv MySummary.txt Summary

# Preview the contents
head Summary/MySummary.txt