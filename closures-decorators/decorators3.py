# ============================================================
# Decorator for Error Handling
# ============================================================
#
# A decorator can add error handling to an existing function
# without changing the function's original logic.
#
# Here, we will handle ZeroDivisionError by checking whether
# the denominator is zero before calling the original function.
#
# ============================================================
# 1. BASIC DIVISION FUNCTION
# ============================================================

def div(a, b):
    print(a / b)


# div(10, 0)  # Raises ZeroDivisionError


# ============================================================
# 2. CREATING THE DECORATOR
# ============================================================
#
# The decorator receives the original function as func.
# inner() acts as a wrapper around func.
#
# The wrapper can check conditions before deciding whether
# the original function should execute.
#
# ============================================================

def decor(func):
    def inner(a, b):
        if b == 0:
            print("Can not divide by zero")
            return

        return func(a, b)

    return inner


# ============================================================
# 3. APPLYING THE DECORATOR
# ============================================================
#
# @decor is equivalent to:
#
#     div = decor(div)
#
# After decoration, div refers to inner().
#
# When div() is called:
#
#     div() → inner() → original div()
#
# The original function runs only when b is not zero.
#
# ============================================================

@decor
def div(a, b):
    print(a / b)


div(10, 2)
div(10, 0)


# ============================================================
# 4. ADVANCED: *args AND **kwargs
# ============================================================
#
# Using *args and **kwargs makes the decorator more reusable.
# It can work with functions having different arguments.
#
# *args  → positional arguments
# **kwargs → keyword arguments
#
# ============================================================

def decor(func):
    def inner(*args, **kwargs):
        # args[1] represents the second positional argument.
        if len(args) > 1 and args[1] == 0:
            print("Can not divide by zero")
            return

        return func(*args, **kwargs)

    return inner


@decor
def div(a, b):
    print(a / b)


div(10, 2)
div(10, 0)


# ============================================================
# KEY POINT
# ============================================================
#
# @decor
# def div(a, b):
#     ...
#
# is equivalent to:
#
# div = decor(div)
#
# The decorator separates:
#
#     Business logic      → division
#     Extra logic         → zero-check
#
# This same pattern is commonly used for:
#
#     logging, validation, authentication, timing, caching,
#     and error handling.
#
# Remember:
#
#     decorator → receives function
#                ↓
#              wrapper
#                ↓
#         checks condition
#                ↓
#        original function
#
# ============================================================