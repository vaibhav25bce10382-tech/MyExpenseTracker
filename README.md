# My Wallet Manager

**Author:** [vaibhav murty]
**Language:** Python 3.13.7

## Description
A modular expense tracker built for the "Build Your Own Project" course.

## How it works
The program lets users add daily expenses (like "Lunch" or "Bus Ticket") and saves them to a file on the computer (data.json). This way, the data isn't lost when I close the program. It can also calculate how much I have spent in total for specific categories.

##Technical details
I used a modular approach to keep the code clean:
.main.py: Handles the user menu.
.tracker/: A folder containing the logic.
.models.py: Defines what an "Expense" looks like in code.
.storage.py: Handles reading/writing to the JSON file.


## How to Run
1. Download the code.
2. Run `python main.py`.
3. Follow the on-screen menu instructions.
