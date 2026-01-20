# read-files-with-python

Read and iterate through elements within a Python file.

1. Print the content of the 'read_files.py`'.
2. Print only only the people who passed their driving test -> 'P'.

## Transcript

If we don't wish to print the whole and only the people who passed the behind the wheel drive test. For this we need to iteratively check each line in the file, determine whether the person passed the drive test, and only if that's trueprint out that line.

Write a for-loop that iterates through each line of the file. Inside the loop, split the line using the `.split` function, which defaults to splitting on whitespace.

## Code

```python
inputFile = open("inputFile.txt", "r")
for line in inputFile:
    line_split = line.split()
    # The third element of each line is either 'P' or 'F'.
    if line_split[2] == "P":
        print(line)
inputFile.close()
```

### Notes

Iterate through each element on each line and find 'P' for Pass and print that line if it contains the 'P'.

Arrays are zero index based. Therefore, the 'P' or 'F' is located at index two.

### Testing

Run the programme wit in the terminal: `python3 read_files.py`

### Results

```python
# Run program:
(venv) Mac:read_files_with_python vanessatsanguk$ python3 read_files.py

# All people whom have passed their driving test:
Mary 25 P

John 32 P

Hailey 26 P

Iris 23 P

Jacob 29 P

Jamie 26 P

Chloe 21 P

Natalie 29 P

David 23 P

Mario 51 P

Josh 39 P

Kayla 28 P

Hunter 61 P

Erica 16 P

Kyle 19 P

Rosanna 45 P

Joy 28 P

Jim 67 P

Sansa 28 P

Juan 73 P

Colin 59 P

Kate 58 P

Jade 26 P

River 29 P

Chris 31 P
# Output successfully executed and back to prompt:
(venv) Mac:read_files_with_python vanessatsanguk$
```
