# 2_make_api_requests_in_python

Begin weaving real-time data into our Python applications/projects.
API request we make opens a door to a world of dynamic data. We use it to innovate, solve problems, and make informed decisions.

We are developing an e-commerce platform and you need up-to-date information on thousands of products from prices to descriptions. How do you access all this data efficiently and accurately? The key lies in mastering API requests. The first step of using an API in Python is to make a request.

1. Demonstrate API requests.
2. Utilise [upcitemdb.com's API](https://upcitemdb.com/)

Demonstrate how to make an API request, using the free API provided by upcitemdb.com. Your goal is to make a request to the upcitemdb API to get data about a specific product.

For this example, the product will be a [bottle of lemonade with raspberry](https://upcitemdb.com/upc/025000044908), which has a UPC or universal product code of 025000044908.

[Lookup by HTTP GET](https://upcitemdb.com/api/explorer#!/lookup/get_trial_lookup)

Go ahead and enter this UPC into the box and click Try to look up the HTTP get request URL for this product.

Request URL: https://api.upcitemdb.com/prod/trial/lookup

Now copy the request URL until lookup. Now open up make API requests starter code.py in VS Code. First, import the request library. Next, define the base URL, paste in the URL that you previously copied. Then define the parameters. Assign it to a dictionary that maps UPC to the UPC code for the lemonade as a string. Afterwards call request.get pass in base URL and set the params argument equal to parameters. Lastly, print the URL from the response.

## Testing

Now save and run the program: `python3 make_api_requests.py`

The API response URL for the lemonade with raspberry product has been [printed out](./url_printed_in_terminal.png). Now copy this URL and paste it into your browser. This shows all of the [information for this product](./info_for_the_product_from_url_in_browser.png). So <mark>the API request worked</mark>.

Begin weaving real-time data into our applications or projects. Remember each API request we make opens a door to a world of dynamic data. Use it to innovate, solve problems, and make informed decisions.
