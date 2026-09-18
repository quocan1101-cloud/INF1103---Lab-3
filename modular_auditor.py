inventory = 0

def get_valid_input():
    input_value = input("Enter the number of items to add to inventory (or type 'quit' to exit): ")
    if input_value == "quit":
        return "quit"

    try:
        val = int(input_value)
    except ValueError:
        print("Please enter a valid number or 'quit' to exit.")
        return None

    if val < 0:
        print("Please enter a positive number.")
        return None

    return val

