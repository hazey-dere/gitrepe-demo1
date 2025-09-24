def process_numbers():
    print("Enter numbers to process (or 'quit' to exit):")
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'quit':
            print("Exiting the function.")
            break
        elif user_input.isdigit():
            num = int(user_input)
            if num > 0:
                print(f"{num} is positive.")
            elif num < 0:
                print(f"{num} is negative.")
            else:
                print("Zero is neither positive nor negative.")
        else:
            print("Invalid input. Please enter a number or 'quit'.")

# Call the function to demonstrate
process_numbers()
