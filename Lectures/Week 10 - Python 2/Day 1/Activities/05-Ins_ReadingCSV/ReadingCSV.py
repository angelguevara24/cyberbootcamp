
# Connect to the file and read in the text it contains
wrestling_csv = open("WWE-Data-2016.csv", "r")
wrestling_text = wrestling_csv.read()

# Since a CSV is broken into rows and columns, it will need to be split twice
# The first split is to break the original text into rows by splitting on each new line
wrestling_rows = wrestling_text.split("\n")
wrestling_rows.pop()
print(wrestling_rows[0])
print(wrestling_rows[1])
print(wrestling_rows[2])
print(wrestling_rows[3])
print("-----------")


# The next split will then split the row into its respective columns on commas
wrestling_cells = wrestling_rows[0].split(",")
print(wrestling_cells[0])
print(wrestling_cells[1])
print(wrestling_cells[2])
print(wrestling_cells[3])

wrestling_csv.close()