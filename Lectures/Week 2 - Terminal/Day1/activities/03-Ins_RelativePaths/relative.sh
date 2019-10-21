# Move into the Level_1 folder
cd Level_1

# Print working directory
pwd

# Enter Level_2 folder
cd Level_2

# Print working directory
pwd

# Return to Level_1 folder
cd ../

# Enter Level_3 folder
cd Level_2/Level_3
# Print working directory 
pwd

# Return to Level_1 
cd ../../

# Print working directory 
pwd

# Head to Level_5 folder
cd Level_2/Level_3/Level_4/Level_5

# Return to Level_1 folder
cd ../../../../

# Print working directory 
pwd

# List files in Level_1
ls

# Copy file from Level_1 to Level_2 (note the `.`)
cp Text-1_1.txt ./Level_2

# Move file from Level_1 to Level_2 (note the `.`)
mv Text-1_2.txt ./Level_2

# View files in Level_2
cd /Level_2
ls

# Return to root 
cd ~