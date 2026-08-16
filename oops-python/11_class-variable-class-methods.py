# ============================================================
# CLASS VARIABLES AND CLASS METHODS
# ============================================================
# CLASS VARIABLE:
# A variable defined inside a class but outside instance methods.
# It belongs to the class and is normally shared through class
# lookup by all instances.
#
# INSTANCE VARIABLE:
# Belongs specifically to one object.
#
# Class variable -> Employee.company_name
# Instance variable -> e1.name
# ============================================================


class Employee:
    company_name = "Codeyug"

    def __init__(self, name):
        self.name = name


# Access through the class
print(Employee.company_name)

# Access through an instance
e1 = Employee("Rahul")
e2 = Employee("Shantanu")

print(e1.company_name)
print(e2.company_name)


# ============================================================
# CLASS VARIABLE SHADOWING
# ============================================================
# Assigning through an instance does NOT normally change the
# class variable.
#
# e1.company_name = "NewName"
#
# creates an instance attribute named company_name in e1.
# That instance attribute shadows the class attribute for e1.

e1.company_name = "NewName"

print(e1.company_name)       # NewName
print(e2.company_name)       # Codeyug
print(Employee.company_name) # Codeyug

print(e1.__dict__)


# ============================================================
# MODIFYING THE CLASS VARIABLE
# ============================================================
# To change the actual class variable, modify it through the
# class itself.

Employee.company_name = "TechSolutions"

print(Employee.company_name)
print(e2.company_name)

# e1 still has its own shadowing attribute.
print(e1.company_name)


# ============================================================
# CLASS METHODS
# ============================================================
# A class method is bound to the CLASS rather than a particular
# instance.
#
# @classmethod transforms the function into a class method.
#
# cls refers to the class that the method is bound to.
#
# Calling:
# Employee.change_company_name("Google")
#
# automatically supplies Employee as cls.


class Employee:
    company_name = "Codeyug"

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


Employee.change_company_name("TechSolutions")

print(Employee.company_name)


# ============================================================
# cls vs self
# ============================================================
# self -> current INSTANCE
# cls  -> current CLASS
#
# Instance method:
#     def method(self):
#
# Class method:
#     @classmethod
#     def method(cls):
#
# self is used to work with instance state.
# cls is used to work with class-level state.
# ============================================================


class Employee:
    company_name = "Codeyug"

    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print(self.name)

    @classmethod
    def show_company(cls):
        print(cls.company_name)


e1 = Employee("Rahul")

e1.show_employee()
Employee.show_company()

# A class method can also be called through an instance, but it
# remains class-bound:
e1.show_company()


# ============================================================
# WHY cls IS BETTER THAN HARD-CODING THE CLASS NAME
# ============================================================
# Avoid:
#
# Employee.company_name = new_name
#
# inside the class method.
#
# Prefer:
#
# cls.company_name = new_name
#
# because cls refers to the class through which the method is
# invoked and therefore works correctly with inheritance.


class Employee:
    company_name = "Codeyug"

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


class Manager(Employee):
    pass


Manager.change_company_name("TechSolutions")

print(Manager.company_name)
print(Employee.company_name)


# ============================================================
# CLASS METHOD AS AN ALTERNATIVE CONSTRUCTOR
# ============================================================
# A common advanced use of @classmethod is creating alternative
# ways to construct objects.
#
# The class method can receive different input and internally
# call cls(...) to create an instance.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))


e = Employee.from_string("Rahul,50000")

print(e.name)
print(e.salary)


# ============================================================
# CLASS VARIABLE vs INSTANCE VARIABLE
# ============================================================
# CLASS VARIABLE:
#     Employee.company_name
#     Shared through class lookup.
#
# INSTANCE VARIABLE:
#     e1.name
#     Stored separately for each object.
#
# CLASS METHOD:
#     Works primarily with class-level state.
#
# INSTANCE METHOD:
#     Works primarily with instance-level state.
# ============================================================