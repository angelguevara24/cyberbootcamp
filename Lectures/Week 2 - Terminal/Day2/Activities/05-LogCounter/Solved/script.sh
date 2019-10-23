# Part I: Basic Counts
# --------------------------------
# Navigate into the IRC_Logs Folder
cd IRC_Logs

# Count the total number of log files
find . -type f | wc -l

# Count the number of logs that exceed 100 KB
find . -type f -size +100kb | wc -l



# Part II: Login Counter
# --------------------------------
# Count the number of instances in which the user "glanzmann" appeared
grep -i "glanzmann has joined" * | wc -l

# Count the number of instances in which the user "E1ven" appeared
grep -i "E1ven has joined" * | wc -l



# Part III: Chat Counter
# --------------------------------
# Count the number of instances in which the user "glanzmann" spoke
grep -i "<glanzmann>" * | wc -l

# Count the number of instances in which the user "E1ven' spoke
grep -i "<E1ven>" * | wc -l



# Part IV: Day Counter
# --------------------------------
# Count the total number of days for which "glanzmann" logged on
grep -rli "glanzmann" . | wc -l

# Count the total number of days for which "E1ven" logged on
grep -rli "E1ven" . | wc -l

