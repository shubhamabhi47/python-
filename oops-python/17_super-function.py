# ============================================================
# super()
# ============================================================
# super() provides access to the next class in the inheritance
# hierarchy according to Python's Method Resolution Order (MRO).
#
# It is commonly used to:
# - Call a parent/base class constructor.
# - Extend an inherited method.
# - Reuse parent behavior without duplicating its code.
#
# super() is especially important in multiple inheritance because
# it follows MRO instead of simply hard-coding a parent class.
# ============================================================


# ============================================================
# 1. CALLING THE PARENT CONSTRUCTOR
# ============================================================
# Mobile overrides __init__(), so Computer.__init__() would not
# execute automatically.
#
# super().__init__() explicitly delegates initialization to the
# next class in the MRO.

class Computer:
    def __init__(self):
        print("Computer class constructor called")
        self.ram = "8GB"
        self.storage = "512GB"


class Mobile(Computer):
    def __init__(self):
        super().__init__()
        print("Mobile class constructor called")
        self.model = "iPhone"


m1 = Mobile()

print(m1.ram)
print(m1.storage)
print(m1.model)


# ============================================================
# 2. PASSING ARGUMENTS THROUGH super()
# ============================================================
# The child can receive data and forward the relevant arguments
# to the parent constructor.

class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Mobile(Computer):
    def __init__(self, ram, storage, model):
        super().__init__(ram, storage)
        self.model = model


m1 = Mobile("16GB", "1TB", "Samsung")

print(m1.ram)
print(m1.storage)
print(m1.model)


# ============================================================
# 3. CALLING PARENT METHODS
# ============================================================
# super() is not limited to __init__().
# It can call other methods defined higher in the MRO.

class Computer:
    def display(self):
        print("Hello World from Computer")


class Mobile(Computer):
    def show(self):
        super().display()


m1 = Mobile()
m1.show()


# ============================================================
# 4. EXTENDING PARENT BEHAVIOR
# ============================================================
# A child can reuse the parent's implementation and then add
# its own behavior instead of rewriting the entire method.

class Employee:
    def show(self):
        print("Employee information")


class Manager(Employee):
    def show(self):
        super().show()
        print("Manager information")


m = Manager()
m.show()


# ============================================================
# 5. super() vs DIRECT PARENT CLASS CALL
# ============================================================
# This works:
#
#     Employee.show(self)
#
# But it hard-codes the parent class.
#
# Prefer:
#
#     super().show()
#
# because super() follows the MRO and supports cooperative
# multiple inheritance.


# ============================================================
# 6. super() AND MULTIPLE INHERITANCE
# ============================================================
# super() follows the Method Resolution Order rather than simply
# calling a fixed parent.
#
# Each class can cooperate by calling super(), allowing the entire
# MRO chain to execute.

class A:
    def show(self):
        print("A")
        super().show()


class B:
    def show(self):
        print("B")
        super().show()


class C(A, B):
    def show(self):
        print("C")
        super().show()


class End:
    def show(self):
        print("End")


# To make the chain terminate cleanly:
class A:
    def show(self):
        print("A")
        super().show()


class B:
    def show(self):
        print("B")
        super().show()


class C(A, B):
    def show(self):
        print("C")
        super().show()


# object has no useful show(), so use a terminating base explicitly
# in cooperative designs when necessary.


# ============================================================
# 7. PRACTICAL MULTIPLE-INHERITANCE PATTERN
# ============================================================

class Base:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NameMixin(Base):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)


class SalaryMixin(Base):
    def __init__(self, salary, **kwargs):
        self.salary = salary
        super().__init__(**kwargs)


class Employee(NameMixin, SalaryMixin):
    def __init__(self, name, salary):
        super().__init__(name=name, salary=salary)


e = Employee("Rahul", 50000)

print(e.name)
print(e.salary)


# ============================================================
# 8. MRO
# ============================================================
# super() follows the class's Method Resolution Order.
#
# __mro__ shows the order Python uses to search for methods.

print(Employee.__mro__)


# ============================================================
# KEY IDEA
# ============================================================
# super()
#     ↓
# Accesses the next implementation in the MRO.
#
# Common usage:
#
# super().__init__(...)
# super().method(...)
#
# It allows child classes to EXTEND parent behavior instead of
# completely replacing it and avoids unnecessary duplication.
#
# IMPORTANT:
# super() does not literally mean "call my immediate parent".
# More precisely, it means "continue lookup from the next class
# in the MRO".
# ============================================================


# ============================================================
# Another method to pass parameters
# ============================================================
class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Mobile(Computer):
    def __init__(self):
        super().__init__('12gb','512gb')
        self.model = 'Iphone 17 Pro Max'

Apple = Mobile()
print(Apple.__dict__)

# ============================================================
# Another method to pass parameters
# ============================================================
class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Mobile(Computer):
    def __init__(self , ram , storage):
        super().__init__(ram , storage)
        self.model = 'Iphone 17 Pro Max'

Apple = Mobile('12gb','512gb')
print(Apple.__dict__)

# --> In above example values or argumetns get passed from Mobile('12gb','512gb') to Mobile class 
# constructor and then super()  method will pass that values to the the parent class constructor 