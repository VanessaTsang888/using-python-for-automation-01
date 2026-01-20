import csv

file_path = "groceries.csv"

# `row[1]` would be the quantity column (index location 1 as Arrays are zero based),
# and this line converts those quantity strings into actual numbers.
with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    for row in csv_reader:
        # Index location 1 is where the quanity value lives.
        row[1] = int(row[1])
        print(row)

        