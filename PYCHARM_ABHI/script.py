import math


def calculator():
    while True:
        print(
            "\n1. Relational\n2. Bitwise\n3. Number System\n4. Power/Root\n5. Log/Exp\n6. Arithmetic\n7. Logical\n8. Exit")
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






# script is file contain set of information written in any particular
# programming language  which is designed to be excuted by any run time environment

# =>Features of scripts
# 1) scripts are interprted
# 2) scripts are written in a easier way so that users can read and understood
# 3)scripts can be created as modules that we can import the scripts when need to use that particular function
# 4)it allows code reusability


# For example -when we run the script directly it prompts the variable
# If we input the particular module in any other program or if we use more functions from C++,c, or any other programming language



# some of the inbuilt function in number system
# 1)Bin function: BIN(decimal number passed as parameter ) This function converts decimal number into binary number
# Hex and octal




#create a scientific calculator that wil operate the folloeing operation
# 1)Relational operation
# 2)Bitwise operation
# 3)All the conversins in the number system
# 4)Root and power operation
# 5)Log and exponential operation
# 6)Arthematic operaton
# 7)Logical operatin

# we can use recursion function or inbuilt function or exceptional handling concepts and user defined function


# def claculator():
#     ch
#
#
# import math
#
#
# def main_menu():
#     """
#     Displays the main menu and handles user selection.
#     """
#     while True:
#         print("\n===== Scientific Calculator =====")
#         print("1. Relational Operations")
#         print("2. Bitwise Operations")
#         print("3. Number System Conversions")
#         print("4. Root and Power Operations")
#         print("5. Logarithmic and Exponential Operations")
#         print("6. Arithmetic Operations")
#         print("7. Logical Operations")
#         print("8. Exit")
#
#         choice = input("Select an option (1-8): ")
#
#         if choice == '1':
#             relational_operations()
#         elif choice == '2':
#             bitwise_operations()
#         elif choice == '3':
#             number_system_conversions()
#         elif choice == '4':
#             root_power_operations()
#         elif choice == '5':
#             log_exponential_operations()
#         elif choice == '6':
#             arithmetic_operations()
#         elif choice == '7':
#             logical_operations()
#         elif choice == '8':
#             print("Exiting the calculator. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")
#
#
# # ------------------- Relational Operations -------------------
#
# def relational_operations():
#     """
#     Handles relational operations between two numbers.
#     """
#     print("\n--- Relational Operations ---")
#     try:
#         a = float(input("Enter the first number: "))
#         b = float(input("Enter the second number: "))
#
#         print("\nSelect Relational Operation:")
#         print("1. Equal to (==)")
#         print("2. Not equal to (!=)")
#         print("3. Greater than (>)")
#         print("4. Less than (<)")
#         print("5. Greater than or equal to (>=)")
#         print("6. Less than or equal to (<=)")
#
#         op = input("Choose an operation (1-6): ")
#
#         if op == '1':
#             result = a == b
#             print(f"{a} == {b} : {result}")
#         elif op == '2':
#             result = a != b
#             print(f"{a} != {b} : {result}")
#         elif op == '3':
#             result = a > b
#             print(f"{a} > {b} : {result}")
#         elif op == '4':
#             result = a < b
#             print(f"{a} < {b} : {result}")
#         elif op == '5':
#             result = a >= b
#             print(f"{a} >= {b} : {result}")
#         elif op == '6':
#             result = a <= b
#             print(f"{a} <= {b} : {result}")
#         else:
#             print("Invalid operation selected.")
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#
#
# # ------------------- Bitwise Operations -------------------
#
# def bitwise_operations():
#     """
#     Handles bitwise operations between two integers.
#     """
#     print("\n--- Bitwise Operations ---")
#     try:
#         a = int(input("Enter the first integer: "))
#         b = int(input("Enter the second integer: "))
#
#         print("\nSelect Bitwise Operation:")
#         print("1. AND (&)")
#         print("2. OR (|)")
#         print("3. XOR (^)")
#         print("4. Left Shift (<<)")
#         print("5. Right Shift (>>)")
#
#         op = input("Choose an operation (1-5): ")
#
#         if op == '1':
#             result = a & b
#             print(f"{a} & {b} = {result}")
#         elif op == '2':
#             result = a | b
#             print(f"{a} | {b} = {result}")
#         elif op == '3':
#             result = a ^ b
#             print(f"{a} ^ {b} = {result}")
#         elif op == '4':
#             shift = int(input("Enter number of positions to shift left: "))
#             result = a << shift
#             print(f"{a} << {shift} = {result}")
#         elif op == '5':
#             shift = int(input("Enter number of positions to shift right: "))
#             result = a >> shift
#             print(f"{a} >> {shift} = {result}")
#         else:
#             print("Invalid operation selected.")
#     except ValueError:
#         print("Invalid input. Please enter integer values.")
#
#
# # ------------------- Number System Conversions -------------------
#
# def number_system_conversions():
#     """
#     Converts numbers between different number systems.
#     """
#     print("\n--- Number System Conversions ---")
#     try:
#         number = input("Enter the number to convert: ")
#         print("\nSelect the base of the input number:")
#         print("1. Binary")
#         print("2. Octal")
#         print("3. Decimal")
#         print("4. Hexadecimal")
#
#         input_base_choice = input("Choose the input base (1-4): ")
#         input_base = None
#         if input_base_choice == '1':
#             input_base = 2
#         elif input_base_choice == '2':
#             input_base = 8
#         elif input_base_choice == '3':
#             input_base = 10
#         elif input_base_choice == '4':
#             input_base = 16
#         else:
#             print("Invalid input base selected.")
#             return
#
#         # Convert input to decimal first
#         decimal_number = int(number, input_base)
#
#         print("\nSelect the target base to convert to:")
#         print("1. Binary")
#         print("2. Octal")
#         print("3. Decimal")
#         print("4. Hexadecimal")
#
#         output_base_choice = input("Choose the output base (1-4): ")
#         if output_base_choice == '1':
#             result = bin(decimal_number)
#             base_str = "Binary"
#         elif output_base_choice == '2':
#             result = oct(decimal_number)
#             base_str = "Octal"
#         elif output_base_choice == '3':
#             result = str(decimal_number)
#             base_str = "Decimal"
#         elif output_base_choice == '4':
#             result = hex(decimal_number)
#             base_str = "Hexadecimal"
#         else:
#             print("Invalid output base selected.")
#             return
#
#         print(f"\n{number} in {base_str} is: {result}")
#     except ValueError:
#         print("Invalid number or base selected.")
#
#
# # ------------------- Root and Power Operations -------------------
#
# def root_power_operations():
#     """
#     Calculates roots and powers of numbers.
#     """
#     print("\n--- Root and Power Operations ---")
#     try:
#         print("\nSelect Operation:")
#         print("1. Power (x^y)")
#         print("2. Square Root")
#         print("3. Cube Root")
#         print("4. Nth Root")
#
#         op = input("Choose an operation (1-4): ")
#
#         if op == '1':
#             x = float(input("Enter the base number (x): "))
#             y = float(input("Enter the exponent (y): "))
#             result = math.pow(x, y)
#             print(f"{x} ^ {y} = {result}")
#         elif op == '2':
#             x = float(input("Enter the number to find the square root of: "))
#             if x < 0:
#                 print("Cannot compute square root of a negative number.")
#                 return
#             result = math.sqrt(x)
#             print(f"Square root of {x} is {result}")
#         elif op == '3':
#             x = float(input("Enter the number to find the cube root of: "))
#             result = math.copysign(abs(x) ** (1 / 3), x)
#             print(f"Cube root of {x} is {result}")
#         elif op == '4':
#             x = float(input("Enter the number to find the nth root of: "))
#             n = float(input("Enter the value of n: "))
#             if x < 0 and n % 2 == 0:
#                 print("Cannot compute even root of a negative number.")
#                 return
#             result = math.copysign(abs(x) ** (1 / n), x)
#             print(f"{n}th root of {x} is {result}")
#         else:
#             print("Invalid operation selected.")
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#
#
# # ------------------- Logarithmic and Exponential Operations -------------------
#
# def log_exponential_operations():
#     """
#     Calculates logarithms and exponential functions.
#     """
#     print("\n--- Logarithmic and Exponential Operations ---")
#     try:
#         print("\nSelect Operation:")
#         print("1. Natural Logarithm (ln)")
#         print("2. Logarithm base 10")
#         print("3. Logarithm with Custom Base")
#         print("4. Exponential (e^x)")
#         print("5. 10^x")
#
#         op = input("Choose an operation (1-5): ")
#
#         if op == '1':
#             x = float(input("Enter the number: "))
#             if x <= 0:
#                 print("Logarithm undefined for non-positive numbers.")
#                 return
#             result = math.log(x)
#             print(f"ln({x}) = {result}")
#         elif op == '2':
#             x = float(input("Enter the number: "))
#             if x <= 0:
#                 print("Logarithm undefined for non-positive numbers.")
#                 return
#             result = math.log10(x)
#             print(f"log10({x}) = {result}")
#         elif op == '3':
#             x = float(input("Enter the number: "))
#             base = float(input("Enter the base: "))
#             if x <= 0 or base <= 0 or base == 1:
#                 print("Invalid input for logarithm.")
#                 return
#             result = math.log(x, base)
#             print(f"log base {base} of {x} = {result}")
#         elif op == '4':
#             x = float(input("Enter the exponent: "))
#             result = math.exp(x)
#             print(f"e^{x} = {result}")
#         elif op == '5':
#             x = float(input("Enter the exponent: "))
#             result = math.pow(10, x)
#             print(f"10^{x} = {result}")
#         else:
#             print("Invalid operation selected.")
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#
#
# # ------------------- Arithmetic Operations -------------------
#
# def arithmetic_operations():
#     """
#     Performs basic arithmetic operations.
#     """
#     print("\n--- Arithmetic Operations ---")
#     try:
#         print("\nSelect Operation:")
#         print("1. Addition (+)")
#         print("2. Subtraction (-)")
#         print("3. Multiplication (*)")
#         print("4. Division (/)")
#         print("5. Modulus (%)")
#         print("6. Floor Division (//)")
#
#         op = input("Choose an operation (1-6): ")
#
#         a = float(input("Enter the first number: "))
#         b = float(input("Enter the second number: "))
#
#         if op == '1':
#             result = a + b
#             print(f"{a} + {b} = {result}")
#         elif op == '2':
#             result = a - b
#             print(f"{a} - {b} = {result}")
#         elif op == '3':
#             result = a * b
#             print(f"{a} * {b} = {result}")
#         elif op == '4':
#             if b == 0:
#                 print("Error: Division by zero.")
#                 return
#             result = a / b
#             print(f"{a} / {b} = {result}")
#         elif op == '5':
#             if b == 0:
#                 print("Error: Modulus by zero.")
#                 return
#             result = a % b
#             print(f"{a} % {b} = {result}")
#         elif op == '6':
#             if b == 0:
#                 print("Error: Floor division by zero.")
#                 return
#             result = a // b
#             print(f"{a} // {b} = {result}")
#         else:
#             print("Invalid operation selected.")
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#
#
# # ------------------- Logical Operations -------------------
#
# def logical_operations():
#     """
#     Performs logical operations between two boolean values.
#     """
#     print("\n--- Logical Operations ---")
#     try:
#         print("Enter boolean values as 1 (True) or 0 (False).")
#         a = input("Enter the first boolean value: ")
#         b = input("Enter the second boolean value: ")
#
#         if a not in ['0', '1'] or b not in ['0', '1']:
#             print("Invalid boolean input. Please enter 1 or 0.")
#             return
#
#         a = bool(int(a))
#         b = bool(int(b))
#
#         print("\nSelect Logical Operation:")
#         print("1. AND")
#         print("2. OR")
#         print("3. NOT (first value)")
#         print("4. NOT (second value)")
#         print("5. XOR")
#
#         op = input("Choose an operation (1-5): ")
#
#         if op == '1':
#             result = a and b
#             print(f"{a} AND {b} = {result}")
#         elif op == '2':
#             result = a or b
#             print(f"{a} OR {b} = {result}")
#         elif op == '3':
#             result = not a
#             print(f"NOT {a} = {result}")
#         elif op == '4':
#             result = not b
#             print(f"NOT {b} = {result}")
#         elif op == '5':
#             result = a ^ b
#             print(f"{a} XOR {b} = {result}")
#         else:
#             print("Invalid operation selected.")
#     except ValueError:
#         print("Invalid input. Please enter 1 or 0.")
#
#
# # ------------------- Entry Point -------------------
#
# if __name__ == "__main__":
#     main_menu()


