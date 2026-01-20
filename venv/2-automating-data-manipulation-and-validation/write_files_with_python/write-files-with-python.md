# write-files-with-python

1. Utilize automation to write files in Python.

2. Setup conditions for file creation.

3. Verify proper file creation.

## The Data

Data file: 'inputFile.txt'

## The Goal

Write is to write all of the lines that pertain to people who passed the test into a new file called 'passFile.txt'.
Then the same for all the people who failed their test.

So call the open function to create a file called 'passFile.txt' that the program will write to. Pass in the string 'w'.

...

### Run the Program

Execute this command to run the program: `python3 write_files.py`

### Testing

To confirm the two files are created successfully, navigate to the files explorer -> directories, first locate 'passFile.txt'. Open it up and check that it only contains lines with 'P' at the end. Then locate 'failFile.txt'. Open it up and check that it only contains lines with 'F' at the end.

#### Results

My test passed because when I ran the program, the two new text files appeared in the directory called '2-automating-data-manipulation-and-validation' as expected:
"passFile.txt" and "failFile.txt".
