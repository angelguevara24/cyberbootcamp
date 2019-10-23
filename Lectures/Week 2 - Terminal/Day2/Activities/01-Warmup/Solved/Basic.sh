# Option 1 (Basic)
# --------------------------------
# Create the Archive folder
mkdir Archive

# Navigate into TodaysLog folder
cd TodaysLog

# Combine the files in TodaysLog
cat 1 2 3 4 5 > '09_15_18.txt'

# Move the file to Archive
mv 09_15_18.txt ../Archive

# Navigate to Archive
cd Archive

# View archived result
less Archive

