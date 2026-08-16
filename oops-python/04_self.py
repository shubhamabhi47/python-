# ============================================================
# OOP INTERNAL MECHANICS: CLASS, OBJECT, self & MEMORY
# ============================================================
# A CLASS is a blueprint/template used to create objects.
# When Python executes a class definition, it creates a CLASS
# OBJECT in memory.
#
# Methods defined inside the class are functions stored as part
# of the class. Instance methods receive the current object as
# their first argument.
# ============================================================


# ============================================================
# 1. CLASS DEFINITION
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Conceptually:
#
# Employee
#   |
#   +-- __init__()  -> method/function
#
# The class itself exists as an object in memory.

print(type(Employee))
# <class 'type'>


# ============================================================
# 2. OBJECT INSTANTIATION
# ============================================================
# Calling Employee(...) creates an instance of Employee.
#
# Conceptually, Python performs:
#
# 1. Allocate/create a new Employee object.
# 2. Initialize that object through __init__().
# 3. Pass the newly created object as self.
#
# Important:
# __init__() initializes the object; it is not technically the
# method responsible for allocating the object.
# __new__() is responsible for creating/allocating the instance.
# ============================================================

e1 = Employee("Rahul", 50000)
e2 = Employee("Shantanu", 60000)


# ============================================================
# 3. UNDERSTANDING self
# ============================================================
# self refers to the CURRENT INSTANCE.
#
# When:
#
# e1 = Employee("Rahul", 50000)
#
# Python conceptually invokes:
#
# Employee.__init__(e1, "Rahul", 50000)
#
# Therefore inside __init__():
#
# self -> e1
# name -> "Rahul"
# salary -> 50000
#
# So:
# self.name = name
#
# becomes conceptually:
# e1.name = "Rahul"
#
# For e2:
#
# self -> e2
# self.name = name
#
# becomes:
# e2.name = "Shantanu"


print(e1.name)
print(e1.salary)

print(e2.name)
print(e2.salary)


# ============================================================
# 4. self IS NOT A KEYWORD
# ============================================================
# 'self' is a naming convention used for the current instance.
# Python does not require the name to literally be 'self'.
#
# However, using 'self' is strongly recommended because it is
# the standard Python convention and makes code readable.

class Demo:
    def show(current_object):
        print(current_object)


obj = Demo()
obj.show()

# Conceptually:
# obj.show()
# becomes:
# Demo.show(obj)


# ============================================================
# 5. INSTANCE ATTRIBUTES / INSTANCE STATE
# ============================================================
# Every object maintains its own instance attributes.
#
# e1 and e2 are separate objects, so their states are separate.
#
# Conceptual representation:
#
# e1 -> {name: "Rahul", salary: 50000}
# e2 -> {name: "Shantanu", salary: 60000}
#
# Changing e1 does not change e2.

e1.name = "Amit"

print(e1.name)  # Amit
print(e2.name)  # Shantanu


# ============================================================
# 6. OBJECT IDENTITY / MEMORY
# ============================================================
# id() returns an integer identifying an object during its
# lifetime. It can be used to demonstrate that e1 and e2 are
# different objects.

print(id(e1))
print(id(e2))
print(e1 is e2)  # False


# ============================================================
# 7. METHODS ARE DEFINED BY THE CLASS
# ============================================================
# Instance attributes belong to individual objects.
# Methods are defined on the class and can be used by its
# instances.
#
# When an instance method is accessed through an object, Python
# automatically binds that object as the first argument.
#
# Example:
#
# e1.show()
#
# is conceptually similar to:
#
# Employee.show(e1)
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)


e1 = Employee("Rahul", 50000)
e2 = Employee("Shantanu", 60000)

e1.show()
e2.show()

# Explicit equivalent:
Employee.show(e1)
Employee.show(e2)


# ============================================================
# 8. INSTANCE DICTIONARY
# ============================================================
# Normal Python objects commonly store instance attributes in
# __dict__.
#
# This allows us to inspect the object's instance state.

print(e1.__dict__)
print(e2.__dict__)

# Example output:
# {'name': 'Rahul', 'salary': 50000}
# {'name': 'Shantanu', 'salary': 60000}


# ============================================================
# 9. CLASS DICTIONARY
# ============================================================
# A class also has a namespace represented by __dict__.
# It contains class-level definitions such as methods.

print(Employee.__dict__.keys())


# ============================================================
# 10. INSTANCE ATTRIBUTE vs CLASS ATTRIBUTE
# ============================================================
# INSTANCE ATTRIBUTE:
# Stored separately for each object.
#
# CLASS ATTRIBUTE:
# Stored on the class and shared/looked up by instances unless
# an instance provides an attribute with the same name.

class Employee:
    company = "ABC Corp"

    def __init__(self, name):
        self.name = name


e1 = Employee("Rahul")
e2 = Employee("Shantanu")

print(e1.company)
print(e2.company)

# company is found through the class because it is not present
# in the individual instance dictionaries.


# ============================================================
# 11. ATTRIBUTE LOOKUP
# ============================================================
# When Python evaluates:
#
# e1.name
#
# it searches for the attribute according to Python's attribute
# lookup rules. For a normal instance, the instance namespace is
# checked before falling back to the class and its inheritance
# hierarchy.
#
# Therefore:
#
# e1.name -> instance attribute
# e1.company -> class attribute if absent from e1


print(e1.__dict__)
print(Employee.__dict__["company"])


# ============================================================
# 12. __new__() vs __init__()
# ============================================================
# Advanced distinction:
#
# __new__() -> creates/returns the new instance.
# __init__() -> initializes the already-created instance.
#
# Normal code usually only defines __init__().
# __new__() becomes important when controlling object creation,
# immutable types, metaclasses, singletons, etc.

class Employee:
    def __new__(cls, name, salary):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self, name, salary):
        print("Initializing object")
        self.name = name
        self.salary = salary


e = Employee("Rahul", 50000)


# ============================================================
# 13. COMPLETE INTERNAL FLOW
# ============================================================
# For:
#
# e1 = Employee("Rahul", 50000)
#
# Conceptually:
#
# Employee("Rahul", 50000)
#          |
#          v
# __new__(Employee, "Rahul", 50000)
#          |
#          v
# New Employee instance
#          |
#          v
# __init__(e1, "Rahul", 50000)
#          |
#          v
# e1.__dict__ = {
#     "name": "Rahul",
#     "salary": 50000
# }
#
# The exact implementation involves Python's object model,
# descriptors and type machinery, but this model is sufficient
# for understanding normal class/instance behavior.
# ============================================================