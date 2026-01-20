# These libraries enable the script to download a webpage (`requests`) and then parse its HTML structure (`BeautifulSoup`) so you can extract specific information from it.
import requests
# Import BeautifulSoup 
from bs4 import BeautifulSoup

# Define the url
url = "https://www.feedbooks.com/search?cat=FBFIC016000&query=feedbooks"

# Send a request to get html code from that url
response = requests.get(url, headers={"Accept": "text/html"})

# Parse the response. Call BeautifulSoup func.
# The second argument tells Beautiful Soup to use Python's builtin HTML parser.
parsed_response = BeautifulSoup(response.text, "html.parser")

# Format the parsed HTML response in a way that’s easier to read and print it out.
print(parsed_response.prettify())

# Run the program: `python3 request_and_parse.py`