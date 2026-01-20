# Import the JSON library
import json
# Define the file path
file_path = "groceries.json"
# `with` statement to open the JSON file for reading
with open(file_path, "r") as file:
    # Func to read the data in the file, save in variable on the left.
    data = file.read()
# To parse the data with JSON schema, `json.loads()` func is called, and the result is saved in the variable on the left. 
parsed_data = json.loads(data)
# Print the quantity associated with the apples grocery item.
print("apples quantity:", parsed_data["apples"]) # apples quantity: 2

## Run the program with: `python3 parse_data_part3.py` 
### Result:
### apples quantity: 2
### The test worked as expected as I did receive the above result in the Terminal as expected.