# 4_explore_waiting_strategies_with_selenium

There are two main types of waiting strategies that Selenium offers:

1. Pause until a set condition is met.
2. Pause execution until elements are available, up to a set time limit.

Most modern day websites use asynchronous techniques such as Ajax to load their webpages. This allows web servers to update parts of the webpage without reloading the entire thing. Because of this, they're able to create fast loading and dynamic webpages. However, this becomes a problem when a Selenium web driver tries to locate a web element before it's loaded. This will raise an 'exception'. Typically, an element not visible exception, and your program will not work. And this leads into why waiting strategies are important. Waiting strategies can add crucial time intervals in between actions performed, thus allowing the web driver to wait until an element is loaded before it interacts with it.

There are two main types of waiting strategies that Selenium offers. Explicit and implicit. Explicit waits, when paired with a specific condition, will wait until that condition is met before executing. On the other hand, implicit waits when paired with a specific amount of time will wait that long for the element to become available before executing.

## Selenium with Python

A powerful combination for automating web browser testing and interactions. It allows you to control a browser programmatically, enabling test automation across multiple browsers (Chrome, Firefox, Edge, Safari) and platforms.

[Selenium Python Tutorial (with Example)](https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test)
