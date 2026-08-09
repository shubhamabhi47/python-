import math


def calculator():
    while True:
        print("\n1. Relational\n2. Bitwise\n3. Number System\n4. Power/Root\n5. Log/Exp\n6. Arithmetic\n7. Logical\n8. Exit")
        choice = input("Choose an option (1-8): ")

        match choice:
            case '1':
                relational_operations()
            case '2':
                bitwise_operations()
            case '3':
                number_system_conversions()
            case '4':
                root_power_operations()
            case '5':
                log_exponential_operations()
            case '6':
                arithmetic_operations()
            case '7':
                logical_operations()
            case '8':
                break
            case _:
                print("Invalid choice. Please try again.")


# Relational operations
def relational_operations():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    op = input("Choose a relational operator (==, !=, >, <, >=, <=): ")

    match op:
        case "==":
            print(f"Result: {a == b}")
        case "!=":
            print(f"Result: {a != b}")
        case ">":
            print(f"Result: {a > b}")
        case "<":
            print(f"Result: {a < b}")
        case ">=":
            print(f"Result: {a >= b}")
        case "<=":
            print(f"Result: {a <= b}")
        case _:
            print("Invalid operator.")


# Bitwise operations
def bitwise_operations():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    op = input("Choose a bitwise operator (&, |, ^, <<, >>): ")

    match op:
        case "&":
            print(f"Result: {a & b}")
        case "|":
            print(f"Result: {a | b}")
        case "^":
            print(f"Result: {a ^ b}")
        case "<<":
            print(f"Result: {a << b}")
        case ">>":
            print(f"Result: {a >> b}")
        case _:
            print("Invalid operator.")


# Number system conversions
def number_system_conversions():
    num = input("Enter a number: ")
    base = int(input("Enter the base of the number (2, 8, 10, 16): "))

    dec = int(num, base)
    print(f"Binary: {bin(dec)}, Octal: {oct(dec)}, Hexadecimal: {hex(dec)}, Decimal: {dec}")


# Power and root operations
def root_power_operations():
    x = float(input("Enter the value of x: "))
    y = input("Enter the value of y (press Enter for square root): ")

    if y:
        y = float(y)
        print(f"{x}^{y} = {x ** y}")
    else:
        print(f"√{x} = {math.sqrt(x)}")


# Logarithmic and exponential operations
def log_exponential_operations():
    x = float(input("Enter the value of x: "))
    op = input("Choose an operation (log, exp): ")

    match op:
        case "log":
            print(f"log({x}) = {math.log(x)}")
        case "exp":
            print(f"exp({x}) = {math.exp(x)}")
        case _:
            print("Invalid operation.")


# Arithmetic operations
def arithmetic_operations():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    op = input("Choose an arithmetic operator (+, -, *, /, %, //): ")

    match op:
        case "+":
            print(f"Result: {a + b}")
        case "-":
            print(f"Result: {a - b}")
        case "*":
            print(f"Result: {a * b}")
        case "/":
            print(f"Result: {a / b}")
        case "%":
            print(f"Result: {a % b}")
        case "//":
            print(f"Result: {a // b}")
        case _:
            print("Invalid operator.")


# Logical operations
def logical_operations():
    a = bool(int(input("Enter the value of a (1 for True, 0 for False): ")))
    b = bool(int(input("Enter the value of b (1 for True, 0 for False): ")))
    op = input("Choose a logical operation (and, or, not): ")

    match op:
        case "and":
            print(f"Result: {a and b}")
        case "or":
            print(f"Result: {a or b}")
        case "not":
            print(f"Result: {not a}")
        case _:
            print("Invalid operation.")


if __name__ == "__main__":
    calculator()
