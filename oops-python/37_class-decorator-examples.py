# ============================================================
# CLASS DECORATOR: TYPE VALIDATION
# ============================================================
# A class-based decorator uses __call__() to make the decorator
# instance behave like the original function.
#
# @TypeValidator
# def add(...):
#     ...
#
# is equivalent to:
#
# add = TypeValidator(add)
#
# __init__() runs once during decoration and stores the original
# function.
#
# __call__() runs every time the decorated function is called.
# ============================================================


# ============================================================
# 1. THE PROBLEM: INVALID TYPES
# ============================================================
# Without validation, Python may raise TypeError only after the
# function starts executing.

def add(a, b, c):
    return a + b + c


print(add(10, 20, 30))

# print(add(10, "20", 30))  # TypeError


# ============================================================
# 2. BASIC CLASS-BASED DECORATOR
# ============================================================
# The decorator object stores the original function and intercepts
# every call through __call__().

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorator executed")
        return self.func(*args, **kwargs)


@Decorator
def multiply(a, b):
    return a * b


print(multiply(10, 20))


# ============================================================
# 3. TYPE VALIDATOR
# ============================================================
# Validate arguments before allowing the original function to run.

class TypeValidator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        for value in args:
            if isinstance(value, str):
                raise TypeError(
                    f"Invalid type: {type(value).__name__}. "
                    "Only numbers are allowed."
                )

        return self.func(*args, **kwargs)


@TypeValidator
def add(a, b, c):
    return a + b + c


try:
    print(add(10, 20, 30))
    print(add(10, "20", 30))
except TypeError as e:
    print(f"Caught error: {e}")


# ============================================================
# 4. BETTER VALIDATION: ACCEPT ONLY NUMBERS
# ============================================================
# Checking only for str is incomplete because other invalid types
# could still be passed.
#
# bool is technically a subclass of int, so it is explicitly
# rejected here.

class NumberValidator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(
                    f"Expected number, got {type(value).__name__}"
                )

        return self.func(*args, **kwargs)


@NumberValidator
def add(a, b, c):
    return a + b + c


print(add(10, 20, 30))

# print(add(10, "20", 30))
# print(add(10, True, 30))


# ============================================================
# 5. VALIDATING POSITIONAL + KEYWORD ARGUMENTS
# ============================================================
# *args validates positional arguments.
# **kwargs validates keyword arguments.
#
# This makes the decorator more general.

class NumberValidator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        values = (*args, *kwargs.values())

        for value in values:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(
                    f"Expected number, got {type(value).__name__}"
                )

        return self.func(*args, **kwargs)


@NumberValidator
def calculate(a, b, c=0):
    return a + b + c


print(calculate(10, 20, 30))
print(calculate(10, 20, c=30))


# ============================================================
# 6. ADVANCED: VALIDATE SPECIFIC TYPES
# ============================================================
# Instead of hard-coding number validation, the decorator can
# receive the expected types as configuration.
#
# @ValidateTypes(int, int, int)
#
# means:
# argument 1 -> int
# argument 2 -> int
# argument 3 -> int

class ValidateTypes:
    def __init__(self, *expected_types):
        self.expected_types = expected_types

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for value, expected in zip(args, self.expected_types):
                if not isinstance(value, expected):
                    raise TypeError(
                        f"{func.__name__}() expected "
                        f"{expected.__name__}, "
                        f"got {type(value).__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper


@ValidateTypes(int, int, int)
def add(a, b, c):
    return a + b + c


print(add(10, 20, 30))

# print(add(10, "20", 30))


# ============================================================
# 7. WHY isinstance()?
# ============================================================
# isinstance(value, Type) returns True when value is an instance
# of the specified type or its subclass.
#
# It is generally preferred over:
#
# type(value) == Type
#
# because isinstance() supports inheritance.

class Number:
    pass


class Integer(Number):
    pass


obj = Integer()

print(isinstance(obj, Integer))
print(isinstance(obj, Number))


# ============================================================
# 8. DECORATOR WITH ERROR HANDLING
# ============================================================
# Validation can happen before the function executes.
# Exceptions can then be handled by the caller.

class TypeValidator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        for value in (*args, *kwargs.values()):
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"{self.func.__name__} accepts numbers only"
                )

        return self.func(*args, **kwargs)


@TypeValidator
def divide(a, b):
    return a / b


try:
    print(divide(10, 2))
    print(divide(10, "2"))
except TypeError as e:
    print("Type error:", e)
except ZeroDivisionError as e:
    print("Math error:", e)


# ============================================================
# 9. PRESERVING FUNCTION METADATA
# ============================================================
# A class decorator replaces the original function with a class
# instance, so metadata such as __name__ and __doc__ can be lost.
#
# update_wrapper() copies important metadata to the decorator
# instance.

from functools import update_wrapper


class TypeValidator:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        for value in (*args, *kwargs.values()):
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"{self.__name__} accepts numbers only"
                )

        return self.func(*args, **kwargs)


@TypeValidator
def add(a, b):
    """Adds two numbers."""
    return a + b


print(add(10, 20))
print(add.__name__)
print(add.__doc__)


# ============================================================
# 10. ADVANCED: REUSABLE TYPE VALIDATOR
# ============================================================
# This version validates every argument against the corresponding
# expected type.
#
# @ValidateTypes(int, int, int)
#
# The decorator factory first creates a configuration object.
# That object then receives the target function through __call__().

from functools import wraps


class ValidateTypes:
    def __init__(self, *expected_types):
        self.expected_types = expected_types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) < len(self.expected_types):
                raise TypeError(
                    f"{func.__name__}() requires "
                    f"{len(self.expected_types)} arguments"
                )

            for index, (value, expected) in enumerate(
                zip(args, self.expected_types), start=1
            ):
                if not isinstance(value, expected):
                    raise TypeError(
                        f"Argument {index}: expected "
                        f"{expected.__name__}, "
                        f"got {type(value).__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper


@ValidateTypes(int, int, int)
def add(a, b, c):
    return a + b + c


print(add(10, 20, 30))


# ============================================================
# 11. IMPORTANT: TWO TYPES OF CLASS-BASED DECORATORS
# ============================================================
# TYPE 1:
#
# @Decorator
# def func():
#     ...
#
# Python performs:
#
# func = Decorator(func)
#
# Here __init__ receives the function and __call__ executes it.
#
#
# TYPE 2:
#
# @Decorator(config)
# def func():
#     ...
#
# Python performs:
#
# decorator = Decorator(config)
# func = decorator(func)
#
# Here:
#
# __init__() -> receives configuration
# __call__() -> receives the function
#
# This second pattern is useful for configurable decorators.
# ============================================================


# ============================================================
# 12. FINAL COMPLETE EXAMPLE
# ============================================================
# A practical reusable validator with:
#   - configurable expected types
#   - positional arguments
#   - keyword arguments
#   - preserved metadata
#   - clear error messages

from functools import wraps


class ValidateTypes:
    def __init__(self, *expected_types):
        self.expected_types = expected_types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(self.expected_types):
                raise TypeError(
                    f"{func.__name__}() expects "
                    f"{len(self.expected_types)} arguments, "
                    f"got {len(args)}"
                )

            for index, (value, expected) in enumerate(
                zip(args, self.expected_types), start=1
            ):
                if not isinstance(value, expected):
                    raise TypeError(
                        f"Argument {index} of {func.__name__}(): "
                        f"expected {expected.__name__}, "
                        f"got {type(value).__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper


@ValidateTypes(int, int, int)
def add(a, b, c):
    """Returns the sum of three integers."""
    return a + b + c


try:
    print(add(10, 20, 30))
    print(add(10, "20", 30))
except TypeError as e:
    print(f"Caught error: {e}")


# ============================================================
# CORE FLOW
# ============================================================
# For:
#
# @TypeValidator
# def add(a, b, c):
#     return a + b + c
#
# Python creates:
#
#     add = TypeValidator(add)
#
# __init__(add)
#       ↓
# stores original function
#       ↓
# add(10, 20, 30)
#       ↓
# __call__(10, 20, 30)
#       ↓
# validate arguments
#       ↓
# original add()
#       ↓
# result
#
# CORE IDEA:
# A class decorator replaces the original callable with an
# instance of a class whose __call__() controls what happens
# whenever that callable is invoked.
# ============================================================