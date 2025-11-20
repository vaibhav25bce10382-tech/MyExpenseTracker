import json
import os
from tracker.models import Expense

# Define the filename for data persistence
DATA_FILE = "data.json"

def save_expenses(expense_list):
    """
    Writes the list of Expense objects to a JSON file.
    Satisfies 'Data Input & Processing' requirement.
    """
    # Convert list of objects to list of dictionaries
    data = [exp.to_dict() for exp in expense_list]
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def load_expenses():
    """
    Reads from JSON file and returns a list of Expense objects.
    """
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            # Convert list of dictionaries back to Expense objects
            return [Expense.from_dict(item) for item in data]
    except (IOError, json.JSONDecodeError):
        # If file is corrupt or empty, return empty list
        return []