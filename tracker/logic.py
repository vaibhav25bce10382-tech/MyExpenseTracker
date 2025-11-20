from tracker.storage import load_expenses, save_expenses
from tracker.models import Expense

def add_new_expense(description, category, amount):
    """
    Creates a new expense and saves it.
    """
    expenses = load_expenses()
    new_expense = Expense(description, category, amount)
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense for '{description}' added.")

def list_expenses():
    """
    Prints all expenses to the console.
    """
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 70)
    
    # Enumerate allows us to show an ID (1, 2, 3...)
    for index, exp in enumerate(expenses, start=1):
        print(f"{index:<5} | {exp.date:<12} | {exp.category:<15} | ${exp.amount:<9.2f} | {exp.description}")

def delete_expense_by_index(index):
    """
    Deletes an expense based on the ID shown in the list.
    Satisfies 'CRUD Operations' requirement.
    """
    expenses = load_expenses()
    # Adjust index because list shows 1-based, but Python is 0-based
    real_index = index - 1
    
    if 0 <= real_index < len(expenses):
        removed = expenses.pop(real_index)
        save_expenses(expenses)
        return True
    return False