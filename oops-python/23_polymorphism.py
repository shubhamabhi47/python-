# ============================================================
# POLYMORPHISM
# ============================================================
# Polymorphism means "many forms".
#
# The same operation/interface can behave differently depending
# on the object or data involved.
#
# Major forms in Python:
# 1. Operator polymorphism / operator overloading
# 2. Built-in function polymorphism
# 3. Duck typing
# 4. Method overriding
# 5. Abstract interfaces
#
# Python achieves polymorphism mainly through dynamic typing and
# runtime method dispatch.
# ============================================================


# ============================================================
# 1. OPERATOR POLYMORPHISM
# ============================================================
# The + operator behaves differently depending on the operands.
#
# int + int       -> arithmetic addition
# str + str       -> string concatenation
# list + list     -> list concatenation

print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])


# ============================================================
# 2. OPERATOR OVERLOADING WITH CUSTOM OBJECTS
# ============================================================
# Operators internally call special/dunder methods.
#
# a + b
#     ↓
# a.__add__(b)
#
# By implementing __add__, we can define what + means for our
# custom objects.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2

print(p3)


# ============================================================
# 3. MORE OPERATOR OVERLOADING
# ============================================================
# Common operator -> special method:
#
# +   -> __add__()
# -   -> __sub__()
# *   -> __mul__()
# /   -> __truediv__()
# //  -> __floordiv__()
# %   -> __mod__()
# **  -> __pow__()
# ==  -> __eq__()
# <   -> __lt__()
# >   -> __gt__()
# <=  -> __le__()
# >=  -> __ge__()
# len -> __len__()
# str -> __str__()
# repr -> __repr__()

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount

    def __repr__(self):
        return f"Money({self.amount})"


m1 = Money(500)
m2 = Money(300)

print(m1 + m2)
print(m1 == m2)
print(m1 == Money(500))


# ============================================================
# 4. WHY NotImplemented IS IMPORTANT
# ============================================================
# Returning NotImplemented tells Python:
# "I don't know how to perform this operation with this type."
#
# It is different from raising an exception directly and allows
# Python to try the reflected operation on the other operand.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return NotImplemented

    def __repr__(self):
        return f"Number({self.value})"


print(Number(10) + Number(20))


# ============================================================
# 5. BUILT-IN FUNCTION POLYMORPHISM
# ============================================================
# The same built-in function can work with different object types.
#
# len() internally relies on the object's __len__() behavior.

print(len("Python"))
print(len([10, 20, 30]))
print(len({"a": 1, "b": 2}))


# ============================================================
# 6. CUSTOM __len__()
# ============================================================
# We can make our own objects compatible with len().

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Rahul", "Aman", "Raj"])

print(len(team))


# ============================================================
# 7. DUCK TYPING
# ============================================================
# Duck typing focuses on behavior rather than the concrete type.
#
# The function does not ask:
# "Are you a Company?"
#
# It asks indirectly:
# "Can you perform reverse()?"
#
# If the required behavior exists, the object can be used.

class Company:
    def reverse(self):
        return "Reversing Company process"


class ListContainer:
    def reverse(self):
        return "Reversing List process"


def perform_reverse(obj):
    print(obj.reverse())


perform_reverse(Company())
perform_reverse(ListContainer())


# ============================================================
# 8. DUCK TYPING WITH COMPLETELY UNRELATED CLASSES
# ============================================================
# These classes have no inheritance relationship.
# They only share the required interface.

class Dog:
    def speak(self):
        print("Dog says Woof")


class Human:
    def speak(self):
        print("Human says Hello")


class Robot:
    def speak(self):
        print("Robot says Beep")


def make_speak(obj):
    obj.speak()


make_speak(Dog())
make_speak(Human())
make_speak(Robot())


# ============================================================
# 9. DUCK TYPING IS MORE FLEXIBLE THAN TYPE CHECKING
# ============================================================
# Avoid unnecessarily checking exact types.
#
# BAD:
#
# if type(obj) == Dog:
#     ...
#
# Better:
# simply use the required behavior.

def start_engine(vehicle):
    vehicle.start()


class Car:
    def start(self):
        print("Car engine started")


class Bike:
    def start(self):
        print("Bike engine started")


start_engine(Car())
start_engine(Bike())


# ============================================================
# 10. METHOD OVERRIDING
# ============================================================
# A child class can provide its own implementation of a method
# defined by the parent.
#
# The same method call can therefore produce different behavior.

class Animal:
    def sound(self):
        print("Some animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()


# ============================================================
# 11. RUNTIME POLYMORPHISM
# ============================================================
# The exact implementation is determined at runtime based on
# the actual object.
#
# animal.sound()
#
# If animal refers to Dog -> Dog.sound()
# If animal refers to Cat -> Cat.sound()

animal = Dog()
animal.sound()

animal = Cat()
animal.sound()


# ============================================================
# 12. COMMON INTERFACE WITH DIFFERENT IMPLEMENTATIONS
# ============================================================
# Different classes can implement the same operation differently.

class Payment:
    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


payments = [
    CreditCardPayment(),
    UpiPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(1000)


# ============================================================
# 13. POLYMORPHISM WITH ABSTRACT BASE CLASSES
# ============================================================
# For larger applications, we can formally define an interface
# using ABC and @abstractmethod.
#
# Every concrete child must implement the required method.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shapes = [
    Circle(5),
    Rectangle(10, 4)
]

for shape in shapes:
    print(shape.area())


# ============================================================
# 14. POLYMORPHISM + isinstance()
# ============================================================
# isinstance() can be useful when behavior genuinely differs
# based on type, but excessive type checking can reduce the
# flexibility of polymorphic code.

def calculate_area(shape):
    return shape.area()


print(calculate_area(Circle(5)))
print(calculate_area(Rectangle(10, 4)))


# ============================================================
# 15. POLYMORPHISM WITH BUILT-IN SORTED()
# ============================================================
# sorted() can work with many iterable types and can also use a
# common key function to operate on different objects.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.name}: {self.marks}"


students = [
    Student("Rahul", 85),
    Student("Aman", 95),
    Student("Raj", 75)
]

students.sort(key=lambda student: student.marks)

print(students)


# ============================================================
# 16. STR() POLYMORPHISM
# ============================================================
# print() can represent different objects because it ultimately
# uses string conversion behavior.

class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee: {self.name}"


employee = Employee("Rahul")

print(employee)


# ============================================================
# 17. POLYMORPHISM THROUGH A COMMON FUNCTION
# ============================================================
# A function can operate on multiple object types as long as they
# provide the expected behavior.

class PDF:
    def export(self):
        print("Exporting PDF")


class Excel:
    def export(self):
        print("Exporting Excel")


class CSV:
    def export(self):
        print("Exporting CSV")


def export_file(file):
    file.export()


for file in [PDF(), Excel(), CSV()]:
    export_file(file)


# ============================================================
# 18. ADVANCED: STRUCTURAL TYPING WITH PROTOCOL
# ============================================================
# Protocol provides static type-checking support for duck typing.
#
# The class does not need to explicitly inherit from the Protocol.
# If it provides the required structure, type checkers can treat
# it as compatible.

from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None:
        ...


class CircleDrawable:
    def draw(self):
        print("Drawing Circle")


class SquareDrawable:
    def draw(self):
        print("Drawing Square")


def render(obj: Drawable):
    obj.draw()


render(CircleDrawable())
render(SquareDrawable())


# ============================================================
# 19. POLYMORPHISM VS OVERLOADING
# ============================================================
# Python does NOT support traditional compile-time method
# overloading like Java/C++.
#
# Defining the same method multiple times simply replaces the
# previous definition.
#
# Python usually achieves flexible behavior using:
# - default arguments
# - *args / **kwargs
# - duck typing
# - type checking when necessary
# - singledispatch when true type-based dispatch is required.

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))


# ============================================================
# 20. ADVANCED: SINGLE DISPATCH
# ============================================================
# functools.singledispatch allows different implementations
# based on the type of the first argument.

from functools import singledispatch


@singledispatch
def display(value):
    print(f"Generic: {value}")


@display.register
def _(value: int):
    print(f"Integer: {value}")


@display.register
def _(value: str):
    print(f"String: {value}")


@display.register
def _(value: list):
    print(f"List: {value}")


display(10)
display("Python")
display([1, 2, 3])
display(3.14)


# ============================================================
# 21. POLYMORPHISM: THE BIG PICTURE
# ============================================================
# Same operation:
#
#     obj.show()
#
# Different objects:
#
#     Dog    -> Bark
#     Cat    -> Meow
#     Robot  -> Beep
#
# The caller only depends on the common behavior.
#
# This reduces coupling and makes code easier to extend.
#
# A good polymorphic design allows us to add a new class without
# changing the existing code that uses the common interface.
# ============================================================


# ============================================================
# KEY IDEA
# ============================================================
# POLYMORPHISM = ONE INTERFACE / OPERATION + MANY BEHAVIORS
#
# Operator polymorphism:
#     1 + 2
#     "A" + "B"
#
# Operator overloading:
#     __add__, __eq__, __len__, etc.
#
# Built-in polymorphism:
#     len(), str(), sorted(), print(), etc.
#
# Duck typing:
#     "If the object provides the required behavior, use it."
#
# Method overriding:
#     Parent interface + different child implementations.
#
# ABC:
#     Explicit contract for subclasses.
#
# Protocol:
#     Static-typing-friendly structural/duck typing.
#
# The main goal is to write code that depends on BEHAVIOR rather
# than unnecessary knowledge of the object's exact type.
# ============================================================