# scrape_multiple_pages

```python
# The below url works in a website browser.
url = "https://www.feedbooks.com/publicdomain/browse/top?lang=en&page="+str(page_number)
```

The goal is to build a web scraper that collects all the book titles and authors displayed from the Page Number, Book Titles, Book Authors from the first, second, and third pages of this website.

## Testing

Run the program with: `python3 scrape_multiple_pages.py`

#### Results

```python
# Prompt and my cmd script to run the program
Mac:scrap_multiple_pages vanessatsanguk$ python3 scrape_multiple_pages.py

Page Number: 1

Book Titles: ['Anne Of Green Gables Complete 8 Book Set', 'Humor Me', 'The Count of Monte Cristo', 'The Hitch', 'Anatomy of an Alibi', "Hans Christian Andersen's Complete Fairy Tales", 'The Work of Our Hands', "The New Rules of Women's Health", 'Detour', 'Peter Pan', 'Homeschooled', 'The First Time I Saw Him (A Reese Witherspoon Book Club Pick)', 'Black Bear', 'The Storm', 'The First Time I Saw Him (A Reese Witherspoon Book Club Pick)', "But I'm Bored!", 'Beyond Infidelity', 'The Singles Tax', '1984', 'Lost Lambs', "The Devil's Daughter", 'Dauntless [Dramatized Adaptation]', 'Cheater Slicks', 'Far from the Madding Crowd', 'Commercial Real Estate Investing', 'The Healthy Kidney Handbook', 'Chagos Archipelago', "Sheriff's Bad Bear", 'Fifty Percent of Mountaineering is Uphill', 'Rogue Zero (An Agent Zero Spy Thriller—Book #16)', 'Patriots Before Revolution', 'Stat', 'Big Bad', 'How to Do Discourse Analysis', "Turing's Vision", 'Ivy Touched and Bronze Blade', 'Black Rose and Gold Queen', 'Angel Investing, Revised & Updated', 'Ogre on Patrol', 'Bound to Punish', 'Holding Change', 'Behold Your Queen!', 'The 1% Good Club', 'Leverage', "I'm Still Here", 'Vultures', 'For Richer For Poorer', 'The Adversary', 'Hidden Guests', 'On the Edge']

Book Authors: ['L. M. Montgomery', 'Chris Duffy', 'Alexandre Dumas', 'Sara Levine', 'Ashley Elston', 'Hans Christian Andersen', 'Adrian Sutherland', 'Meghan Rabbitt', 'Jeff Rake', 'J. M. Barrie', 'Stefan Merrill Block', 'Laura Dave', 'Trina Moyles', 'Rachel Hawkins', 'Laura Dave', 'Lizzie Assa', 'Lauren LaRusso', 'Renée Sylvestre-Williams', 'George Orwell', 'Madeline Cash', 'Danielle Steel', 'Jack Campbell', 'Hailey Edwards', 'Thomas Hardy', 'Randall Zisler, PhD', 'C. Nicole Swiner, M.D.', 'Tom Lutz', 'Kati Wilde', 'Susanna Pfisterer', 'Jack Mars', 'Amy Watson', 'Iesha Bree', 'Queenie Wise', 'James Paul Gee', 'Alessio Plebe', 'Shannon Mayer', 'Shannon Mayer', 'David S. Rose', 'Ava Ross', 'J. L. Beck', 'adrienne maree brown', 'Gladys Malvern', 'Cooper Chapman', 'Mark Dawson', 'Hilary Bonner', 'Mark Dawson', 'Danielle Steel', 'Brian Andrews', 'Lise Barnéoud', 'Kate Horan']

Page Number: 2

Book Titles: ['Anne Of Green Gables Complete 8 Book Set', 'Humor Me', 'The Hitch', 'Anatomy of an Alibi', 'The Count of Monte Cristo', "Hans Christian Andersen's Complete Fairy Tales", 'The Work of Our Hands', 'Detour', "The New Rules of Women's Health", 'Peter Pan', 'Homeschooled', 'The First Time I Saw Him (A Reese Witherspoon Book Club Pick)', 'Black Bear', 'The Storm', 'The First Time I Saw Him (A Reese Witherspoon Book Club Pick)', "But I'm Bored!", 'The Singles Tax', 'Beyond Infidelity', 'Lost Lambs', '1984', "The Devil's Daughter", 'Big Bad', 'Chagos Archipelago', 'Patriots Before Revolution', 'The Healthy Kidney Handbook', 'Rogue Zero (An Agent Zero Spy Thriller—Book #16)', 'Fifty Percent of Mountaineering is Uphill', "Sheriff's Bad Bear", 'Stat', 'Commercial Real Estate Investing', 'Far from the Madding Crowd', 'Dauntless [Dramatized Adaptation]', 'Cheater Slicks', 'Bound to Punish', 'How to Do Discourse Analysis', "Turing's Vision", 'Ogre on Patrol', 'Ivy Touched and Bronze Blade', 'Black Rose and Gold Queen', 'Angel Investing, Revised & Updated', 'Holding Change', 'Marriage is a Shore Thing', 'Undercover Shadow', 'Leverage', 'The Adventuress of Albany', "I'm Still Here", 'For Richer For Poorer', 'Vultures', 'Hungry Hill', 'The 1% Good Club']

Book Authors: ['L. M. Montgomery', 'Chris Duffy', 'Sara Levine', 'Ashley Elston', 'Alexandre Dumas', 'Hans Christian Andersen', 'Adrian Sutherland', 'Jeff Rake', 'Meghan Rabbitt', 'J. M. Barrie', 'Stefan Merrill Block', 'Laura Dave', 'Trina Moyles', 'Rachel Hawkins', 'Laura Dave', 'Lizzie Assa', 'Renée Sylvestre-Williams', 'Lauren LaRusso', 'Madeline Cash', 'George Orwell', 'Danielle Steel', 'Queenie Wise', 'Tom Lutz', 'Amy Watson', 'C. Nicole Swiner, M.D.', 'Jack Mars', 'Susanna Pfisterer', 'Kati Wilde', 'Iesha Bree', 'Randall Zisler, PhD', 'Thomas Hardy', 'Jack Campbell', 'Hailey Edwards', 'J. L. Beck', 'James Paul Gee', 'Alessio Plebe', 'Ava Ross', 'Shannon Mayer', 'Shannon Mayer', 'David S. Rose', 'adrienne maree brown', 'Laura Langa', 'Heather Slade', 'Mark Dawson', 'Darry Fraser', 'Hilary Bonner', 'Danielle Steel', 'Mark Dawson', 'Daphne Du Maurier', 'Cooper Chapman']

Page Number: 3

Book Titles: ['Anne Of Green Gables Complete 8 Book Set', 'Humor Me', 'The Count of Monte Cristo', 'The Hitch', 'Anatomy of an Alibi', "Hans Christian Andersen's Complete Fairy Tales", 'The Work of Our Hands', "The New Rules of Women's Health", 'Detour', 'Peter Pan', 'Homeschooled', 'The First Time I Saw Him (A Reese Witherspoon Book Club Pick)', 'Black Bear', 'The Storm', 'The First Time I Saw Him (A Reese Witherspoon Book Club Pick)', "But I'm Bored!", 'Beyond Infidelity', 'The Singles Tax', '1984', 'Lost Lambs', "The Devil's Daughter", 'Dauntless [Dramatized Adaptation]', 'Cheater Slicks', 'Far from the Madding Crowd', 'Commercial Real Estate Investing', 'The Healthy Kidney Handbook', 'Chagos Archipelago', "Sheriff's Bad Bear", 'Fifty Percent of Mountaineering is Uphill', 'Rogue Zero (An Agent Zero Spy Thriller—Book #16)', 'Patriots Before Revolution', 'Stat', 'Big Bad', 'How to Do Discourse Analysis', "Turing's Vision", 'Ivy Touched and Bronze Blade', 'Black Rose and Gold Queen', 'Angel Investing, Revised & Updated', 'Ogre on Patrol', 'Bound to Punish', 'Holding Change', 'Behold Your Queen!', 'The 1% Good Club', 'Leverage', "I'm Still Here", 'Vultures', 'For Richer For Poorer', 'The Adversary', 'Hidden Guests', 'On the Edge']

Book Authors: ['L. M. Montgomery', 'Chris Duffy', 'Alexandre Dumas', 'Sara Levine', 'Ashley Elston', 'Hans Christian Andersen', 'Adrian Sutherland', 'Meghan Rabbitt', 'Jeff Rake', 'J. M. Barrie', 'Stefan Merrill Block', 'Laura Dave', 'Trina Moyles', 'Rachel Hawkins', 'Laura Dave', 'Lizzie Assa', 'Lauren LaRusso', 'Renée Sylvestre-Williams', 'George Orwell', 'Madeline Cash', 'Danielle Steel', 'Jack Campbell', 'Hailey Edwards', 'Thomas Hardy', 'Randall Zisler, PhD', 'C. Nicole Swiner, M.D.', 'Tom Lutz', 'Kati Wilde', 'Susanna Pfisterer', 'Jack Mars', 'Amy Watson', 'Iesha Bree', 'Queenie Wise', 'James Paul Gee', 'Alessio Plebe', 'Shannon Mayer', 'Shannon Mayer', 'David S. Rose', 'Ava Ross', 'J. L. Beck', 'adrienne maree brown', 'Gladys Malvern', 'Cooper Chapman', 'Mark Dawson', 'Hilary Bonner', 'Mark Dawson', 'Danielle Steel', 'Brian Andrews', 'Lise Barnéoud', 'Kate Horan']
# Execution successfully completed and back to prompt
Mac:scrap_multiple_pages vanessatsanguk$
```

I have been able to scrap pages 1, 2, and 3 from the above website.
