# Extract Data From HTML code

File: extract_data_from_html.py

Assume that you've already created a request to get HTML code from this webpage and parsed the response. So our next goal is to extract data from the parsed HTML response. Specifically, you'd like to find all the book titles that appear on this webpage and print them out.

Scrap data from this website: "https://www.feedbooks.com/search?cat=FBFIC016000&query=feedbooks" which according to my research has changed to: https://market.feedbooks.com/

Target site / selector is the same meaning this new url should work.

## The Bug

Execute this file to run the program and print the results to the Terminal: `python3 extract_data_from_html.py`

<mark>Problem</mark>
I used the above script to run the program and no response have been returned and I don't receive any error msg.

I used [Claude AI](https://claude.ai/share/1fc52ac9-b9e2-4795-962e-ccf80dd044b8) to help me diagnose the problem and found out that the 'book titles' are dynamically loaded by JavaScript. This means I need to use the Selenium framework to scrape the website.

Here's What's Actually Happening:
When you open the page in your browser and inspect it, you see the book titles in the HTML. BUT when `requests.get()` fetches the same URL, it gets a different or incomplete version of the HTML - one without the book titles loaded yet.
Why This Happens:

JavaScript renders the content: The server sends basic HTML, then JavaScript loads the book data and adds it to the page
Browser vs requests: Your browser executes JavaScript and waits for content to load. `requests` just grabs the initial HTML and stops - no JavaScript execution.

**_Proof Test_**:
Run this to see what HTML `requests` is actually getting:

```python
import requests
from bs4 import BeautifulSoup

url = "https://market.feedbooks.com/"
response = requests.get(url, headers={
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
})

# Save what requests actually receives
with open("requests_html.html", "w", encoding="utf-8") as f:
    f.write(response.text)

# Check if the class exists in the HTML
if "block__item-title" in response.text:
    print("✓ The class exists in the HTML from requests")
else:
    print("✗ The class does NOT exist - content is loaded by JavaScript")

parsed_response = BeautifulSoup(response.text, "html.parser")
titles = parsed_response.find_all("a", class_="block__item-title")
print(f"Titles found: {len(titles)}")
```

If it prints "✗ The class does NOT exist", that confirms the content is dynamically loaded by JavaScript, and you must use Selenium to scrape this website.
Open the saved `requests_html.html` file in a text editor and search for "block\_\_item-title" - I bet you won't find it!

### the complete code using Selenium to scrape the book titles

This comment explains that the line is waiting for all book title elements to be loaded on the page and then storing them in the `titles` variable.

```python
    # Wait until all elements with class name "block__item-title" are present in the DOM and retrieve them.
    titles = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "block__item-title")))
```

```python
# Using Selenium to scrape all the book titles.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the URL
    url = "https://market.feedbooks.com/"
    driver.get(url)

    # Wait for the book titles to load (wait up to 10 seconds)
    wait = WebDriverWait(driver, 10)
    # Wait until all elements with class name "block__item-title" are present in the DOM and retrieve them.
    titles = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "block__item-title")))

    print(f"Number of titles found: {len(titles)}")
    print("\nBook Titles:")
    print("-" * 50)

    # Print each title
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.text}")

finally:
    # Always close the browser, even if there's an error
    driver.quit()
```

This is a string multiplication operation that creates a string consisting of the dash character ("-") repeated 50 times, resulting in "--------------------------------------------------". This 50-character string is what gets passed to and printed by the print() function, typically used as a visual separator or divider in the output.

```python
    # Str multiplication operation that creates a string consisting of the dash character ("-") repeated 50 times.
    print("-" * 50)
```

Output:

```plain text
Book Titles:
--------------------------------------------------
```

#### Results

I ran the program again with `python3 extract_data_from_html.py` and this time it work with the new code as above because I managed to get all x50 book titles as I've request with the python code - see below.

```html
(using-python-for-automation-1) Mac:extract_data_from_HTML_code vanessatsanguk$
python3 extract_data_from_html.py Error sending stats to Plausible: error
sending request for url (https://plausible.io/api/event) Number of titles found:
50 Book Titles: -------------------------------------------------- 1. La fièvre
du SOCCER Tome 3 2. I, Medusa 3. Claude Monet 4. Yesterday Once More 5. Grave
Descend 6. Sherlock Holmes: The Complete Collection 7. The Count of Monte Cristo
8. The Secret of Secrets 9. Bury Our Bones in the Midnight Soil 10. Mate 11. The
Perfect Son 12. The Locked Door 13. All the Light We Cannot See 14. Not My
Daughter 15. MINI Hockey #4 16. Complo-Sophisme 17. Whistle 18. Wild Dark Shore
19. Persuasion 20. The Burning Library 21. One by One 22. MINI Star Miaou Tome 4
23. Great Big Beautiful Life: Reese's Book Club 24. The Intruder 25. Die With
Zero 26. Oliver Twist 27. The Emperor of Gladness: Oprah's Book Club 28. It's
Not Summer Without You 29. False Witness 30. Hans Christian Andersen's Complete
Fairy Tales 31. The Housemaid 32. The Widow 33. Holiday Ever After 34. The Black
Wolf 35. My body, my rights! 36. The King's Ransom 37. Wuthering Heights 38. The
Strawberry Patch Pancake House 39. A Slowly Dying Cause 40. Haven't Killed in
Years 41. Some Kind of Famous 42. We'll Always Have Summer 43. Wild Animal 44.
The Let Them Theory 45. Habs Nation 46. Project Hail Mary 47. Far from the
Madding Crowd 48. How Girls Are Made 49. The Gingerbread Bakery 50. House of
Day, House of Night (using-python-for-automation-1)
Mac:extract_data_from_HTML_code vanessatsanguk$
```

To receive the first x10 book titles rather than all x50, I used this code from Claud AI:

```python
(using-python-for-automation-1) Mac:extract_data_from_HTML_code vanessatsanguk$ python3 extract_data_from_html.py
Number of titles found: 50

Book Titles:
--------------------------------------------------
1. La fièvre du SOCCER Tome 3
2. I, Medusa
3. Claude Monet
4. Yesterday Once More
5. Grave Descend
6. Sherlock Holmes: The Complete Collection
7. The Count of Monte Cristo
8. The Secret of Secrets
9. Bury Our Bones in the Midnight Soil
10. Mate
```
