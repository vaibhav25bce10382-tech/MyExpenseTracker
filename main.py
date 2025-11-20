import sys
from .tracker.utills import print_header, get_valid_number, get_valid_string
from tracker.logic import add_new_expense, list_expenses, delete_expense_by_index
from tracker.analysis import show_category_summary

# I have customized the menu to look more unique
def show_menu_options():
    print("\nPlease choose an action:")
    print("[1] Log a new expense")
    print("[2] View my expense history")
    print("[3] See spending report (Category-wise)")
    print("[4] Remove an entry")
    print("[5] Exit App")

def main_menu():
    """
    Entry point for the Expense Manager.
    """
    while True:
        print_header("MY WALLET MANAGER") # Changed title
        show_menu_options()
        
        # Changed variable name from 'choice' to 'user_input'
        user_input = input("\nType option number: ")
        
        if user_input == '1':
            print("\n--- New Entry ---")
            # Changed prompt text to be less generic
            details = get_valid_string("What did you buy? (e.g., Pizza): ")
            ctype = get_valid_string("Which category? (e.g., Food): ")
            cost = get_valid_number("How much was it?: ")
            
            add_new_expense(details, ctype, cost)
            input("\nSaved! Press Enter to go back...")
            
        elif user_input == '2':
            print("\n--- History ---")
            list_expenses()
            input("\nPress Enter to go back...")
            
        elif user_input == '3':
            print("\n--- My Spending Analysis ---")
            show_category_summary()
            input("\nPress Enter to go back...")

        elif user_input == '4':
            print("\n--- Remove Entry ---")
            list_expenses()
            try:
                # Changed variable 'idx' to 'delete_id'
                delete_id = int(get_valid_number("ID of the item to remove: "))
                if delete_expense_by_index(delete_id):
                    print("Item removed from database.")
                else:
                    print("Error: I couldn't find that ID.")
            except ValueError:
                print("Please enter a valid ID number.")
            input("\nPress Enter to go back...")
            
        elif user_input == '5':
            print("Exiting... Have a good day!")
            sys.exit()
        else:
            print("That is not a valid option. Please try 1-5.")

if __name__ == "__main__":
    main_menu()