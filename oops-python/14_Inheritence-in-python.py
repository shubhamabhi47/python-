# ============================================================
# INHERITANCE
# ============================================================
# Inheritance allows a child/subclass to reuse attributes and
# methods from a parent/base/superclass.
#
# Parent/Base class  -> Employee
# Child/Derived class -> Manager
#
# It represents an "IS-A" relationship:
# Manager IS-A Employee
#
# A child can use inherited members and also define its own.
# ============================================================


# ============================================================
# WITHOUT INHERITANCE
# ============================================================
# Independent classes do not automatically share their methods
# or attributes.

class Employee:
    bonus = 5000

    def show(self):
        print("This is Employee class")


class Manager:
    bonus = 10000

    def display(self):
        print("This is Manager class")


e1 = Employee()
m1 = Manager()

# e1.display()  # AttributeError
# m1.show()     # AttributeError


# ============================================================
# BASIC INHERITANCE
# ============================================================
# class Manager(Employee):
# means Manager inherits from Employee.
#
# Manager gets access to Employee's inherited members unless they
# are overridden or otherwise hidden.

class Employee:
    bonus = 5000

    def show(self):
        print("This is Employee class")


class Manager(Employee):
    def display(self):
        print("This is Manager class")


m1 = Manager()

m1.show()
m1.display()

print(m1.bonus)


# ============================================================
# PARENT CANNOT AUTOMATICALLY ACCESS CHILD MEMBERS
# ============================================================
# Inheritance works from parent -> child.
#
# Employee does not automatically gain Manager-specific members.
#
# Employee:
#     show()
#
# Manager:
#     show()       -> inherited
#     display()    -> own member
#
# Therefore an Employee object cannot call display().

e1 = Employee()

# e1.display()  # AttributeError


# ============================================================
# METHOD AND ATTRIBUTE INHERITANCE
# ============================================================
# A child can inherit both:
# - Class attributes
# - Methods
#
# The child can also add its own attributes/methods.

class Employee:
    company = "ABC"

    def work(self):
        print("Employee is working")


class Manager(Employee):
    def manage(self):
        print("Manager is managing")


m = Manager()

print(m.company)
m.work()
m.manage()


# ============================================================
# IS-A RELATIONSHIP
# ============================================================
# A Manager is an Employee.
#
# Therefore isinstance() recognizes Manager objects as instances
# of Employee as well.

print(isinstance(m, Manager))  # True
print(isinstance(m, Employee)) # True


# ============================================================
# ATTRIBUTE LOOKUP WITH INHERITANCE
# ============================================================
# If Python cannot find an attribute in the instance or current
# class, it searches the inheritance hierarchy.
#
# Simplified:
#
# m.attribute
#     ↓
# instance
#     ↓
# Manager
#     ↓
# Employee
#     ↓
# object
#
# This lookup process is formally governed by Python's MRO
# (Method Resolution Order).
# ============================================================


# ============================================================
# METHOD OVERRIDING
# ============================================================
# A child can provide its own implementation of a method that
# already exists in the parent.
#
# The child's implementation takes precedence during normal
# lookup.

class Employee:
    def show(self):
        print("Employee")


class Manager(Employee):
    def show(self):
        print("Manager")


m = Manager()
m.show()  # Manager


# ============================================================
# super()
# ============================================================
# super() provides a convenient way to access the parent class
# implementation from the child class.
#
# This is especially important when extending inherited behavior.

class Employee:
    def show(self):
        print("Employee")


class Manager(Employee):
    def show(self):
        super().show()
        print("Manager")


m = Manager()
m.show()


# ============================================================
# INHERITANCE WITH __init__()
# ============================================================
# If the child defines its own __init__(), the parent __init__()
# is not automatically executed.
#
# super().__init__(...) can explicitly initialize the parent part
# of the object.

class Employee:
    def __init__(self, name):
        self.name = name


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


m = Manager("Rahul", "Engineering")

print(m.name)
print(m.department)


# ============================================================
# IMPORTANT IDEA
# ============================================================
# Parent -> provides reusable/general behavior.
# Child  -> specializes or extends that behavior.
#
# Inheritance provides:
# - Code reuse
# - Specialization
# - Method overriding
# - Polymorphic relationships
#
# But inheritance should represent a genuine "IS-A" relationship.
# If two classes merely share some functionality, composition or
# another design may be more appropriate.
# ============================================================