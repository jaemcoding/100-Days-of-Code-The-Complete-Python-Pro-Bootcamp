import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

is_new = True
while is_new:
    print(art.logo)
    is_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while is_continue:
        operation_symbol = input("Pick an operation:")
        num2 = float(input("What's the next number?: "))
        result = (operations[operation_symbol](num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {result}")
        num1 = result
        new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if new_calculation == "n":
            is_continue = False