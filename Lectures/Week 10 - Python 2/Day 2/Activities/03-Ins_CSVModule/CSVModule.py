# Module for reading CSVs
import csv

###################################################
### Method 1: Improved Reading using CSV module ###
###################################################
csvFile = open("WWE-Data.csv")

# The `csv.reader()` method is used to read in the data within the file
contents = csv.reader(csvFile)
# Contents returned as a CSV object
print(contents)

# The CSV object can be looped through without any splitting
for row in contents:
    print(row)

    # rows are already created as lists of cells for us, so no need to split
    print(row[0])


#################################################
### Method 2 (Old): Plain Reading (no module) ###
#################################################
csvFile = open("WWE-Data.csv")

# The `file.read()` method is used to read in the text within the file
contents = csvFile.read()
# Contents of the file have been returned as a giant string
print(contents)

# contents is one big string, so we have to manually split it up
rows = contents.split("\n")

for row in rows:
    print(row)

    # row is still just one big string, so we have to manually split it up
    cells = row.split(",")

    print(cells[0])