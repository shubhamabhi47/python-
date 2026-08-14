# ============================================================
# Decorators in Python
# ============================================================
#
# Decorators are a powerful feature in Python used to modify
# or extend the behavior of functions without permanently
# changing their original source code.
#
# Before learning decorators, it is important to understand
# Higher-Order Functions.
#
# Higher-Order Functions are functions that:
# 1. Take another function as an argument, or
# 2. Return another function.
#
# A decorator is essentially a function that takes another
# function, adds some extra functionality to it, and returns
# the modified function.
#
# ============================================================
# 1. Basic Function Structure
# ============================================================

def printer():
    print("Welcome to the session")
    print("Welcome to the session")


# Calling the function
printer()


# ============================================================
# 2. Creating a Decorator
# ============================================================
#
# A decorator wraps an existing function and allows us to add
# extra functionality before or after the original function
# executes.
#
# The original function does not need to be permanently changed.
# Instead, the decorator creates a wrapper around it.
#
# In the example below:
#
# - dec_decorator receives a function as an argument.
# - wrapper is the new function that adds extra functionality.
# - func() executes the original function.
# - The decorator returns wrapper.
#
# ============================================================

def dec_decorator(func):
    def wrapper():
        # Pre-execution logic

        func()  # Execute the original function

        # Post-execution logic
        print("New functionality added")

    return wrapper


# Applying the decorator manually
printer = dec_decorator(printer)

printer()


# ============================================================
# 3. Using @decorator Syntax
# ============================================================
#
# Python provides a cleaner way to apply decorators using the
# @ symbol.
#
# This is called decorator syntax.
#
# When we write:
#
# @dec_decorator
# def printer():
#     ...
#
# Python internally performs:
#
# printer = dec_decorator(printer)
#
# Therefore, @dec_decorator is simply syntactic sugar that
# makes decorators easier and cleaner to use.
#
# ============================================================

@dec_decorator
def printer():
    print("Welcome")


printer()


# ============================================================
# 4. Advanced Example: Access Control / Logic Modification
# ============================================================
#
# Decorators can be used to add additional functionality to
# an existing function without modifying the original logic.
#
# In this example:
#
# - The addition() function takes two numbers.
# - The decorator executes addition() first.
# - The decorator then asks the user for a third number.
# - The third number is added to the original result.
# - The final result is printed and returned.
#
# This demonstrates how a decorator can extend the behavior
# of an existing function.
#
# The original addition logic remains unchanged.
#
# ============================================================

def decorator_add(func):
    def wrapper():
        result = func()  # Execute the original add function

        third_num = float(input("Enter third number: "))

        final_res = result + third_num

        print(f"Final result: {final_res}")

        return final_res

    return wrapper


@decorator_add
def addition():
    n1 = float(input("First: "))
    n2 = float(input("Second: "))

    return n1 + n2


addition()