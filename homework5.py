# Homework 5



def calculate(a, operator, b):
    """Performs basic arithmetic operations and returns the result, or None if invalid."""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return None
        return a / b
    else:
        return None

def main():
    while True:
        first_input = input("First number (or q): ").strip()
        
        # 5. Keep asking until the user types q as the first number
        if first_input.lower() == 'q':
            break
        
        try:
            a = float(first_input)
        except ValueError:
            print("Cannot calculate that")
            continue

        operator = input("Operator (+ - * /): ").strip()
        
        second_input = input("Second number: ").strip()
        try:
            b = float(second_input)
        except ValueError:
            print("Cannot calculate that")
            continue

        result = calculate(a, operator, b)
        
        # 4. If calculate() returns None, print: Cannot calculate that
        if result is None:
            print("Cannot calculate that")
        else:
            print(f"Result: {result}")

main()
