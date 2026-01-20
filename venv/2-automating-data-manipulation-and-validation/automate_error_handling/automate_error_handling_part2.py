# Use an assert statement to check for a logical error.
# By using try-except blocks and appropriately handling exceptions in our code, you can prevent unexpected errors, improve the reliability of your code and provide a better experience for your users. Implement try-except blocks and assert statements to automate error handling in our own Python code.

# years is defined as a list of numbers, and the goal is to sort the years in place.
years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
# We accidentally used the wrong method as this method reverses the order of the elements in a list.
# years.reverse()
years.sort()
# Years is printed out and there's an assert statement to check the logic of the code.
print(years)
# Assert state to check the logic of the code.
# Specifically, it checks if the first element is less than or equal to the last element in the updated list. 
# Use an assert statement and print the below error msg.
assert years[0] <= years[-1], "First element is greater than last element."