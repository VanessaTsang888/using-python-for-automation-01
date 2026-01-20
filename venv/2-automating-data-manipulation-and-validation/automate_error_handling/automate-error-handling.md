# automate-error-handling

automate_error_handling_part1.py

Try-Accept Block to catch possible runtime errors, also known as exceptions.

In this example, the goal is to get the user to input a number and perform a calculation with that number. However, there are two potential errors that you could get, the user might enter a non-number value or they might enter zero as the input. To handle these errors gracefully, you use a try-except block. The try block contains the code that might raise an exception. So if the user enters a value that isn't a number, a ValueError will occur. And if the user enters zero, the division operation will raise a ZeroDivisionError. If an exception occurs within the try block, execution immediately jumps to the appropriate except block based on the type of exception that occurred. So if a ValueError occurs, you print a message indicating that the input was invalid. And if a ZeroDivisionError occurs, you print a message indicating that you cannot divide by zero. If no exception occurs, the except blocks are skipped and the code continues to execute normally. Now, run the program to check out how it works. First, enter a number that's not zero. Then, run the program a second time, and this time, enter zero. Next, run the program a third time, and this time, enter a value that's not a number. The try-except structure worked.

## The Code

File: automate_error_handling_part1.py

The goal is to get the user to input a number and perform a calculation with that number.

There are two potential errors that you could get, the user might enter a non-number value or they might enter zero as the input. To handle these errors gracefully, you use a try-except block.

```python
# `i` is generic placeholder for a number.
try:
    number = int(...)
    result = i / number
    print(...)
except ValueError:
    print(...)
except ZeroDivisionError:
    print(...)
```

### Testing

Execute this cmd script: `python3 automate_error_handling_part1.py`

### Results

10 / 3 = 3.333

```python
# Execute the program
(using-python-for-automation-1) Mac:automate_error_handling vanessatsanguk$ python3 automate_error_handling_part1.py
# User entered '3'
Enter a number: 3
# 10 / 3 is 3.3
The result is: 3.3333333333333335
# Execute the program again
(using-python-for-automation-1) Mac:automate_error_handling vanessatsanguk$ python3 automate_error_handling_part1.py
# User entered '0'
Enter a number: 0
# Auto generated msg as zero cannot be divided by anything
You cannot divide by zero.
# Execute program again
(using-python-for-automation-1) Mac:automate_error_handling vanessatsanguk$ python3 automate_error_handling_part1.py
# User entered chars that is NOT a number
Enter a number: hello
# So below is auto generated for inform user that thier input must be a valid integer number
You must enter a valid integer.
```

automate_error_handling_part2.py

Use an assert statement to check for a logical error. In this example, years is defined as a list of numbers, and the goal is to sort the years in place. Let's consider what would happen if you accidentally used the wrong method, for example, if you called the reverse method, which reverses the order of the elements in a list. Afterwards, years is printed out, and there's an assert statement to check the logic of the code. Specifically, it checks if the first element is less than or equal to the last element in the updated list. This is a quick way to check if the list got sorted or not. Run the program. You'll notice an AssertionError that is evoked due to the logical error from calling the reverse method instead of the sort method. This error message tells you what's wrong, so you can easily fix the issue. Now, you can fix the error by replacing reverse with sort. Save and run the program. And it works, no errors this time By using try-except blocks and appropriately handling exceptions in your code, you can prevent unexpected errors, improve the reliability of your code, and provide a better experience for your users. Go ahead and implement try-except blocks and assert statements to automate error handling in your own Python code.

## The Code

```python
years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
years.reverse()
print(years)
assert years[0] <= years[-1], "First element is greater than last element."
```

### Testing

Execute this cmd script: `python3 automate_error_handling_part2.py`

### Results

```python
# Error because we used the `reverse()` method instead of `sort()` method.
(using-python-for-automation-1) Mac:automate_error_handling vanessatsanguk$ python3 automate_error_handling_part2.py
[1996, 1920, 1954, 1989, 1912, 1975, 1937, 1968, 1943, 1925]
Traceback (most recent call last):
  File "/Users/vanessatsanguk/Documents/code05/using-python-for-automation/using-python-for-automation-1/2-automating-data-manipulation-and-validation/automate_error_handling/automate_error_handling_part2.py", line 11, in <module>
    assert years[0] <= years[-1], "First element is greater than last element."
           ^^^^^^^^^^^^^^^^^^^^^
AssertionError: First element is greater than last element.
```

Replace the `reverse()` method with the `sort()` method to execute with a resutl without any errors.

```python
(using-python-for-automation-1) Mac:automate_error_handling vanessatsanguk$ python3 automate_error_handling_part2.py
# test passed the data is in the correct order as expected this time so no logical error printed out.
[1912, 1920, 1925, 1937, 1943, 1954, 1968, 1975, 1989, 1996]
```

### Conclusion

By using try-except blocks and appropriately handling exceptions in our code, you can prevent unexpected errors, improve the reliability of your code and provide a better experience for your users. Implement try-except blocks and assert statements to automate error handling in our own Python code.
