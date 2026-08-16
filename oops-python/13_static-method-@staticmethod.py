# ============================================================
# STATIC METHODS
# ============================================================
# A static method is a method stored in a class namespace that
# does not receive an implicit self or cls argument.
#
# It is useful when a function is logically related to a class
# but does not need instance state or class state.
#
# @staticmethod tells Python not to bind an instance or class
# automatically.
# ============================================================


class Bank:
    @staticmethod
    def simple_interest(principal, years, rate):
        return (principal * years * rate) / 100


# No object is required.
interest = Bank.simple_interest(2000, 2, 5)
print(f"Simple Interest: {interest}")


# ============================================================
# STATIC METHOD WITH USER INPUT
# ============================================================
# Since the method does not depend on self or cls, it can work
# directly with values supplied by the caller.

principal = float(input("Enter principal amount: "))
years = int(input("Enter number of years: "))
rate = 5.0

interest = Bank.simple_interest(principal, years, rate)
print(f"Calculated Interest: {interest}")


# ============================================================
# STATIC METHOD vs INSTANCE METHOD vs CLASS METHOD
# ============================================================
# Instance method:
#     def method(self)
#     -> receives the current object automatically
#     -> works with instance state
#
# Class method:
#     @classmethod
#     def method(cls)
#     -> receives the class automatically
#     -> works with class-level state
#
# Static method:
#     @staticmethod
#     def method(...)
#     -> receives neither automatically
#     -> independent of instance/class state
# ============================================================


class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, number):
        return self.value + number

    @classmethod
    def create_zero(cls):
        return cls(0)

    @staticmethod
    def multiply(a, b):
        return a * b


calculator = Calculator(10)

print(calculator.add(5))
print(Calculator.create_zero().value)
print(Calculator.multiply(5, 4))


# ============================================================
# STATIC METHOD CAN ALSO BE CALLED THROUGH AN INSTANCE
# ============================================================
# Although class access is usually clearer, a static method can
# technically be accessed through an object as well.
#
# No object is passed automatically.

calculator = Calculator(10)

print(calculator.multiply(3, 4))
print(Calculator.multiply(3, 4))


# ============================================================
# WHEN TO USE @staticmethod
# ============================================================
# Use a static method when:
# - The logic is conceptually related to the class.
# - It does not need self.
# - It does not need cls.
# - It does not read or modify object/class state.
#
# Examples:
# - Validation utilities
# - Mathematical calculations
# - Formatting helpers
# - Conversion functions
# - Parsing/utility operations
#
# If the function has no meaningful relationship with the class,
# a normal module-level function may be a better design.
# ============================================================


class User:
    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 <= age <= 120

    @staticmethod
    def normalize_name(name):
        return name.strip().title()


print(User.is_valid_age(25))
print(User.normalize_name("  rahul kumar  "))