# Using Chrome browser for testing
# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# define url. Define the url variable as a Str.
url = "https://bevacqua.github.io/dragula/"

# instantiate webdriver and open a chrome browser.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# Load the webpage. The URL has been passed to the driver.
driver.get(url)

# find the source -- in this example, the Washington title
source = driver.find_element(By.XPATH, '//*[@id="left-defaults"]/div[1]')

# find the destination -- in this example, the United States title
destination = driver.find_element(By.XPATH, '//*[@id="right-defaults"]/div[3]')

# instantiate ActionChains. Action chains is used to perform the drag and drop.
actions = ActionChains(driver)

# perform the drag and drop -- dragging the source and dropping it into the destination
actions.drag_and_drop(source, destination).perform()

# pause the program for 15 seconds just to view the results
sleep(15)

# close the browser window and quit the driver
# driver.quit()

# in the terminal, hit the Enter key to close the browser.
input("Press Enter to close the browser...")
