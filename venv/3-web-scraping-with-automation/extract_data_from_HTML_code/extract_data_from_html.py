# Scrap the below website to receive the book title for all x50 books on the webpage. 
# Use Selenium to scrape this website content as it is dynamically loaded by JavaScript.
# Import the main webdriver module to control the browser
from selenium import webdriver
# Import By class to specify different locator strategies (e.g., CLASS_NAME, ID, XPATH)
from selenium.webdriver.common.by import By
# Import WebDriverWait to enable explicit waits for elements to load
from selenium.webdriver.support.ui import WebDriverWait
# Import expected_conditions module to define conditions for WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the URL
    url = "https://market.feedbooks.com/"
    # Set up the Chrome driver
    driver.get(url)
    
    # Wait for the book titles to load (wait up to 10 seconds)
    wait = WebDriverWait(driver, 10)
    # Wait until all elements with class name "block__item-title" are present in the DOM and retrieve them.
    titles = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "block__item-title")))

    # Get only the first 10 titles
    # first_10_titles = titles[:10]
    
    # Display the total number of titles found.
    print(f"Number of titles found: {len(titles)}")
    print("\nBook Titles:")
    # Str multiplication operation that creates a string consisting of the dash character ("-") repeated 50 times
    print("-" * 50)
    
    # Print each title
    # for i, title in enumerate(titles, 1):
    # Print first x10 only
    # for i, title in enumerate(first_10_titles, 1): 
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.text}")
    
finally:
    # Always close the browser, even if there's an error
    driver.quit()