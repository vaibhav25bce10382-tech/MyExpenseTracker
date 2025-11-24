import json
import os
from tracker.models import Expense

DATA_FILE = "data.json"

def save_expenses(expense_list):
   
    data = [exp.to_dict() for exp in expense_list]
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def load_expenses():
    
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
    except (IOError, json.JSONDecodeError):
        return []
