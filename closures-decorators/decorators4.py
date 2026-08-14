# ============================================================
# SMART DIVIDER USING DECORATORS
# ============================================================
#
# A decorator can add validation or error-prevention logic
# without modifying the original function.
#
# Here, the decorator checks whether the denominator is zero
# before allowing the division function to execute.
#
# ============================================================
# 1. BASIC DIVISION
# ============================================================

def div(a, b):
    print(a / b)


div(10, 2)  # Output: 5.0
# div(10, 0)  # Raises ZeroDivisionError


# ============================================================
# 2. CREATING THE DECORATOR
# ============================================================
#
# smart_divider receives the original div function as func.
#
# inner() becomes the new function that controls when the
# original function is allowed to execute.
#
# If b == 0, inner() returns immediately.
# Otherwise, it calls the original function.
#
# ============================================================

def smart_divider(func):
    def inner(a, b):
        if b == 0:
            print("You cannot perform division by zero")
            return

        return func(a, b)

    return inner


# ============================================================
# 3. APPLYING THE DECORATOR
# ============================================================
#
# @smart_divider is equivalent to:
#
#     div = smart_divider(div)
#
# After decoration:
#
#     div → inner
#     inner → original div through func
#
# So calling div() actually calls inner() first.
#
# ============================================================

@smart_divider
def div(a, b):
    print(a / b)


div(10, 0)  # Output: You cannot perform division by zero
div(10, 2)  # Output: 5.0


# ============================================================
# 4. EXECUTION FLOW
# ============================================================
#
# div(10, 0)
#      ↓
# inner(10, 0)
#      ↓
# b == 0 ?
#      ↓
# Yes → print message → return
#
# The original div() is NEVER called.
#
#
# div(10, 2)
#      ↓
# inner(10, 2)
#      ↓
# b == 0 ?
#      ↓
# No
#      ↓
# func(10, 2)
#      ↓
# original div()
#      ↓
# 5.0
#
# ============================================================
# KEY POINT
# ============================================================
#
# @smart_divider
# def div(a, b):
#     ...
#
# means:
#
#     div = smart_divider(div)
#
# The decorator acts as a gatekeeper:
#
#     call → inner → validation → original function
#
# This pattern is useful for validation, logging,
# authentication, timing, caching, and error handling.
#
# ============================================================
