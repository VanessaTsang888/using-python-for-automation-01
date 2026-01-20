# Open inputFile.txt with the intention of reading it
inputFile = open("inputFile.txt", "r")

# open passFile.txt with the intention of writing it
passFile = open("passFile.txt", "w")

# open failFile.txt with the intention of writing it
failFile = open("failFile.txt", "w")

# loop through each line in inputFile.txt
# If not `P` then its 'F'.
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

# close inputFile.txt as we are done with this file.
inputFile.close()

# close passFile.txt as we are done with this file.
passFile.close()

# close failFile.txt as we are done with this file.
failFile.close()