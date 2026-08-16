# ============================================================
# ENCAPSULATION
# ============================================================
# Encapsulation means bundling data and the methods that operate
# on that data inside a class.
#
# It also allows a class to control how its internal state is
# accessed or modified.
#
# Python does NOT provide Java-style strict private members.
# Instead, it uses naming conventions and name mangling.
# ============================================================


# ============================================================
# 1. BASIC ENCAPSULATION
# ============================================================
# Data and behavior are grouped inside one class.
#
# However, public attributes can still be accessed and modified
# directly from outside.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


emp = Employee("Rahul", 50000)

emp.display()
print(emp.name)

emp.salary = -1000  # Direct modification is possible.


# ============================================================
# 2. PUBLIC MEMBERS
# ============================================================
# Attributes without a leading underscore are public by
# convention and can be accessed normally.

class Finance:
    def __init__(self):
        self.revenue = 100000
        self.number_of_employees = 50


f = Finance()

print(f.revenue)
print(f.number_of_employees)

f.revenue = 200000


# ============================================================
# 3. PRIVATE MEMBERS (__name)
# ============================================================
# A double leading underscore triggers NAME MANGLING.
#
# __revenue is internally transformed approximately into:
#
# _Finance__revenue
#
# This prevents accidental access/name collisions and signals
# that the attribute is intended for internal use.
#
# It is NOT true access restriction.

class Finance:
    def __init__(self):
        self.revenue = 100000
        self.__number_of_employees = 50


f = Finance()

print(f.revenue)

# print(f.__number_of_employees)  # AttributeError


# ============================================================
# 4. GETTER AND SETTER FOR CONTROLLED ACCESS
# ============================================================
# A getter reads internal state.
# A setter modifies internal state after applying rules.
#
# This creates a controlled interface around the data.

class Finance:
    def __init__(self):
        self.__revenue = 100000

    def get_revenue(self):
        return self.__revenue

    def set_revenue(self, value):
        if value <= 0:
            raise ValueError("Revenue must be positive")
        self.__revenue = value


f = Finance()

print(f.get_revenue())

f.set_revenue(200000)

print(f.get_revenue())


# ============================================================
# 5. @property: PYTHONIC ENCAPSULATION
# ============================================================
# Python commonly uses @property instead of explicit get_/set_
# methods.
#
# It provides controlled access while allowing normal attribute
# syntax:
#
# f.revenue
# f.revenue = 200000

class Finance:
    def __init__(self, revenue):
        self.revenue = revenue

    @property
    def revenue(self):
        return self._revenue

    @revenue.setter
    def revenue(self, value):
        if value <= 0:
            raise ValueError("Revenue must be positive")
        self._revenue = value


f = Finance(100000)

print(f.revenue)

f.revenue = 200000

print(f.revenue)


# ============================================================
# 6. PROTECTED CONVENTION (_name)
# ============================================================
# A single leading underscore means:
#
# _revenue
#
# "This is intended for internal/subclass use."
#
# Python does not prevent external access.
#
# It is a convention, unlike name mangling with __name.

class Finance:
    def __init__(self):
        self._revenue = 100000


f = Finance()

print(f._revenue)  # Technically accessible, but discouraged.


# ============================================================
# 7. NAME MANGLING
# ============================================================
# Python transforms a double-leading-underscore attribute to
# _ClassName__attribute.
#
# Example:
#
# __revenue
#      ↓
# _Finance__revenue

class Finance:
    def __init__(self):
        self.__revenue = 100000


f = Finance()

print(f.__dict__)

# Name-mangled access:
print(f._Finance__revenue)


# ============================================================
# 8. WHY NAME MANGLING EXISTS
# ============================================================
# Name mangling is particularly useful in inheritance because it
# prevents accidental attribute collisions between a parent and
# child class.
#
# It is NOT designed as a security mechanism.

class Parent:
    def __init__(self):
        self.__value = "Parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "Child"


obj = Child()

print(obj.__dict__)

print(obj._Parent__value)
print(obj._Child__value)


# ============================================================
# KEY IDEA
# ============================================================
# Encapsulation:
#     Bundle state + behavior together.
#
# Public:
#     name
#
# Protected convention:
#     _name
#
# Private/name-mangled:
#     __name
#
# Getter/Setter:
#     Controlled access through methods.
#
# @property:
#     Pythonic interface for controlled attribute access.
#
# IMPORTANT:
# Python's __name is NOT truly private.
# Name mangling mainly prevents accidental access and naming
# conflicts; it does not provide security.
# ============================================================

class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value