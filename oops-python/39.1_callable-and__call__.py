# ============================================================
# __call__() AND CALLABLE OBJECTS
# ============================================================
# A callable is an object that can be invoked using parentheses:
#
#     obj()
#
# Functions, methods, classes, and objects implementing __call__()
# can be callable.
#
# callable(obj) returns True if Python considers obj callable.
# ============================================================


# ============================================================
# 1. CHECKING CALLABLE OBJECTS
# ============================================================

def greet():
    return "Hello"


x = 10

print(callable(greet))  # True
print(callable(x))      # False


# ============================================================
# 2. FUNCTIONS ARE OBJECTS
# ============================================================
# Functions are objects too, and function objects implement
# __call__().
#
# Therefore:
#
#     add(10, 20)
#
# performs the function-call operation on the function object.
#
# Note:
# The exact interpreter-level implementation is more nuanced than
# simply rewriting every function call as add.__call__(...), but
# conceptually __call__ represents the callable protocol.

def add(a, b):
    return a + b


print(add(10, 20))
print(callable(add))


# ============================================================
# 3. MAKING A CUSTOM OBJECT CALLABLE
# ============================================================
# Defining __call__() makes instances of the class callable.

class Calculator:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y


calculator = Calculator(10)

print(calculator(20))
print(callable(calculator))


# ============================================================
# 4. __call__ WITH MULTIPLE ARGUMENTS
# ============================================================
# __call__ can accept any arguments required by the object's
# behavior.

class Calculator:
    def __call__(self, a, b, operation="+"):
        if operation == "+":
            return a + b
        if operation == "-":
            return a - b
        if operation == "*":
            return a * b
        if operation == "/":
            return a / b
        raise ValueError("Unsupported operation")


calc = Calculator()

print(calc(10, 5))
print(calc(10, 5, "-"))
print(calc(10, 5, "*"))
print(calc(10, 5, "/"))


# ============================================================
# 5. STATEFUL CALLABLE OBJECTS
# ============================================================
# Unlike a normal function, a callable object can retain state
# between calls through instance variables.

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


counter = Counter()

print(counter())
print(counter())
print(counter())
print(counter.count)


# ============================================================
# 6. CALLABLE OBJECT AS A FUNCTION WITH MEMORY
# ============================================================
# This is useful when behavior needs persistent configuration/state.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(10))
print(triple(10))


# ============================================================
# 7. __call__ WITH *args AND **kwargs
# ============================================================
# A callable object can behave like a flexible function.

class Calculator:
    def __call__(self, *args, **kwargs):
        operation = kwargs.get("operation", "sum")

        if operation == "sum":
            return sum(args)

        if operation == "max":
            return max(args)

        if operation == "min":
            return min(args)

        raise ValueError("Unsupported operation")


calc = Calculator()

print(calc(10, 20, 30))
print(calc(10, 20, 30, operation="max"))
print(calc(10, 20, 30, operation="min"))


# ============================================================
# 8. __call__ FOR VALIDATION
# ============================================================
# A callable object can encapsulate reusable validation logic.

class Validator:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __call__(self, value):
        return self.minimum <= value <= self.maximum


is_valid_age = Validator(18, 60)

print(is_valid_age(25))
print(is_valid_age(70))


# ============================================================
# 9. CALLABLE OBJECT AS A DECORATOR
# ============================================================
# Decorators are another practical use of callable objects.
#
# A decorator object can store configuration while __call__()
# receives the function being decorated.

class Logger:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"{self.prefix}: calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{self.prefix}: finished")
            return result

        return wrapper


@Logger("LOG")
def add(a, b):
    return a + b


print(add(10, 20))


# ============================================================
# 10. PRACTICAL: FUNCTION-LIKE CONFIGURED OBJECT
# ============================================================
# A callable object is useful when the operation has configuration
# that should be created once and reused many times.

class TaxCalculator:
    def __init__(self, rate):
        self.rate = rate

    def __call__(self, amount):
        return amount * self.rate / 100


gst = TaxCalculator(18)

print(gst(1000))
print(gst(5000))


# ============================================================
# 11. __call__ CAN MODIFY OBJECT STATE
# ============================================================
# Calling an object does not have to be a pure operation.
# It can update the object's internal state.

class Accumulator:
    def __init__(self):
        self.total = 0

    def __call__(self, value):
        self.total += value
        return self.total


accumulate = Accumulator()

print(accumulate(10))
print(accumulate(20))
print(accumulate(30))


# ============================================================
# 12. __call__ VS NORMAL METHOD
# ============================================================
# Normal method:
#
#     obj.calculate(10)
#
# Callable object:
#
#     obj(10)
#
# __call__ is useful when the object conceptually represents an
# operation/function rather than just a data object.

class Power:
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, number):
        return number ** self.exponent


square = Power(2)
cube = Power(3)

print(square(5))
print(cube(5))


# ============================================================
# 13. CLASSES THEMSELVES ARE CALLABLE
# ============================================================
# A class is callable:
#
#     Student(...)
#
# creates an instance.
#
# Classes use their metaclass's callable behavior to perform
# instantiation.

class Student:
    def __init__(self, name):
        self.name = name


print(callable(Student))

student = Student("Rahul")

print(student.name)


# ============================================================
# 14. CHECKING CALLABILITY BEFORE EXECUTION
# ============================================================
# callable() is useful when a variable may contain either a
# callable or a normal value.

def process():
    return "Processed"


objects = [process, 100, lambda: "Lambda", Counter()]

for obj in objects:
    if callable(obj):
        if isinstance(obj, Counter):
            print(obj())
        else:
            print(obj())
    else:
        print(obj)


# ============================================================
# 15. ADVANCED: CALLABLE OBJECT WITH __repr__
# ============================================================
# __call__ defines execution behavior.
# __repr__ makes the object easier to inspect/debug.

class Converter:
    def __init__(self, multiplier, name):
        self.multiplier = multiplier
        self.name = name

    def __call__(self, value):
        return value * self.multiplier

    def __repr__(self):
        return f"Converter(name={self.name!r}, multiplier={self.multiplier})"


km_to_m = Converter(1000, "km_to_m")

print(km_to_m)
print(km_to_m(5))


# ============================================================
# 16. ADVANCED: CALLABLE OBJECT WITH ASYNC __call__
# ============================================================
# __call__ can also be asynchronous.
#
# Such an object must be called with await:
#
#     await obj(...)
#
# Useful for stateful/configured asynchronous operations.

class AsyncProcessor:
    async def __call__(self, value):
        return value * 2


# async def main():
#     processor = AsyncProcessor()
#     result = await processor(10)
#     print(result)


# ============================================================
# IMPORTANT INTERNAL CONCEPT
# ============================================================
# When Python encounters:
#
#     obj(...)
#
# it performs the CALL operation according to Python's callable
# protocol.
#
# For a normal user-defined instance, defining:
#
#     def __call__(self, ...):
#
# makes the instance callable.
#
# Therefore:
#
#     calculator(20)
#
# behaves conceptually as:
#
#     calculator.__call__(20)
#
# But Python's actual special-method lookup for operations is
# performed on the TYPE, not simply through normal instance
# attribute lookup.


# ============================================================
# KEY IDEA
# ============================================================
# __call__ turns an object into a FUNCTION-LIKE OBJECT.
#
# Normal object:
#     obj.method(value)
#
# Callable object:
#     obj(value)
#
# Main advantages:
#
#     • Object can retain state.
#     • Configuration can be stored once.
#     • Behavior can be reused through function-like syntax.
#     • Useful for validators, processors, calculators, ML models,
#       decorators, callbacks, and stateful operations.
#
# callable(obj):
#     Checks whether obj can be invoked.
#
# __call__:
#     Defines what happens when the object is invoked.
# ============================================================