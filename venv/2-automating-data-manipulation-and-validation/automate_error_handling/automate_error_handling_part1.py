# Try-Accept Block to catch possible runtime errors, also known as exceptions.
# Handle errors gracefully, use a try-except block.
# The goal of this program is to get the user to input a number and perform a calculation with that number.
try:
    # User must enter an integer number.
    number = int(input("Enter a number: "))
    # Divide that number by 10
    result = 10 / number
    # Print the result of the above division.
    print("The result is:",result)
except ValueError:
    # This str will print if user enters a char that is not a number.
    print("You must enter a valid integer.")
except ZeroDivisionError:
    # This str will print if user enter zero.
    print("You cannot divide by zero.")