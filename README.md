.My Wallet Manager (Expense Tracker)
.Submitted by: Vaibhav Murty
.Course: CSE1021
.Project Overview
This is a Python-based command-line tool that helps me track where my money goes. I built this because I often forget small expenses like snacks or transport, and I wanted a way to log them quickly without needing internet access.
.How It Works
The program lets users add daily expenses (like "Lunch" or "Bus Ticket") and saves them to a file on the computer (data.json). This way, the data isn't lost when I close the program. It can also calculate how much I have spent in total for specific categories.
.Key Features
Add Data: Quick entry of description, category, and cost.
Save Data: Uses the json library to save records permanently.
Reports: Shows a table of spending per category.
Error Checking: Prevents entering negative numbers or empty text.
.Technical details
I used a modular approach to keep the code clean:
main.py: Handles the user menu.
tracker/: A folder containing the logic.
models.py: Defines what an "Expense" looks like in code.
storage.py: Handles reading/writing to the JSON file.
.How to Run
Open this folder in the terminal.
Type python main.py to start the application.
