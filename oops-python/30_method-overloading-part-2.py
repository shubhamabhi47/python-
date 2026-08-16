# ============================================================
# SIMULATING METHOD OVERLOADING IN PYTHON
# ============================================================
# Python does not support traditional method overloading.
# Multiple methods with the same name cannot coexist in a class;
# the latest definition replaces the previous one.
#
# Instead, Python commonly simulates overloading using:
# 1. Default arguments
# 2. None as a sentinel value
# 3. *args / **kwargs
# 4. Conditional logic
# 5. Type-based dispatch
# ============================================================


# ============================================================
# 1. OVERLOADING USING DEFAULT ARGUMENTS + CONDITIONAL LOGIC
# ============================================================
# Optional parameters allow one method to handle different
# numbers of arguments.

class Calculation:
    def add(self, n1=None, n2=None, n3=None):
        if n1 is not None and n2 is not None and n3 is not None:
            return n1 + n2 + n3
        if n1 is not None and n2 is not None:
            return n1 + n2
        raise TypeError("add() requires 2 or 3 arguments")


obj = Calculation()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))


# ============================================================
# 2. WHY USE is NOT None INSTEAD OF != None?
# ============================================================
# None is a singleton sentinel value.
# "is None" / "is not None" explicitly checks identity and is
# the recommended Python style.
#
# Avoid:
#     value != None
#
# Prefer:
#     value is not None


# ============================================================
# 3. GEOMETRY EXAMPLE
# ============================================================
# One method handles:
#     calculate_area(side)       -> Square
#     calculate_area(length,w)   -> Rectangle

class Area:
    def calculate_area(self, length, width=None):
        if width is None:
            if length <= 0:
                raise ValueError("Side must be positive")
            return length * length

        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive")

        return length * width


area = Area()

print(area.calculate_area(10))
print(area.calculate_area(10, 20))


# ============================================================
# 4. DEFAULT VALUES SHOULD HAVE CLEAR SEMANTICS
# ============================================================
# Using 0 to mean "argument not supplied" can be problematic
# because 0 may itself be valid data.
#
# Example:
#     width=0
#
# could mean either:
#     • user intentionally supplied 0
#     • width was omitted
#
# None is safer as a sentinel when None is not a valid input.

class Shape:
    def area(self, length, width=None):
        if width is None:
            return length ** 2
        return length * width


shape = Shape()

print(shape.area(5))
print(shape.area(5, 10))


# ============================================================
# 5. USING *args FOR A VARIABLE NUMBER OF ARGUMENTS
# ============================================================
# *args is useful when the number of arguments is genuinely
# variable.

class Addition:
    def add(self, *numbers):
        if not numbers:
            raise TypeError("At least one number is required")
        return sum(numbers)


obj = Addition()

print(obj.add(10))
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(1, 2, 3, 4, 5))


# ============================================================
# 6. *args + CONDITIONAL LOGIC
# ============================================================
# You can reproduce different behaviors based on argument count.

class Calculator:
    def calculate(self, *numbers):
        if len(numbers) == 1:
            return numbers[0] ** 2
        if len(numbers) == 2:
            return numbers[0] + numbers[1]
        if len(numbers) == 3:
            return numbers[0] * numbers[1] * numbers[2]
        raise TypeError("Expected 1, 2, or 3 arguments")


calc = Calculator()

print(calc.calculate(5))
print(calc.calculate(5, 10))
print(calc.calculate(2, 3, 4))


# ============================================================
# 7. KEYWORD ARGUMENTS WITH DEFAULT VALUES
# ============================================================
# Default arguments also work naturally with keyword arguments.

class Employee:
    def create(self, name, salary=0, department="General"):
        return {
            "name": name,
            "salary": salary,
            "department": department
        }


employee = Employee()

print(employee.create("Rahul"))
print(employee.create("Rahul", 50000))
print(employee.create("Rahul", 50000, "Backend"))


# ============================================================
# 8. *args AND **kwargs TOGETHER
# ============================================================
# *args -> variable positional arguments
# **kwargs -> variable keyword arguments

class User:
    def create(self, *args, **kwargs):
        print("Positional:", args)
        print("Keyword:", kwargs)


user = User()

user.create("Rahul", 21)
user.create("Rahul", 21, city="Delhi", role="Student")


# ============================================================
# 9. TYPE-BASED BEHAVIOR
# ============================================================
# Traditional overloading can also depend on parameter types.
# Python does not do this automatically, but we can explicitly
# implement it using isinstance().

class Converter:
    def convert(self, value):
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            return value.strip().upper()
        if isinstance(value, list):
            return tuple(value)
        raise TypeError(f"Unsupported type: {type(value).__name__}")


converter = Converter()

print(converter.convert(10))
print(converter.convert(" python "))
print(converter.convert([1, 2, 3]))


# ============================================================
# 10. ADVANCED: SENTINEL OBJECT
# ============================================================
# If None is itself a valid argument, create a unique sentinel.
# This lets us distinguish:
#
#     argument omitted
#     argument explicitly passed as None

_MISSING = object()


class Configuration:
    def set_value(self, value=_MISSING):
        if value is _MISSING:
            return "No value supplied"
        if value is None:
            return "Value explicitly set to None"
        return f"Value: {value}"


config = Configuration()

print(config.set_value())
print(config.set_value(None))
print(config.set_value(100))


# ============================================================
# 11. VALIDATING ARGUMENT COUNT
# ============================================================
# Explicit argument-count handling gives clearer errors than
# silently accepting invalid combinations.

class Math:
    def add(self, *numbers):
        count = len(numbers)

        if count == 2:
            return numbers[0] + numbers[1]
        if count == 3:
            return sum(numbers)

        raise TypeError(
            f"add() takes 2 or 3 arguments, got {count}"
        )


math = Math()

print(math.add(10, 20))
print(math.add(10, 20, 30))


# ============================================================
# 12. WHEN DEFAULT ARGUMENTS ARE BETTER THAN *args
# ============================================================
# Use explicit parameters when each parameter has a different
# meaning.
#
# Example:
#     length, width
#
# is clearer than:
#     *values

class Rectangle:
    def area(self, length, width=None):
        return length ** 2 if width is None else length * width


rectangle = Rectangle()

print(rectangle.area(10))
print(rectangle.area(10, 20))


# ============================================================
# 13. WHEN *args IS BETTER
# ============================================================
# If all values have the same meaning, *args is cleaner.

class Sum:
    def calculate(self, *numbers):
        return sum(numbers)


s = Sum()

print(s.calculate(10, 20))
print(s.calculate(10, 20, 30, 40))
print(s.calculate(1, 2, 3, 4, 5, 6))


# ============================================================
# 14. METHOD OVERLOADING VS METHOD OVERRIDING
# ============================================================
# Overloading:
# Same class + same method name + different signatures.
# Traditional form is NOT supported by Python.
#
# Overriding:
# Child class replaces a parent's method implementation.
# This IS supported by Python.

class Parent:
    def show(self):
        print("Parent implementation")


class Child(Parent):
    def show(self):
        print("Child implementation")


obj = Child()
obj.show()


# ============================================================
# 15. METHOD OVERLOADING VS POLYMORPHISM
# ============================================================
# The technique above can produce polymorphic behavior because
# the same method call can behave differently depending on the
# supplied input.
#
# However, simply calling this "method overloading" is technically
# imprecise: Python is simulating overload-like behavior rather
# than providing Java/C++-style compile-time overload resolution.
#
# Example:
#
#     obj.add(10, 20)
#     obj.add(10, 20, 30)
#
# Both use the same Python method, but its internal logic chooses
# the appropriate behavior.


# ============================================================
# 16. REAL-WORLD EXAMPLE
# ============================================================
# One method can support multiple ways of creating a product.

class Product:
    def create(self, name, price=None, quantity=1):
        if price is None:
            raise ValueError("Price is required")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        return {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        }


product = Product()

print(product.create("Laptop", 50000))
print(product.create("Laptop", 50000, 2))


# ============================================================
# 17. CLEANER DESIGN: SEPARATE METHODS
# ============================================================
# Simulating overloading is not always the best design.
# If operations have significantly different meanings, separate
# method names can make the API clearer.

class Geometry:
    def square_area(self, side):
        return side ** 2

    def rectangle_area(self, length, width):
        return length * width


geometry = Geometry()

print(geometry.square_area(10))
print(geometry.rectangle_area(10, 20))


# ============================================================
# KEY TAKEAWAYS
# ============================================================
# Python does not support traditional method overloading.
#
# This does NOT create two methods:
#
#     def add(self, a, b): ...
#     def add(self, a, b, c): ...
#
# The second definition replaces the first.
#
# Common Python alternatives:
#
#     Default arguments:
#         def add(self, a, b, c=0)
#
#     Optional arguments:
#         def add(self, a, b=None)
#
#     Variable arguments:
#         def add(self, *args)
#
#     Keyword arguments:
#         def method(self, **kwargs)
#
#     Type-based dispatch:
#         isinstance(...)
#
#     Advanced dispatch:
#         functools.singledispatchmethod
#
# BEST PRACTICE:
# Use explicit parameters when they have clear meaning, *args
# when the number of similar arguments is genuinely variable,
# and separate methods when different operations deserve distinct
# names.
# ============================================================