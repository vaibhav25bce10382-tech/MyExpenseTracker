def print_header(title):
   
    print("\n" + "=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)

def get_valid_number(prompt):
    
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
   
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print("Input cannot be empty.")
