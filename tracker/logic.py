from tracker.storage import load_expenses, save_expenses
from tracker.models import Expense

def add_new_expense(description, category, amount):
   
    expenses = load_expenses()
    new_expense = Expense(description, category, amount)
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense for '{description}' added.")

def list_expenses():
  
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 70)
    
    for index, exp in enumerate(expenses, start=1):
        print(f"{index:<5} | {exp.date:<12} | {exp.category:<15} | ${exp.amount:<9.2f} | {exp.description}")

def delete_expense_by_index(index):
   
    expenses = load_expenses()
    real_index = index - 1
    
    if 0 <= real_index < len(expenses):
        removed = expenses.pop(real_index)
        save_expenses(expenses)
        return True
    return False
