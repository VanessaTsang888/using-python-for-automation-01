# Import the RegEx library.
## Call the `re.compile` function and pass in a regular expression for identifying phone numbers. 
### Example sentence to test out the regular expression.
#### Call `.search` on the regular expression and pass in the example sentence, saving the result in a variable.
##### If the result was populated, extract the 'phone number' from the result and then the 'area code' from the result.
##### To extract the phone number, call `result.group` funct.
##### The area code is the first three characters. So to extract the area code, slice with 'square brackets' passing in index `0``, colon, index `3``.
import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "The number is 123-456-7890."

result = phoneNumRegex.search(example)

if result:
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])