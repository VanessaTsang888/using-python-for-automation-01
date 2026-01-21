# Using Chrome browser for testing
# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# define url. Define the url variable as a Str.
url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

# instantiate webdriver and open a chrome browser.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# Load the webpage. The URL has been passed to the driver.
driver.get(url)

# find the first name field 
first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
# fill out the first name field
first_name.send_keys("Jo")

# find the last name field 
last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
# find the last name field 
last_name.send_keys("Bloggs")

# find the email field 
email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
# fill in the email field 
email.send_keys("jo-bloggs@email.com")

# find the telephone field 
telephone = driver.find_element(By.XPATH, '//*[@id="input-telephone"]')
# fill in the telephone field 
telephone.send_keys("1234567891011")

# find the password field 
password = driver.find_element(By.XPATH, '//*[@id="input-password"]')
# fill in the password field 
password.send_keys("pw-888")

# find the password confirm field 
password_confirm = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')# fill in the password confirm field 
password_confirm.send_keys("pw-888")

# find the desired response to the newsletter subscribe field
newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/div[2]/label')
# click on it. Func is called so that the element is clicked in the automation. 
newsletter_subscribe.click()

# find the checkbox for agreeing to the terms 
agree = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div/label')
# click on the agree checkbox
agree.click()

# find the continue button
continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input')
# click on the continue button
continue_button.click()

# scroll down by 200 units to view the lower part of the page
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 1000 seconds to view the results during testing
sleep(10000)

# Func called to close the browser that was opened for this automated testing.
driver.quit()

# Save and run program and check out the results. The program automatically filled out all of the input fields in the web form using the data you specified and submitted the form.