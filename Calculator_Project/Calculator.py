# Define the functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program to run the calculator
def main():
    print("Welcome to the Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take input from the user for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Validate choice input
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input. Please enter a valid input.")
        return
    
    # Take input from the user for the numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the chosen operation
    if choice == '1':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")

# Run the main function
if __name__ == "__main__":
    main()
