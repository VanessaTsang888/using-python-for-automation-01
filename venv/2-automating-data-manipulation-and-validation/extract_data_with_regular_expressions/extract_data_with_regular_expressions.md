# extract_data_with_regular_expressions

Regular expressions (regex) are powerful tools in Python that we can use to search, match and extract the data we need.

Regex enables efficient and flexible pattern matching for extracting and manipulating specific data from large and complex text sources.

Regular expressions are a coding structure that allow us to extract data using patterns in text.

## The Code

Call the `re.compile` function and pass in a regular expression for identifying phone numbers in the format of three digits, followed by a hyphen, followed by another three digits, followed by a hyphen, and four more digits. Start with `r`, followed by a string that contains the pattern for identifying phone numbers. Use \d to indicate each digit.

Create an example sentence to test out the regular expression. I've gone with the following sentence. The number is 123-456-7890.

Then call `.search` on the regular expression and pass in the example sentence, saving the result in a variable.

If the result was populated, which means a match was found, extract the phone number from the result and then the area code from the result.
To extract the phone number, call `result.group`.
Based on how the phone number is structured in the example string, let's assume that the area code is the first three characters. So to extract the area code, call `result.group`, and then slice with square brackets passing in index 0, colon, index 3.

Now, save and run your code. Based on the output, the phone number and the area code were extracted correctly. And with that, you now have the power to extract data with regular expressions in Python. Practice using the re library in Python to create regular expressions for other data extraction tasks.

### Testing

Save and run our code.
Execute this command script to run the program: `python3 extract_data_with_regex.py`.

#### Results

From the test the following data got printed out to the Terminal:

```python
# Output from the data extraction
Phone number found: 123-456-7890
Area code: 123
```

Based on the output the data has been extracted correctly. With this we have the power to extract data with RegEx in Python (and with the `re` library).
