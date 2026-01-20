# Data: a string that contains the groceries info.
file_path = "groceries.txt"

# `with` statement to open the txt file.
with open(file_path, "r") as file:
    # Read the data from file.
    data = file.read()
# Print the data.    
print("data:", data)
# To parse the data, the '.split()' func is called to split the string of grocery data into a list, so each grocery item can be accessed individually.
parsed_data = data.split(", ")
# Print out the parsed data.
print("parsed data:", parsed_data)
# To access grocery item at index 2, index the list and print and print it out.
print("item at index 2:", parsed_data[2]) # carrots is printed out in Terminal.