# validate_inputs_with_automation

Use Python to validate user input. **_Automate input validation to protect digital transactions from data breaches and financial losses._**

Every day, millions of data transactions occur in the digital world, from simple online purchases to complex banking operations. A single error in these inputs can lead to disastrous consequences, such as financial loss or a breach of sensitive information. It is very useful to understand how to automate input validation, a crucial shield, protecting digital transactions from such errors.

1. Discover automation of input validation.
2. Understand its role as a shield.

Use the `PyInputPlus` library to valide user input.

## The Code

three examples in how to use the `PyInputPlus` library to valide user input

Import statement: PyInputPlus library using the alias `pyip` for ease of use.

[PyInputPlus](https://medium.com/@eva21fachria/enhance-user-input-validation-with-pyinputplus-a-python-alternative-for-error-free-input-81dce07c16bb) is a Python library that enhances the built-in input() function with advanced input validation features. It automatically handles invalid user input by repeatedly prompting the user until valid data is provided, preventing runtime errors and improving program robustness.

### Example 01

Call `pyip.inputInt` and pass in a prompt string that says, `enter the number of shopping bags you will need for your items:`, followed by the parameter `min`, set equal to 'zero'. This means that when the program is run, the user will be prompted to enter the number of bags, and the program will validate the input. Specifically, it will check that the input is an integer and that it's greater than or equal to zero. Save the output in a variable named result and then print it out.

### Example 02

Use another function for input validation. Call the `pyip.inputMenu` function. Passing a list of three colors as strings, set the lettered parameter equal to True and the numbered parameter equal to False. Save the output in a variable named result, and then print it out after.

### Example 03

Call the `pyip.inputEmail` function. Pass in a prompt string that says, enter your email address:, and save the result in a variable, so it can be printed out after.
When this program is run, the user will be prompted to enter their email address and the program will check if it's a valid email. Now, save and run your code to check out how it works.

#### Testing

Execute the program with: `python3 validate_inputs_with_comments.py`

I am testing my program as if I am the user.

Make sure to enter input when prompted. And it works as expected. The program gathered all of the data that we provided.

These are just a couple of examples of using functions from the `PyInputPlus` library to validate data from user input. Feel free to check out the documentation on pypi.org/project/PyInputPlus for more information and practice using these functions on your own.

#### Results

See attached screenshot of the test in the Terminal within the 'tests' directory.

```python
# Prompt in the Terminal
(using-python-for-automation-1) Mac:validate_inputs_with_automation vanessatsanguk$ python3 validate_inputs_with_comments.py

# Printed in the Terminal: I entered number 8.
EXAMPLE 1
Enter the number of shopping bags you will need for your items:8

You will use 8 store bags.

# I entered 'A'.
EXAMPLE 2
Please select one of the following:
A. red
B. blue
C. green
A

You have chosen a red marker.

# I entered: vanessa.today@email.com.au
EXAMPLE 3
Enter your email address:vanessa.today@email.com.au

# Yes, that is my Email Address I entered.
The email you entered: vanessa.today@email.com.au

# Back to prompt as program execution completed
(using-python-for-automation-1) Mac:validate_inputs_with_automation vanessatsanguk$
```

The program gathered all of the data that the user provided.
These are just a couple of examples of using functions from the `PyInputPlus` library to validate data from user input. Check out the documentation on [pypi.org/project/PyInputPlus](https://pypi.org/project/PyInputPlus/) for more information and practice using these functions on your own.
