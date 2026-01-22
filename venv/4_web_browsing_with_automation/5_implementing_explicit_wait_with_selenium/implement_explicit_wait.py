# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# 'WebDriverWaitSu' supports Selenium's explicit waiting strategy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# define url
url = "https://the-internet.herokuapp.com/dynamic_controls"

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# define a wait. WebDriver will wait 10 seconds for the condition to be met before executing the next step in the program.
wait = WebDriverWait(driver, 10)

# find the Enable button. An explicit wait is used to wait until the Enable button is clickable before finding it.
enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
# click the Enable button
enable_button.click()
sleep(3)

# find the disable button. An explicit wait is used to wait until the Disable button is clickable before finding it.
disable_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
# click the Disable button
disable_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the Remove button. An explicit wait is used to wait until the Remove button is clickable before finding it.
remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
# click the Remove button
remove_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the Add button. An explicit wait is used to wait until the Add button is clickable before finding it.
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
# click the Add button
add_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the checkbox. An explicit wait is used to wait until the checkbox is clickable before finding it. 
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox"]')))
# click the checkbox
checkbox.click()
# After each element is interacted with, pause the program execution for 3 seconds to view the result
sleep(3)

# close the browser and quit the webdriver
driver.quit()