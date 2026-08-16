# ============================================================
# INSTANCE VARIABLES AND INSTANCE METHODS
# ============================================================
# Instance variables belong to a specific object.
# Each object maintains its own independent instance state.
#
# They are commonly created using:
# self.attribute = value
#
# Changes to one object's instance variables do not normally
# affect another object's instance variables.
# ============================================================


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Rahul", 90)
s2 = Student("Akshay", 85)

print(s1.name)
print(s2.name)

s1.name = "Raj"

print(s1.name)  # Raj
print(s2.name)  # Akshay


# ============================================================
# DELETING INSTANCE VARIABLES
# ============================================================
# del removes an attribute from a particular object's namespace.
#
# It does not remove the attribute from other objects.

del s1.name

print(s2.name)

# Accessing s1.name now would raise AttributeError.


# ============================================================
# INSTANCE METHODS
# ============================================================
# An instance method operates on a particular object's state.
#
# Its first parameter receives the current instance.
# By convention this parameter is named self.
#
# Calling:
# s1.display()
#
# binds s1 to self.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


s1 = Student("Rahul", 90)
s2 = Student("Akshay", 85)

s1.display()
s2.display()


# ============================================================
# MODIFYING INSTANCE STATE THROUGH METHODS
# ============================================================
# Instance methods can change the state of the object they
# operate on.
#
# This keeps related data and the operations on that data inside
# the same class.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def change_data(self, new_name, new_marks):
        self.name = new_name
        self.marks = new_marks


s1 = Student("Rahul", 90)

s1.change_data("Vijay", 95)
s1.display()


# ============================================================
# DIRECT MODIFICATION vs METHOD-BASED MODIFICATION
# ============================================================
# Attributes can technically be modified directly:
#
# s1.marks = 95
#
# But a method can provide controlled logic/validation around
# state changes.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def set_marks(self, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks = marks


s1 = Student("Rahul", 90)

s1.set_marks(95)
print(s1.marks)


# ============================================================
# INSTANCE STATE
# ============================================================
# The state of an object is represented by its instance
# attributes.
#
# Different objects can therefore have different states while
# using the same class and methods.

s1 = Student("Rahul", 90)
s2 = Student("Akshay", 85)

print(s1.__dict__)
print(s2.__dict__)


# ============================================================
# KEY IDEA
# ============================================================
# INSTANCE VARIABLE:
#     Data belonging to one particular object.
#
# INSTANCE METHOD:
#     Behavior that operates on a particular object.
#
# Object state:
#     self.name
#     self.marks
#
# Object behavior:
#     display()
#     change_data()
#     set_marks()
#
# This combination of object-specific state + behavior is a core
# mechanism behind encapsulation in OOP.
# ============================================================

# creating instance variable:-
    # 1) Using constructor    ----> Using self commong u know that it is the standard method
    # 2) Using instance method  ---> We will see
    # 3) Outside the class ---> Using dot method like emp1.salary = 1,00,000 

