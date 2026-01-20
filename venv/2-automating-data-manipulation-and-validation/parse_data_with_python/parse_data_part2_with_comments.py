# CSV library is imported.
import csv

# File path is defined.
file_path = "groceries.csv"

# `with` statement to open the file.
with open(file_path, "r") as file:
    # Inside with` statement the `csv.reader` func is called to read the data from the file.
    csv_reader = csv.reader(file)
    # To separte the data from the header, the next() func is called.
    headers = next(csv_reader)
    # for-loop iterates through each row of the remaining data.
    for row in csv_reader:
        # In the loop the int func is called to convert the quanity value from string to integer (a numeric data type).
        # Index location 1 is where the quanity value lives.
        row[1] = int(row[1])
        # Print out the row.
        print(row) 

# Run the program: `python3 parse_data_part2.py`
# x7 rows printed out with x2 cols per row.

####
# Line 16: `row[1] = int(row[1])`
# The `int` func is used to convert the quantity value from a string to an integer as its useful to perform mathematical operations on integers.
# Integers display without quotes when printed.
# It represents data more accurately for numerical processing.
## Then `row[1]` would be the quantity column, and this line converts those quantity strings into actual numbers.
####
