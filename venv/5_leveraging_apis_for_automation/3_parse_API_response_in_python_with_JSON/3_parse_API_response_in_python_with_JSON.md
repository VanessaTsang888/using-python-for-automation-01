# 3_parse_API_response_in_python_with_JSON

1. API parsing with JSON.
   Demonstrate how to parse API responses in Python with JSON.

Test site: [upcitemdb](https://upcitemdb.com/)

## The Goal

First product for this demo is 'Lemonade with Raspberry'.
The goal is to extract the title and brand of this product.

## In Detail

After making a request to an API, the next step is to parse the response. We'll demonstrate how to parse API responses in Python with JSON. The API I'll be using is the free API provided by [upcitemdb.com](https://upcitemdb.com/). Open up

The first product I'll use in my demo is lemonade with raspberry, with a UPC, or Universal Product Code, of 025000044908. The goal is to extract the title and brand of this product. The requests and JSON libraries have been imported, the base URL and the parameters have been defined, and the `requests.get` function has been called to make the API request. The next step is to parse the text from the API response using JSON Schema. So call the `json.loads` function, pass in `response.text`, and save the result in a variable named info. Then, extract the first item from info using the 'index 0'. Next, extract the product's title by indexing item, then extract the product's brand by indexing item. Print out the title and then the brand. Now, save and run the program to check out the result.

This time, I'll use Ridged Potato Chips, with a UPC, or Universal Product Code, of 028400516686. Make sure to save and run your program. There you go. The output shows that the second product's title is Ruffles Original Flavor Ridged Potato Chips, 8.5 ounces, and the brand is Ruffles. The next time you need to parse API Responses in Python, consider parsing with JSON Schema and try out the `json.loads` function.

### Testing

Now, save and run the program to check out the result. It worked. The output shows that the first product's title is Simply Lemonade with Raspberry Bottle, 52 fluid ounces, and the brand is Simply. Let's do this for another product for more practice.

Run the program with `python3 parse_api_responses.py`

### Results

x2 [product examples](./parsed_api_with_json.png) have been printed out in the Terminal as expected. First the 'Lemonade with Raspberry' and then the 'ridged potato chips'.
