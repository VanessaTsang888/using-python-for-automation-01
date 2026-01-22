# 3_automate_drag_and_drop_functionality

Acquire the skills for automating drag and drop functionality in Python with Selenium.

Test site: [DHTML Goodies.com](http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html)
This site is no long available.

Test site: [Dragula](https://bevacqua.github.io/dragula/)
Dragula is the closest match to DHTML Goodies.

Code File: automate_drag_and_drop.py

## How in Detail

Another common browser interaction is drag and drop. Drag and drop allows users to move items from one part of a webpage to another part, and even move items between different applications. We'll acquire the skills for <mark>automating drag and drop functionality in Python with Selenium</mark>.

The above demo website for testing out automated drag and drop browser interactions. Our eventual goal is to build automation for dragging the capital tiles and dropping them into the respective country tiles. To start out, you'd like to automate dragging the Washington tile and dropping it into the United States tile. Copy the URL and open up 'automate_drag_and_drop.py' in VS Code.

The necessary libraries have been imported at the top. We are using the Chrome browser, so I've imported the web driver specific to Chrome. If you're using a different browser, we'll need to adjust the second and third import statements to suit your browser.

Paste in the URL from the website to define the URL variable as a string. The driver has been instantiated, the window has been maximized, and the URL has been passed to the driver. The next step is to define the source and the destination. The source should be Washington. To find this element, go back to the webpage and use the Inspect tool to get the 'XPath' from the HTML code. The corresponding destination should be United States. Get the 'XPath' for this element using Inspect again.

Then, action chains is used to perform the drag and drop. Specifically, the source is moved to the destination. There's a call to the sleep function for five seconds, just so that you can see the results of the automation when testing it out. Lastly, 'driver.quit' is called to close out the browser that was opened for this automated testing.

## Testing

`python3 automate_drag_and_drop.py`

### Results - Output

Below output is from running the program in the terminal. The string/plain text is from the 'input' function at the end of the program which is a message for the user to take action.

```python
# Cmd script to run the program
Mac:3_automate_drag_and_drop_functionality vanessatsanguk$ python3 automate_drag_and_drop.py
# Program running. Hit the 'Enter' key to close the browser from the manual wait function.
Press Enter to close the browser...
# Program ended and back to prompt.
Mac:3_automate_drag_and_drop_functionality vanessatsanguk$
```
