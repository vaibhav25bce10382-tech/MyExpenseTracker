def print_header(title):
    """Prints a pretty header for the UI."""
    print("\n" + "=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)

def get_valid_number(prompt):
    """
    Repeatedly asks the user for input until a valid positive number is entered.
    Satisfies 'Error Handling' requirement.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_string(prompt):
    """
    Ensures the user doesn't enter an empty string.
    """
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print("Input cannot be empty.")