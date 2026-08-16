# ============================================================
# OOP: CLASSES AND OBJECTS IN PYTHON
# ============================================================
# CLASS:
# A user-defined blueprint/template/prototype used to create
# objects. It defines the structure, attributes and behaviors
# that its objects can have.
#
# OBJECT:
# An instance of a class. It is a runtime entity containing
# actual data and having access to the behaviors defined by
# its class.
#
# Analogy:
# Class  -> Form template
# Object -> Filled-out form
#
# One class can create many objects, and each object can contain
# different values while following the same class structure.
# ============================================================


# ============================================================
# BUILT-IN CLASSES
# ============================================================
# Python is object-oriented and essentially everything is an
# object, including numbers, strings, lists, functions, classes,
# etc.
#
# Examples:
# int   -> class for integers
# str   -> class for strings
# list  -> class for lists
# function -> class/type associated with function objects
#
# type() tells us the class/type of an object.

def demo_function():
    pass

print(type(10))             # <class 'int'>
print(type("Hello"))        # <class 'str'>
print(type([1, 2, 3]))      # <class 'list'>
print(type(demo_function))  # <class 'function'>


# ============================================================
# USER-DEFINED CLASS
# ============================================================
# The 'class' keyword creates a new class.
#
# A class body can contain:
# - Attributes -> data/state
# - Methods    -> behavior/operations
#
# 'pass' means the class currently has no implementation.
# ============================================================

class Email:
    pass


# ============================================================
# OBJECT / INSTANCE CREATION
# ============================================================
# Calling a class creates an object.
# This process is called INSTANTIATION.
#
# Email() -> creates an instance of Email
# my_email -> reference to that instance
#
# The class is the blueprint; my_email is the actual object.
# ============================================================

my_email = Email()

print(type(my_email))
# <class '__main__.Email'>


# ============================================================
# MULTIPLE OBJECTS
# ============================================================
# A single class can create multiple independent objects.
# Each object has its own identity and can hold different data.

email1 = Email()
email2 = Email()

print(email1 is email2)  # False


# ============================================================
# CLASS WITH ATTRIBUTES AND METHODS
# ============================================================
# A practical class usually defines:
# - Attributes -> what the object HAS
# - Methods    -> what the object CAN DO
#
# __init__() is the constructor/initializer method.
# It executes automatically when an object is instantiated.
#
# self refers to the current object.
# ============================================================

class Email:
    def __init__(self, sender, receiver, subject):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject

    def send(self):
        print(f"Email sent from {self.sender} to {self.receiver}")

    def show_details(self):
        print(f"From: {self.sender}")
        print(f"To: {self.receiver}")
        print(f"Subject: {self.subject}")


email1 = Email("alice@gmail.com", "bob@gmail.com", "Meeting")
email2 = Email("john@gmail.com", "sam@gmail.com", "Project")

email1.show_details()
email1.send()

email2.show_details()
email2.send()


# ============================================================
# CLASS VS OBJECT
# ============================================================
# CLASS:
# - Blueprint/template
# - Defines structure and behavior
# - Exists as a type definition
#
# OBJECT:
# - Concrete instance of a class
# - Stores actual values
# - Exists at runtime
#
# Example:
# Email              -> class
# email1, email2     -> objects
#
# Email.sender       -> describes what instances can have
# email1.sender      -> actual value stored in one instance
# ============================================================


# ============================================================
# IMPORTANT PYTHON OBJECT MODEL
# ============================================================
# In Python, classes themselves are also objects.
# The type() function can be used to inspect an object's type.
#
# For example:
#
# type(10)       -> int
# type([])       -> list
# type(email1)   -> Email
#
# Python's object model is therefore highly dynamic and
# everything is treated uniformly as an object at runtime.
# ============================================================

print(type(10))
print(type(email1))
print(type(Email))


# ============================================================
# CORE IDEA
# ============================================================
# CLASS  -> Defines what an object should look like and do.
# OBJECT -> Actual instance containing concrete state.
#
# The relationship can be visualized as:
#
#              CLASS
#                |
#        -----------------
#        |       |       |
#      obj1    obj2    obj3
#
# Same structure/behavior, potentially different data.
#
# Understanding CLASS + OBJECT is the foundation for:
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism
# ============================================================