# parse_data_with-python

1. Parsing data techniques
2. Extracting data with precision

## parse_data_part1.py

The data inside of 'groceries.txt' file:
A string that contains the groceries info.

### Steps

Parse data from 'groceries.txt' which contains grocery data with comma separating one item from the next. The first step is defining the file path, which is groceries.txt in this case.

`with` statement to open the file: '"groceries.txt"'

### The Code

To parse the data, the '.split()' func is called. This splits the string of grocery data into a list, so each grocery item can be accessed individually. The function splits every time it encounters a comma followed by a whitespace.

### To run the program

`python3 parse_data_part1.py`

Results recieved:

```python
data: apples, bananas, carrots, durians, eggplants, ginger, hazelnuts
parsed data: ['apples', 'bananas', 'carrots', 'durians', 'eggplants', 'ginger', 'hazelnuts']
# carrots is located in second location as Arrays is zero based.
item at index 2: carrots
```

As per 'groceries.csv', carrots is in second location. This file has two columns: grocery item and quanity.

## parse_data_part2.py

The data from file 'groceries.csv'.
Automate the task to print out each row of data in the Terminal.

### The Code

`with` statement and a for-loop.
The quanity in the second column must be converted in to an integer from a string. To do this utilise the `int` func and pass-in the row Array `row[1]` and Index location 1 is where the 'quanity value' lives as Arrays is zero based index.

### Testing

Run the program: `python3 parse_data_part2.py`

Results:
Each row of CSV file has been printed out.

```python
['apples', 2]
['bananas', 6]
['carrots', 4]
['durians', 3]
['eggplants', 5]
['ginger', 1]
['hazelnuts', 8]
```

## parse_data_part3.py

Parse data from the 'groceries.json' file which is a JSON file that maps grocery items to quantites.

The data is one single obj with x7 items > key-value-pair.

### Run the program

with: `python3 parse_data_part3.py`

#### Results

The test worked as expected as I did receive the below result in the Terminal as expected.

```python
# Column 2 is now an int not a str.
apples quantity: 2
```

## parse_data_part4_completed.py

<mark>Task 1: Print out all grocery items and its price.</mark>

'groceries.xml' is an XML file that represents a groceries list.
The elements of this XML file represent grocery items:

```xml
<grocery_item>
    <name>Apples (per pound)</name>
     <price>1.50</price>
</grocery_item>
```

Each grocery item has a name and a price.

### The Code

Import the element tree class from the `xml.etree.ElementTree` module.
This class represents the XML data as a tree structure, where each node is an XML element.

#### Testing

Exectute `python3 parse_data_part4-with-comments.py`

Test pass as expected as the names of all the grocery items with its price have been printed out in the Terminal:

```plain text
Apples (per pound) 1.50
Bananas (per pound) 0.75
Oranges (per pound) 2.00
Plums (per pound) 1.80
Milk 2.49
Sour cream 1.79
Tortilla chips 2.49
Salsa 2.29
Carrots (per pound) 1.25
Broccoli (per pound) 2.50
Spinach (per bunch) 1.75
Avocados (per bag) 6.99
Cauliflower (per pound) 2.99
Blueberries (per pint) 3.99
Ketchup 1.49
Black beans (per can) 0.99
Bread 1.99
Cereal 3.29
Coffee (per pound) 7.99
Almonds (per pound) 6.99
Avocado Oil 14.49
Truffle Oil 18.99
Saffron (per gram) 15.99
```

<mark>Task 2: Print out all grocery items that have prices higher than six.</mark>

The Code:

1. Declare a variable named `items_over_six` that starts of as an empty list.
2. Inside of the existing for-loop add a statement that checks if the price is greater than 6, if so, append the name to the list. In the if-statement we need to call the float func to convert the price into a decimal before comparing it with six because with XML files all values are represented as strings. So prices is a string and needs to be converted to a number. This is why we pass-in the string `"price"` into the `float` func.
3. At the end add a print statement to display the final list.
4. Save our changes and run the program.

### Testing

Exectute `python3 parse_data_part4-with-comments.py`

Run the program again to test the program.

Results:

```python
# All grocery items that have a price greater than 6:
items with price higher than 6.00: ['Avocados (per bag)', 'Coffee (per pound)', 'Almonds (per pound)', 'Avocado Oil', 'Truffle Oil', 'Saffron (per gram)']
```

## Conclusion

Now we have the power to parse data with Python programming by implementing the above parsing techniques.
