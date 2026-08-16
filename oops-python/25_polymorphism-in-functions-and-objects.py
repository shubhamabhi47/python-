# ============================================================
# DUCK TYPING / RUNTIME POLYMORPHISM
# ============================================================
# Duck typing is Python's approach to polymorphism where the
# object's behavior matters more than its concrete class/type.
#
# If an object provides the required methods, it can be used,
# regardless of which class it belongs to.
#
# Core idea:
#     "Don't ask what the object is; ask what it can do."
# ============================================================


# ============================================================
# 1. SAME INTERFACE, DIFFERENT IMPLEMENTATION
# ============================================================
# Ferrari and BMW both provide car_details() and max_speed(),
# but each class implements them differently.

class Ferrari:
    def car_details(self):
        print("Ferrari: Petrol")

    def max_speed(self):
        print("Ferrari: 300 km/h")


class BMW:
    def car_details(self):
        print("BMW: Diesel")

    def max_speed(self):
        print("BMW: 240 km/h")


# ============================================================
# 2. POLYMORPHIC FUNCTION
# ============================================================
# The function does not check whether obj is Ferrari or BMW.
# It only assumes that obj provides the required methods.

def show_car(obj):
    obj.car_details()
    obj.max_speed()


f = Ferrari()
b = BMW()

show_car(f)
show_car(b)


# ============================================================
# 3. TRUE DUCK TYPING
# ============================================================
# A completely unrelated class can also work if it provides
# the same required interface.
#
# No inheritance is required.

class Tesla:
    def car_details(self):
        print("Tesla: Electric")

    def max_speed(self):
        print("Tesla: 250 km/h")


t = Tesla()

show_car(t)


# ============================================================
# 4. DUCK TYPING VS isinstance()
# ============================================================
# Duck typing focuses on BEHAVIOR.
#
# Avoid unnecessarily doing this:
#
#     if isinstance(obj, Ferrari):
#         ...
#     elif isinstance(obj, BMW):
#         ...
#
# Instead, simply use the required interface when appropriate.

def start_car(car):
    car.start()


class Ferrari:
    def start(self):
        print("Ferrari started")


class BMW:
    def start(self):
        print("BMW started")


class Bike:
    def start(self):
        print("Bike started")


for vehicle in [Ferrari(), BMW(), Bike()]:
    start_car(vehicle)


# ============================================================
# 5. POLYMORPHISM WITH A COMMON INTERFACE
# ============================================================
# Different objects can provide the same operation with different
# implementations.

class Payment:
    def pay(self, amount):
        raise NotImplementedError


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


def process_payment(payment, amount):
    payment.pay(amount)


payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    process_payment(payment, 1000)


# ============================================================
# 6. METHOD OVERRIDING VS DUCK TYPING
# ============================================================
# METHOD OVERRIDING:
#     Usually occurs through inheritance.
#
# DUCK TYPING:
#     Does NOT require inheritance.
#
# Both can provide runtime polymorphism, but the mechanism differs.

class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")


def make_sound(animal):
    animal.speak()


for animal in [Dog(), Cat()]:
    make_sound(animal)


# ============================================================
# 7. DUCK TYPING WITHOUT A COMMON BASE CLASS
# ============================================================
# Dog and Robot are unrelated classes, but both provide walk().
# Therefore the same function can operate on both.

class Dog:
    def walk(self):
        print("Dog is walking")


class Robot:
    def walk(self):
        print("Robot is walking")


def make_walk(obj):
    obj.walk()


make_walk(Dog())
make_walk(Robot())


# ============================================================
# 8. ADVANCED: DEPENDENCY ON BEHAVIOR
# ============================================================
# The function depends only on the behavior it needs.
# This reduces coupling between components.

class EmailService:
    def send(self, message):
        print(f"Email: {message}")


class SMSService:
    def send(self, message):
        print(f"SMS: {message}")


class NotificationService:
    def send(self, message):
        print(f"Notification: {message}")


def notify(service, message):
    service.send(message)


services = [
    EmailService(),
    SMSService(),
    NotificationService()
]

for service in services:
    notify(service, "Order confirmed")


# ============================================================
# 9. BUILT-IN POLYMORPHISM
# ============================================================
# Python's built-in functions also use object protocols.

print(len("Python"))
print(len([10, 20, 30]))
print(len({"a": 1, "b": 2}))


# ============================================================
# 10. OPERATOR POLYMORPHISM
# ============================================================
# The same + operator performs different operations depending
# on the objects involved.

print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])


# ============================================================
# 11. POLYMORPHIC ITERATION
# ============================================================
# The same for-loop can work with different iterable objects
# because they follow Python's iteration protocol.

data = [
    [1, 2, 3],
    (4, 5, 6),
    {7, 8, 9},
    "Python"
]

for item in data:
    for value in item:
        print(value)


# ============================================================
# 12. STRUCTURAL THINKING
# ============================================================
# In duck typing, this function does not care about the object's
# class. It only requires that the object has a calculate() method.

def calculate_total(obj):
    return obj.calculate()


class Invoice:
    def calculate(self):
        return 5000


class Salary:
    def calculate(self):
        return 80000


class Tax:
    def calculate(self):
        return 15000


objects = [Invoice(), Salary(), Tax()]

for obj in objects:
    print(calculate_total(obj))


# ============================================================
# 13. WHAT HAPPENS IF THE REQUIRED METHOD DOES NOT EXIST?
# ============================================================
# Duck typing performs the operation and lets Python raise an
# AttributeError if the required behavior is missing.

class WrongObject:
    def display(self):
        print("Display")


def run(obj):
    obj.start()


# run(WrongObject())
# AttributeError: 'WrongObject' object has no attribute 'start'


# ============================================================
# 14. EAFP STYLE
# ============================================================
# Python commonly follows EAFP:
#
#     Easier to Ask Forgiveness than Permission
#
# Instead of checking the object's type first, perform the
# required operation and handle failure if necessary.

def start(obj):
    try:
        obj.start()
    except AttributeError:
        print("Object does not support start()")


class Car:
    def start(self):
        print("Car started")


class Person:
    pass


start(Car())
start(Person())


# ============================================================
# 15. LBYL VS EAFP
# ============================================================
# LBYL = Look Before You Leap
# EAFP = Easier to Ask Forgiveness than Permission
#
# LBYL:
#
#     if hasattr(obj, "start"):
#         obj.start()
#
# EAFP:
#
#     try:
#         obj.start()
#     except AttributeError:
#         ...
#
# EAFP is common in Python when duck typing is appropriate.


# ============================================================
# 16. PROTOCOL-BASED DESIGN
# ============================================================
# A protocol describes the behavior an object must provide.
#
# Example:
#
#     A "printable" object must provide print_data().
#
# The class itself is less important than whether it satisfies
# the required behavior.

class Report:
    def print_data(self):
        print("Printing report")


class Invoice:
    def print_data(self):
        print("Printing invoice")


def print_document(document):
    document.print_data()


print_document(Report())
print_document(Invoice())


# ============================================================
# 17. STATIC TYPE CHECKING WITH Protocol (ADVANCED)
# ============================================================
# typing.Protocol lets us explicitly describe a structural
# interface for static type checkers.
#
# Runtime inheritance is NOT required.

from typing import Protocol


class Printable(Protocol):
    def print_data(self) -> None:
        ...


class Report:
    def print_data(self):
        print("Report printed")


class Invoice:
    def print_data(self):
        print("Invoice printed")


def print_document(document: Printable):
    document.print_data()


print_document(Report())
print_document(Invoice())


# ============================================================
# 18. IMPORTANT DISTINCTION
# ============================================================
# INHERITANCE POLYMORPHISM:
#
#     Base
#      ↓
#    Child
#
# Child overrides a method from Base.
#
#
# DUCK TYPING:
#
#     Class A ──┐
#     Class B ──┼──> same required behavior
#     Class C ──┘
#
# Classes don't need to share a parent.
#
#
# CORE DIFFERENCE:
#
# Inheritance polymorphism -> relationship-based
# Duck typing             -> behavior-based
# ============================================================


# ============================================================
# FINAL EXAMPLE: REAL-WORLD POLYMORPHISM
# ============================================================

class Razorpay:
    def pay(self, amount):
        print(f"Razorpay payment: ₹{amount}")


class Stripe:
    def pay(self, amount):
        print(f"Stripe payment: ₹{amount}")


class PayPal:
    def pay(self, amount):
        print(f"PayPal payment: ₹{amount}")


def checkout(payment_gateway, amount):
    payment_gateway.pay(amount)


gateways = [
    Razorpay(),
    Stripe(),
    PayPal()
]

for gateway in gateways:
    checkout(gateway, 2500)


# ============================================================
# CORE IDEA
# ============================================================
# Polymorphism means ONE INTERFACE can work with MANY FORMS.
#
# Same function:
#     checkout()
#
# Same method:
#     pay()
#
# Different objects:
#     Razorpay
#     Stripe
#     PayPal
#
# Different implementations:
#     Each object's pay() behaves differently.
#
# Python's dynamic typing + duck typing makes this especially
# powerful because the caller usually needs to know WHAT an
# object CAN DO rather than WHAT CLASS it belongs to.
# ============================================================