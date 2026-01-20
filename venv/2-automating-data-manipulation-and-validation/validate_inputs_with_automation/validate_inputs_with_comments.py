# PyInputPlus library using the alias `pyip` for ease of use.

import pyinputplus as pyip

print("\nEXAMPLE 1")

# When the program is run, the user will be prompted to enter the number of bags, and the program will validate the input.
# It will check that the input is an integer and that it's greater than or equal to zero. Save the output in a variable.
result = pyip.inputInt("Enter the number of shopping bags you will need for your items:", min=0)

# Print the output that's stored in the variable.
print("\nYou will use", result, "store bags.")
# Print the below 'str' on a new line.  
print("\nEXAMPLE 2")

# Use another function for input validation.
# Call `pyip.inputMenu` func, passing a list of three colors as 'str', set the lettered param equal to True, the numbered parameter equal to False.
# Save the output in a variable.
result = pyip.inputMenu(["red", "blue", "green"], lettered=True, numbered=False)

# Print the output in the `result` variable on a new line.
print("\nYou have chosen a", result, "marker.")

# Use another function for input validation.
print("\nEXAMPLE 3")

# Call the `pyip.inputEmail` func, Pass in a prompt 'str' as param, save the result in a variable so it can be printed out later.
# when program is run, user will be prompted to enter their email address and the program will check if it's a valid email.
result = pyip.inputEmail("Enter your email address:")

# Print below 'str' and the user's input stored in the variable, on a new line 
print("\nThe email you entered:", result)

# Now use this cmd script to execute and test the program in the Terminal: `python3 validate_inputs_with_comments.py`