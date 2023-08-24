def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator_input():
    while True:
        operator = input("Choose the operation (+, -, *, //): ")
        if operator in ('+', '-', '*', '//'):
            return operator
        else:
            print("Invalid operation. Please choose from +, -, *, //.")

def calculator(x, y, operator):
    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "//":
        if y != 0:
            result = x // y
        else:
            print("Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator")
        return None
    return result

def main():
    print("Welcome to the Pro Calculator!")
    x = get_number_input("Enter the first number: ")
    operator = get_operator_input()
    y = get_number_input("Enter the second number: ")

    result = calculator(x, y, operator)
    if result is not None:
        print("Result:", result)

if __name__ == "__main__":
    main()
