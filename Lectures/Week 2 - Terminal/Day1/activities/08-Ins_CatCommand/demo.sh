# Show the first 10 lines of a file
head frank_1.txt

# Show the last 10 lines of a file 
head frank_2.txt

# Print the contents of one or more files to the terminal: cat <file1> <file2> ...
cat frank_1.txt

# Combine two files into one (without saving)
cat frank_1.txt frank_2.txt

# Combine two files into one and save the result into a new file
cat frank_1.txt frank_2.txt > frank_full.txt

# Combine two files into one, save the result in a new file, and immediately preview its contents
cat frank_1.txt frank_2.txt | tee frank_full.txt

# Look at first 3 lines of a file
head -3 frank_full.txt

# Look at last 3 lines of a file
tail -3 frank_full.txt
