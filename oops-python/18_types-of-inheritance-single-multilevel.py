# ============================================================
# TYPES OF INHERITANCE
# ============================================================
# Two types covered here:
# 1. Single Inheritance
# 2. Multi-Level Inheritance
#
# Inheritance allows a child class to reuse attributes and
# methods from its parent class.
# ============================================================


# ============================================================
# 1. SINGLE INHERITANCE
# ============================================================
# One child class directly inherits from exactly one parent class.
#
# Human
#   ↓
# Employee

class Human:
    def speak(self):
        print("Human can speak")


class Employee(Human):
    def work(self):
        print("Employee is working")


emp = Employee()

emp.speak()
emp.work()


# ============================================================
# 2. MULTI-LEVEL INHERITANCE
# ============================================================
# A class inherits from another class which itself inherits from
# another class.
#
# Human
#   ↓
# Employee
#   ↓
# Manager
#
# Manager indirectly inherits everything accessible through
# Employee and Human.

class Human:
    def walk(self):
        print("Human can walk")


class Employee(Human):
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def manage(self):
        print("Manager manages the team")


mgr = Manager()

mgr.walk()
mgr.work()
mgr.manage()


# ============================================================
# 3. MULTI-LEVEL INHERITANCE WITH CONSTRUCTORS
# ============================================================
# If a child does not define __init__(), Python searches upward
# through the inheritance hierarchy.
#
# Manager -> Employee -> Human
#
# Since Manager and Employee have no __init__(), Human.__init__()
# is found and executed.

class Human:
    def __init__(self):
        print("Human Constructor")


class Employee(Human):
    pass


class Manager(Employee):
    pass


mgr = Manager()


# ============================================================
# 4. DIFFERENT CONSTRUCTORS IN EACH LEVEL
# ============================================================
# If a class defines its own constructor, that constructor takes
# precedence.
#
# Parent constructors are not automatically executed.
# Use super() when parent initialization is required.

class Human:
    def __init__(self, name):
        self.name = name


class Employee(Human):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


mgr = Manager("Rahul", 80000, "Engineering")

print(mgr.name)
print(mgr.salary)
print(mgr.department)


# ============================================================
# 5. ATTRIBUTE/METHOD RESOLUTION
# ============================================================
# When Python evaluates:
#
# mgr.some_attribute
#
# it searches according to the MRO.
#
# Simplified:
#
# Manager
#    ↓
# Employee
#    ↓
# Human
#    ↓
# object
#
# The first matching attribute is used.

class Human:
    species = "Human"

    def walk(self):
        print("Walking")


class Employee(Human):
    salary = 50000

    def work(self):
        print("Working")


class Manager(Employee):
    department = "Engineering"

    def manage(self):
        print("Managing")


mgr = Manager()

print(mgr.species)
print(mgr.salary)
print(mgr.department)

mgr.walk()
mgr.work()
mgr.manage()


# ============================================================
# 6. ATTRIBUTE OVERRIDING IN MULTI-LEVEL INHERITANCE
# ============================================================
# If the same attribute exists at multiple levels, Python uses
# the first occurrence found in the MRO.

class Human:
    role = "Human"


class Employee(Human):
    role = "Employee"


class Manager(Employee):
    role = "Manager"


mgr = Manager()

print(mgr.role)  # Manager


# ============================================================
# 7. MRO
# ============================================================
# __mro__ shows the exact order Python follows for attribute and
# method lookup.

print(Manager.__mro__)


# ============================================================
# 8. PARENT CANNOT ACCESS CHILD-SPECIFIC MEMBERS
# ============================================================
# Inheritance flows from parent to child.
#
# Employee objects do not automatically contain attributes or
# methods introduced only by Manager.

class Human:
    pass


class Employee(Human):
    def work(self):
        print("Working")


class Manager(Employee):
    def manage(self):
        print("Managing")


employee = Employee()
manager = Manager()

employee.work()
manager.work()
manager.manage()

# employee.manage()  # AttributeError


# ============================================================
# 9. isinstance() WITH MULTI-LEVEL INHERITANCE
# ============================================================
# An object of the lowest-level child is considered an instance
# of every class in its inheritance chain.

print(isinstance(manager, Manager))  # True
print(isinstance(manager, Employee)) # True
print(isinstance(manager, Human))    # True
print(isinstance(manager, object))   # True


# ============================================================
# KEY IDEA
# ============================================================
# SINGLE:
#
# Human
#   ↓
# Employee
#
# MULTI-LEVEL:
#
# Human
#   ↓
# Employee
#   ↓
# Manager
#
# In multi-level inheritance:
# - Child can access parent members.
# - Grandchild can access members from all accessible ancestors.
# - Python searches using MRO.
# - A missing child constructor can be inherited from an ancestor.
# - Parent classes do not gain child-specific behavior.
# ============================================================