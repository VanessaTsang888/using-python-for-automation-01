# inspect-your-data-source

The url for the book site don't work: [feedbooks](https://www.feedbooks.com/search?cat=FBFIC016000&query=feedbooks). According to Claud AI, this is the new URL for the same websiteL https://market.feedbooks.com/

SUMMARY

1. Page examination.
2. Pinpoint data.
3. Set the stage for scraping.

Pull back the curtain and see what makes up the websites you're interested in collecting data from. Before diving in, to gather data from a webpage, you'll need to meticulously review its HTML structure and identify the elements you want to extract as a foundation for your future analysis and automation.

We'll gain the expertise to examine a page, pinpoint the data treasures you seek and set the stage for successful scraping adventures.

Here I have the following webpage open. This contains a public catalog of books that are in English and categorized as humorous, and I'll use the browser's Inspect tool to explore its HTML structure. Right click while on the webpage, and then click Inspect. You'll see the structure of the HTML document pop open on the right. Now, try to locate the data corresponding to the first book within the HTML code. Start by clicking on the section tag where class equals browse content. Next, click on the div tag where class equals browse items, browse items grid. Then click on the first div tag where class equals browse item. Afterwards click on the first div tag where class equals B item grid. When you hover over B item grid in the HTML code, you'll notice that the first book is highlighted in the webpage. Nested inside of this, there's B item cover, which represents the book cover and contains the image. Block item title, which represents the book's title. Block item author, which represents the book's author and block item price, which represents the book's price. These are all types of data that you could potentially scrape from this data source. Now that you've uncovered how to inspect a data source, go ahead and try using the inspect tool in your browser to examine the HTML structure of a different webpage.
