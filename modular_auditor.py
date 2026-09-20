tax_rate = 0.10

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

def process_delivery(current_total, new_value):
    return current_total + new_value

def main():
    inventory = 0

    while True:
        value = get_valid_input()

        if value == "quit":
            break
        if value is None:
            continue

        inventory = process_delivery(inventory, value)
        print (f"Current inventory: {inventory}")

main()