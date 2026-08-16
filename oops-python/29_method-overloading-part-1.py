# ============================================================
# METHOD OVERLOADING IN PYTHON
# ============================================================
# Method overloading means defining multiple methods with the
# same name but different parameter lists.
#
# Languages such as Java/C++ support traditional compile-time
# method overloading.
#
# Python does NOT support traditional method overloading.
# If multiple methods have the same name inside a class, the
# latest definition replaces the previous one.
# ============================================================


# ============================================================
# 1. THEORETICAL METHOD OVERLOADING
# ============================================================
# This pattern works in languages that support method overloading,
# but NOT in Python.
#
# class Addition:
#     def add(self, a, b):
#         return a + b
#
#     def add(self, a, b, c):
#         return a + b + c
#
# In Python, the second add() replaces the first add().


# ============================================================
# 2. PYTHON'S ACTUAL BEHAVIOR
# ============================================================
class Addition:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj = Addition()

# print(obj.add(10, 20))  # TypeError
print(obj.add(10, 20, 30))  # 60


# ============================================================
# 3. WHY DOES THE FIRST METHOD DISAPPEAR?
# ============================================================
# A class namespace behaves approximately like a mapping:
#
#     "add" -> function
#
# When Python encounters the second add(), the same name is
# assigned again:
#
#     "add" -> old function
#     "add" -> new function
#
# Therefore only the latest definition remains accessible.

class Demo:
    def show(self):
        print("First")

    def show(self):
        print("Second")


d = Demo()
d.show()  # Second


# ============================================================
# 4. SIMULATING OVERLOADING WITH DEFAULT ARGUMENTS
# ============================================================
# Python's default arguments can provide different behavior
# depending on how many arguments are supplied.

class Addition:
    def add(self, a, b, c=0):
        return a + b + c


obj = Addition()

print(obj.add(10, 20))       # 30
print(obj.add(10, 20, 30))   # 60


# ============================================================
# 5. MULTIPLE OPTIONAL PARAMETERS
# ============================================================
class Calculator:
    def calculate(self, a, b=0, c=0, d=0):
        return a + b + c + d


calc = Calculator()

print(calc.calculate(10))
print(calc.calculate(10, 20))
print(calc.calculate(10, 20, 30))
print(calc.calculate(10, 20, 30, 40))


# ============================================================
# 6. SIMULATING OVERLOADING WITH *args
# ============================================================
# *args allows a method to accept any number of positional
# arguments.
#
# This is one of the most flexible Python alternatives to
# traditional method overloading.

class Addition:
    def add(self, *numbers):
        return sum(numbers)


obj = Addition()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(1, 2, 3, 4, 5))


# ============================================================
# 7. *args WITH DIFFERENT BEHAVIOR
# ============================================================
# You can inspect the number of arguments and choose different
# logic accordingly.

class Calculator:
    def calculate(self, *args):
        if len(args) == 1:
            return args[0] ** 2
        if len(args) == 2:
            return args[0] + args[1]
        if len(args) == 3:
            return args[0] * args[1] * args[2]
        raise TypeError("Unsupported number of arguments")


calc = Calculator()

print(calc.calculate(5))        # 25
print(calc.calculate(5, 10))    # 15
print(calc.calculate(2, 3, 4))  # 24


# ============================================================
# 8. USING *args AND **kwargs
# ============================================================
# *args handles variable positional arguments.
# **kwargs handles variable keyword arguments.

class User:
    def create(self, *args, **kwargs):
        print("Positional:", args)
        print("Keyword:", kwargs)


user = User()

user.create("Rahul", 21)
user.create("Rahul", 21, city="Delhi", role="Student")


# ============================================================
# 9. TYPE-BASED DISPATCH
# ============================================================
# Python does not overload based on parameter types automatically.
# However, you can explicitly inspect types when necessary.

class Calculator:
    def add(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        raise TypeError("Unsupported operand types")


calc = Calculator()

print(calc.add(10, 20))
print(calc.add("Hello ", "Python"))


# ============================================================
# 10. SINGLE DISPATCH WITH functools.singledispatchmethod
# ============================================================
# Python provides singledispatchmethod for dispatching behavior
# based on the type of the first non-self/cls argument.
#
# This is closer to type-based overloading while still following
# Python's dynamic-dispatch model.

from functools import singledispatchmethod


class Printer:
    @singledispatchmethod
    def display(self, value):
        raise TypeError(f"Unsupported type: {type(value).__name__}")

    @display.register
    def _(self, value: int):
        print(f"Integer: {value}")

    @display.register
    def _(self, value: str):
        print(f"String: {value}")

    @display.register
    def _(self, value: list):
        print(f"List: {value}")


printer = Printer()

printer.display(100)
printer.display("Python")
printer.display([1, 2, 3])


# ============================================================
# 11. DEFAULT ARGUMENTS VS *args
# ============================================================
# Default arguments are best when there is a known maximum number
# of parameters and each parameter has clear meaning.
#
# *args is better when the number of inputs is genuinely variable.

class Student:
    def marks(self, math, physics=0, chemistry=0):
        return math + physics + chemistry


s = Student()

print(s.marks(90))
print(s.marks(90, 85))
print(s.marks(90, 85, 88))


class Addition:
    def add(self, *numbers):
        return sum(numbers)


a = Addition()

print(a.add(10, 20))
print(a.add(10, 20, 30, 40, 50))


# ============================================================
# 12. METHOD OVERLOADING VS METHOD OVERRIDING
# ============================================================
# Do not confuse these concepts.
#
# Method Overloading:
# Same class + same method name + different parameter lists.
# Python does not support traditional overloading.
#
# Method Overriding:
# Child class provides a new implementation of a method inherited
# from its parent class.
#
# Method overriding IS fully supported in Python.

class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")


obj = Child()
obj.show()  # Child


# ============================================================
# 13. ADVANCED: OVERLOADING + INHERITANCE
# ============================================================
# A child can override a flexible method and provide its own
# behavior.

class Calculator:
    def calculate(self, *args):
        return sum(args)


class AdvancedCalculator(Calculator):
    def calculate(self, *args):
        if not args:
            return 0
        result = 1
        for value in args:
            result *= value
        return result


basic = Calculator()
advanced = AdvancedCalculator()

print(basic.calculate(2, 3, 4))      # 9
print(advanced.calculate(2, 3, 4))   # 24


# ============================================================
# 14. IMPORTANT PYTHON PHILOSOPHY
# ============================================================
# Python generally favors flexible interfaces instead of
# maintaining multiple methods with the same name.
#
# Common alternatives to traditional method overloading:
#
#     1. Default arguments
#     2. *args
#     3. **kwargs
#     4. Type checking
#     5. singledispatchmethod
#     6. Separate method names when operations are conceptually
#        different
#
# Example:
#
#     add_two(a, b)
#     add_three(a, b, c)
#
# can sometimes be clearer than forcing everything into one
# overloaded method.


# ============================================================
# KEY IDEA
# ============================================================
# Python does NOT select between multiple same-named methods based
# on argument count or type.
#
# This:
#
#     def add(self, a, b): ...
#     def add(self, a, b, c): ...
#
# does NOT create two overloaded methods.
#
# The second definition replaces the first.
#
# Instead, Python typically uses:
#
#     def add(self, a, b, c=0): ...
#
# or:
#
#     def add(self, *args): ...
#
# depending on the problem.
# ============================================================