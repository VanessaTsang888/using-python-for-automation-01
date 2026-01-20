# Open and store this text file in the variable on the left.
# Pass-in the string `r` to read the file.
inputFile = open("inputFile.txt", "r")
for line in inputFile:
    # Split each element on each line. Defaults on splitting on whitespaces.
    line_split = line.split()
    # The 'P' or 'F' is located in at index two.
    if line_split[2] == "P":
        print(line)
inputFile.close()