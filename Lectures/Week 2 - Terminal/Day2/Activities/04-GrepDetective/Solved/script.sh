# CD into IRC_Logs
cd IRC_Logs

# Find the days for which power2all, glanzmann, gansbrest, and E1ven were active
grep -rli "power2all" .
grep -rli "glanzmann" . 
grep -rli "gansbrest" .
grep -rli "E1ven" .

# Find the times for which power2all, glanzmann, gansbrest, and E1ven logged on and off
grep -i "power2all has" *
grep -i "glanzmann has" *
grep -i "gansbrest has" *
grep -i "E1ven has" *

# Bonus
# -------------------------------------------------------------------------------------
# Create folders for each of the above users.
# Then copy every log for which they appear into their respective folder.
mkdir power2all glanzmann gansbrest E1ven
find . -type f -exec grep -rli "power2all"  {} \; -exec cp {} power2all \;
find . -type f -exec grep -rli "glanzmann"  {} \; -exec cp {} glanzmann \;
find . -type f -exec grep -rli "gansbrest"  {} \; -exec cp {} gansbrest \;
find . -type f -exec grep -rli "E1ven"  {} \; -exec cp {} E1ven \;
