# Import the element tree class from the `xml.etree.ElementTree` module.
import xml.etree.ElementTree as ET
# Define the file path - the tree
file_path = "groceries.xml"
# Call the `.parse()` func to parse the tree. 
tree = ET.parse(file_path)
# `tree.getroot()` is called to get the root of the tree`.
root = tree.getroot()
# Print out all grocery items that have prices higher than six
# Save an empty list in the variable on the left.
items_over_six = []

# Iterate through each grocery item from the root.
for item in root.findall("grocery_item"):
    # The name is extracted by calling `item.find()` passing a `name` as a str followed by `.text`
    name = item.find("name").text
    # Same thing is done for the 'price' data.
    price = item.find("price").text
    # func to convert the price into a decimal before comparing it with six because with XML files all values are represented as strings
    if float(price) > 6.00:
            # So prices is a string and needs to be converted to a number.
            items_over_six.append(name)
    # name and price is printed out.
    print(name, price)

    # Print statement to display the final list.
    print("items with price higher than 6.00:", items_over_six)