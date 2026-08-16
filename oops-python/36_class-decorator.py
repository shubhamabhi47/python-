# ============================================================
# CLASS DECORATORS
# ============================================================
# A class decorator is a class used as a decorator.
#
# A decorator receives a function/class and returns a modified
# function/class.
#
# With a class decorator:
#
#     @Decorator
#     def add(...):
#         ...
#
# is conceptually:
#
#     add = Decorator(add)
#
# The original function is stored inside the decorator instance.
# __call__() then makes that instance behave like the function.
# ============================================================


# ============================================================
# 1. FUNCTION DECORATOR RECAP
# ============================================================
# A normal decorator receives a function and returns a wrapper.

def my_decorator(func):
    def wrapper():
        print("Extra functionality")
        result = func()
        return result
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# ============================================================
# 2. CLASS USED AS A DECORATOR
# ============================================================
# __init__() receives the original function when the decorator
# is applied.
#
# __call__() runs whenever the decorated function is called.

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function")
        result = self.func(*args, **kwargs)
        print("After function")
        return result


@Decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Rahul")


# ============================================================
# 3. MODIFYING THE FUNCTION'S RESULT
# ============================================================
# The decorator can execute the original function and then
# transform its result.

class SquareResult:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(f"Original result: {result}")
        return result ** 2


@SquareResult
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 6)

print(f"Final result: {result}")


# ============================================================
# 4. WHY *args AND **kwargs?
# ============================================================
# A decorator should normally work with functions having different
# signatures.
#
# *args   -> positional arguments
# **kwargs -> keyword arguments

class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)


@Logger
def add(a, b):
    return a + b


@Logger
def greet(name, message="Hello"):
    return f"{message}, {name}"


print(add(10, 20))
print(greet("Rahul"))
print(greet("Rahul", message="Welcome"))


# ============================================================
# 5. CLASS DECORATOR WITH STATE
# ============================================================
# Unlike a normal wrapper, a decorator object can maintain state
# between function calls.

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count}")
        return self.func(*args, **kwargs)


@CallCounter
def greet(name):
    print(f"Hello {name}")


greet("A")
greet("B")
greet("C")

print(greet.count)


# ============================================================
# 6. CLASS DECORATOR WITH CONFIGURATION
# ============================================================
# A class decorator can accept configuration when the decorator
# itself is created.
#
#     @Repeat(3)
#
# requires TWO stages:
#
# Repeat(3) -> creates decorator object/factory
# decorator(function) -> decorates the function
#
# This is different from simply using @Repeat.

class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper


@Repeat(3)
def greet(name):
    print(f"Hello {name}")


greet("Rahul")


# ============================================================
# 7. CLASS DECORATOR + functools.wraps
# ============================================================
# A wrapper normally loses metadata such as:
#
#     __name__
#     __doc__
#
# functools.wraps preserves important function metadata.

from functools import wraps


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)


@Logger
def add(a, b):
    """Adds two numbers."""
    return a + b


print(add(2, 3))

# Important:
# Since the decorated object itself is a Logger instance, simply
# using wraps inside __call__ is not enough to make add.__name__
# behave exactly like a normal decorated function.


# ============================================================
# 8. ADVANCED: CLASS DECORATOR PRESERVING FUNCTION METADATA
# ============================================================
# update_wrapper() can copy metadata from the original function
# to the decorator instance itself.

from functools import update_wrapper


class Logger:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.__name__}")
        return self.func(*args, **kwargs)


@Logger
def add(a, b):
    """Adds two numbers."""
    return a + b


print(add(10, 20))
print(add.__name__)
print(add.__doc__)


# ============================================================
# 9. CLASS DECORATOR FOR VALIDATION
# ============================================================
# Class decorators are useful when validation behavior needs
# configuration and reusable state.

class ValidateTypes:
    def __init__(self, *types):
        self.types = types

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for value, expected in zip(args, self.types):
                if not isinstance(value, expected):
                    raise TypeError(
                        f"Expected {expected.__name__}, "
                        f"got {type(value).__name__}"
                    )
            return func(*args, **kwargs)

        return wrapper


@ValidateTypes(int, int)
def add(a, b):
    return a + b


print(add(10, 20))

# print(add(10, "20"))  # TypeError


# ============================================================
# 10. CLASS DECORATOR FOR TIMING
# ============================================================
# A decorator can measure execution time without changing the
# original function's core logic.

import time
from functools import update_wrapper


class Timer:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()

        result = self.func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        print(f"{self.__name__} took {elapsed:.6f}s")

        return result


@Timer
def calculate():
    return sum(range(1_000_000))


print(calculate())


# ============================================================
# 11. STACKING CLASS DECORATORS
# ============================================================
# Multiple decorators are applied from bottom to top.
#
#     @A
#     @B
#     def func():
#
# is equivalent to:
#
#     func = A(B(func))

class First:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("First before")
        result = self.func(*args, **kwargs)
        print("First after")
        return result


class Second:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Second before")
        result = self.func(*args, **kwargs)
        print("Second after")
        return result


@First
@Second
def greet():
    print("Hello")


greet()


# ============================================================
# 12. CLASS DECORATOR VS FUNCTION DECORATOR
# ============================================================
# Function decorator:
#
#     function -> wrapper function
#
# Class decorator:
#
#     function -> decorator object
#
# The class-based approach is particularly useful when the
# decorator needs persistent state or configuration.
#
# Both ultimately implement the same decorator protocol:
#
#     receive callable -> return callable
# ============================================================


# ============================================================
# 13. IMPORTANT DECORATOR FLOW
# ============================================================
# Consider:
#
#     @Logger
#     def add(a, b):
#         return a + b
#
# During definition:
#
#     add = Logger(add)
#
# This invokes:
#
#     Logger.__init__(original_add)
#
# Later:
#
#     add(10, 20)
#
# invokes:
#
#     Logger.__call__(10, 20)
#
# Inside __call__:
#
#     self.func(10, 20)
#
# executes the original function.
# ============================================================


# ============================================================
# 14. CLASS DECORATOR FOR CACHING
# ============================================================
# A stateful class decorator can implement a simple cache.
#
# The object stores previous results and avoids repeating work.

class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key not in self.cache:
            print("Calculating...")
            self.cache[key] = self.func(*args, **kwargs)
        else:
            print("Using cached result")

        return self.cache[key]


@Cache
def expensive_calculation(n):
    return sum(i * i for i in range(n))


print(expensive_calculation(100000))
print(expensive_calculation(100000))


# ============================================================
# KEY IDEA
# ============================================================
# CLASS DECORATOR:
#
#     @Decorator
#     def function(...):
#         ...
#
# becomes:
#
#     function = Decorator(function)
#
# __init__():
#     Runs once when the function is decorated.
#     Stores/configures the original function.
#
# __call__():
#     Runs every time the decorated function is called.
#
# *args / **kwargs:
#     Allow the decorator to support flexible function signatures.
#
# STATE:
#     Class decorators can retain information between calls.
#
# CONFIGURATION:
#     A decorator class can store reusable configuration such as
#     retry count, logging options, validation rules, or cache data.
#
# update_wrapper():
#     Useful when the decorator instance should preserve metadata
#     such as __name__, __doc__, and related attributes.
#
# CORE PATTERN:
#
#     original function
#            ↓
#     decorator object
#            ↓
#     __call__()
#            ↓
#     original function + extra behavior
# ============================================================