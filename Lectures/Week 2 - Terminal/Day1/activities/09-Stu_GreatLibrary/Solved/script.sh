# Navigate into Books folder
cd Books

# Create a new folder called Summary
mkdir Summary

# Preview each of the files
less 1_call_to_worship.txt
less 2_dangerous_js.txt
less 3_weird_machines.txt
less 4_great_tea.txt
less 5_phone_hacking.txt

# Combine each text file 
cat 1_call_to_worship.txt 2_dangerous_js.txt 3_weird_machines.txt 5_phone_hacking.txt > full.txt

# Preview the top and bottom contents
head -10 full.txt
tail -10 full.txt

# Move the full file into the Summary folder 
mv full.txt Summary/

