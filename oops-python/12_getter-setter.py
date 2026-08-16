# ============================================================
# GETTER AND SETTER METHODS
# ============================================================
# Getter -> controlled way to READ an attribute.
# Setter -> controlled way to MODIFY an attribute.
#
# They are commonly used with internal/private attributes when
# validation, transformation or additional logic is required.
#
# In Python, get_/set_ methods are a convention, not a mandatory
# language rule. Python's @property is often preferred for a
# cleaner attribute-like interface.
# ============================================================


class Employee:
    def __init__(self):
        self.__name = None

    def set_name(self, name):
        self.__name = name
        print("Name has been set")

    def get_name(self):
        return self.__name


e1 = Employee()

e1.set_name("Raj")
print(e1.get_name())


# ============================================================
# SETTER WITH VALIDATION
# ============================================================
# A major advantage of a setter is that invalid data can be
# rejected before modifying the object's internal state.

class Employee:
    def __init__(self):
        self.__name = None

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self.__name = name.strip()

    def get_name(self):
        return self.__name


e1 = Employee()
e1.set_name(" Rahul ")
print(e1.get_name())


# ============================================================
# GETTER/SETTER USING @property
# ============================================================
# Python provides @property to expose methods using normal
# attribute syntax.
#
# Instead of:
#     e1.get_name()
#     e1.set_name("Raj")
#
# we can write:
#     e1.name
#     e1.name = "Raj"
#
# This provides encapsulation while keeping a clean interface.
# ============================================================

class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()


e1 = Employee("Raj")

print(e1.name)

e1.name = "Rahul"
print(e1.name)


# ============================================================
# READ-ONLY PROPERTY
# ============================================================
# If only @property is defined and no setter is provided, the
# attribute becomes read-only through normal attribute syntax.

class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


e1 = Employee("Raj")

print(e1.name)

# e1.name = "Rahul"
# Raises AttributeError because no setter exists.


# ============================================================
# PROPERTY WITH VALIDATION AND DERIVED DATA
# ============================================================
# Properties are useful when accessing an attribute requires
# computation or validation while still providing simple syntax.

class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def annual_salary(self):
        return self.salary * 12


e1 = Employee(50000)

print(e1.annual_salary)


# ============================================================
# IMPORTANT DISTINCTION
# ============================================================
# get_/set_ methods:
#
#     e.name = e.get_name()
#     e.set_name("Raj")
#
# @property:
#
#     e.name
#     e.name = "Raj"
#
# Both can provide controlled access, but @property follows
# Python's idiomatic attribute-style interface.
#
# Use getters/setters or properties when access requires:
# - Validation
# - Transformation
# - Computation
# - Access control
# - Maintaining invariants
# ============================================================