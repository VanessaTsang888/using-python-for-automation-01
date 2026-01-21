# 2_automate_basic_browser_interactions

Delegate all those tedious, repetitive online tasks to our Python scripts. Clicking buttons, typing into forms, navigating pages are now all automated. We'll be exploring how to use Selenium to automate basic browser interactions in Python.

1. Explore Selenium basics
2. Automate browser interactions.
3. Python integration.

Dummy website for web automation testing. Our goal is to build automation testing for filling in this web form.
[Lambdatest Playground](https://ecommerce-playground.lambdatest.io/index.php?route=account/register)
Python code file: automate_basic_browser_code.py

This is a dummy website for web automation testing. Your goal is to build automation for filling in this web form. Copy the URL and open up automate_basic_browser_starter_code.py in VS code. Some of the code has already been provided in the exercise file. As you follow along in this demo, you'll be replacing the placeholders to complete the code. The necessary libraries have been imported at the top. Note that I'm using the Chrome browser, so I've imported the web driver specific to Chrome. If you're using a different browser, you'll need to adjust the second and third import statements to suit your browser. Paste the URL from the web form to define the URL variable as a stream. The driver has been instantiated, the window has been maximized, and the URL has been passed to the driver. The next step is to go through each field that needs to be filled out in the web form and make the driver find the element associated with each field. The Inspect browser tool will come in handy here. Let's start with the First Name field. Go to the web form, right click while on the First Name field and click Inspect. Right click on the HTML code that appears in the side panel and click Copy, then Copy XPath. Then paste the XPath to replace the placeholder for the second argument in the call to driver.find_element in the code. Afterwards, first_name.send_keys is called. Type out the text you want to fill in the First Name field with. Do this for the Last Name, Email, Telephone, Password and Password Confirm fields. For the Newsletter Subscribe field, right click on the label for the No, click Inspect, right click on the HTML code for this label and click Copy and then Copy XPath. Paste the XPath to replace the placeholder for the second argument in the call to driver.find_element in your code. Afterwards, newsletter_subscribe.click is called so that the element is clicked in the automation. Do this for the Agree field as well. Finally, there's the Continue button that has to be clicked for the completed form to be submitted. Use the Inspect tool again to copy the XPath for this button and paste it into the program. After this button is clicked in the automation, the window is scrolled down by 200 units. There's a call to the Sleep function for five seconds, just so that you can see the results of the automation when testing it out. Lastly, driver.quit is called to close out the browser that was opened for this automated testing. Save and run the program and check out the results for yourself. There. The program automatically filled out all of the input fields in the web form using the data you specified and submitted the form. Now go ahead and try automating the process of filling out another web form using Selenium in Python.

## Testing

Save and run program and check out the results. The program automatically filled out all of the input fields in the web form using the data you specified and submitted the form.

Save and run the program and check out the results for yourself.
Run the progrm with: `python3 automate_basic_browser_code.py`

### Results

The program automatically filled out all of the input fields in the web form using the data you specified and submitted the form. However, the `sleep(1000)` func to pause the program for 1000 seconds to view the results during testing was not enough. Therefore, on the top-left of the browser window I clicked the 'back' icon to navigate back to the previous page where the form is located and here I was able to get enough time to analyse the data in the inputs are as expected. Test passed - see my screenshot.

[Automate_basic_browser_interactions_test_passed](./automate_basic_browser_interactions_test_passed.png)
