from tracker.storage import load_expenses

def show_category_summary():
   
    expenses = load_expenses()
    if not expenses:
        print("No data to analyze.")
        return

    summary = {}
    total_spent = 0

    for exp in expenses:
        if exp.category not in summary:
            summary[exp.category] = 0
        summary[exp.category] += exp.amount
        total_spent += exp.amount

    print(f"{'Category':<20} | {'Total Spent':<15}")
    print("-" * 40)
    
    for category, total in summary.items():
        print(f"{category:<20} | ${total:<15.2f}")
    
    print("-" * 40)
    print(f"{'GRAND TOTAL':<20} | ${total_spent:<15.2f}")
