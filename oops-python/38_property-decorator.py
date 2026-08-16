# ============================================================
# @property DECORATOR
# ============================================================
# @property allows a method to be accessed like an attribute.
#
#     obj.email
#
# internally executes:
#
#     email(self)
#
# It is useful when a value is derived from other attributes,
# but should still have a clean attribute-style interface.


# ============================================================
# 1. PROBLEM: STATIC DERIVED ATTRIBUTE
# ============================================================
# email is calculated only once inside __init__().
# If first/last changes later, email becomes stale.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"


e1 = Employee("Shantanu", "Kejkar")
e1.first = "Jay"

print(e1.email)
# Shantanu.Kejkar@gmail.com


# ============================================================
# 2. USING A METHOD
# ============================================================
# Making email a method keeps the value dynamic because it is
# calculated whenever it is accessed.
#
# However, callers now need email() instead of email.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


e1 = Employee("Shantanu", "Kejkar")
e1.first = "Jay"

print(e1.email())


# ============================================================
# 3. @property
# ============================================================
# @property converts the method into a managed attribute.
#
# The method still executes, but the caller uses:
#
#     e1.email
#
# instead of:
#
#     e1.email()

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


e1 = Employee("Shantanu", "Kejkar")
e1.first = "Jay"

print(e1.email)


# ============================================================
# 4. PROPERTY FOR DERIVED DATA
# ============================================================
# A property is ideal for values that can be calculated from
# other attributes.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


e1 = Employee("Shantanu", "Kejkar")

print(e1.fullname)
print(e1.email)

e1.first = "Jay"

print(e1.fullname)
print(e1.email)


# ============================================================
# 5. PROPERTY SETTER
# ============================================================
# A property without a setter is read-only through normal
# attribute assignment.
#
#     e1.fullname = "Virat Kohli"
#
# would raise AttributeError.
#
# @fullname.setter defines what should happen during assignment.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(maxsplit=1)
        self.first = first
        self.last = last


e1 = Employee("Shantanu", "Kejkar")

print(e1.fullname)

e1.fullname = "Virat Kohli"

print(e1.fullname)
print(e1.first)
print(e1.last)


# ============================================================
# 6. PROPERTY DELETER
# ============================================================
# @fullname.deleter defines the behavior of:
#
#     del e1.fullname
#
# The deleter can clean up or reset internal state.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(maxsplit=1)

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


e1 = Employee("Shantanu", "Kejkar")

print(e1.fullname)

del e1.fullname

print(e1.first)
print(e1.last)


# ============================================================
# 7. PROPERTY WITH VALIDATION
# ============================================================
# One of the biggest advantages of properties is controlled
# assignment.
#
# Validation can be added without changing the external API.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


e1 = Employee("Rahul", 50000)

print(e1.salary)

e1.salary = 60000

print(e1.salary)

# e1.salary = -1000  # ValueError


# ============================================================
# 8. WHY _salary?
# ============================================================
# If the property is called salary, doing:
#
#     self.salary = value
#
# inside salary.setter would call the setter again and create
# infinite recursion.
#
# Therefore, the actual stored value is kept separately:
#
#     salary -> property
#     _salary -> internal storage

class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Invalid salary")
        self._salary = value


e1 = Employee(50000)
print(e1.salary)


# ============================================================
# 9. READ-ONLY PROPERTY
# ============================================================
# If only @property is defined and no setter exists, the property
# behaves like a read-only attribute.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2


c = Circle(5)

print(c.area)

# c.area = 100  # AttributeError


# ============================================================
# 10. DYNAMIC PROPERTY
# ============================================================
# Properties are recalculated whenever accessed.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2


c = Circle(5)

print(c.area)

c.radius = 10

print(c.area)


# ============================================================
# 11. ADVANCED: PROPERTY WITH MULTIPLE VALIDATIONS
# ============================================================
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be numeric")
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount


account = BankAccount("Rahul", 10000)

print(account.balance)

account.balance = 15000

print(account.balance)


# ============================================================
# 12. PROPERTY + BUSINESS LOGIC
# ============================================================
# A property does not have to simply return a stored variable.
# It can perform calculations or business logic.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(10, 5)

print(r.area)
print(r.perimeter)


# ============================================================
# 13. PROPERTY AS AN ABSTRACTION LAYER
# ============================================================
# The external API remains:
#
#     employee.salary
#
# even if the internal implementation changes later.
#
# This means a normal public attribute can be converted into a
# property without forcing users of the class to change their
# code.

class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Salary must be greater than zero")
        self._salary = value


e1 = Employee(50000)

print(e1.salary)

e1.salary = 70000

print(e1.salary)


# ============================================================
# 14. PROPERTY + DELETER WITH CLEANUP
# ============================================================
class User:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty")
        self._username = value

    @username.deleter
    def username(self):
        print("Removing username")
        del self._username


user = User("rahul")

print(user.username)

del user.username


# ============================================================
# 15. PROPERTY INTERNAL FLOW
# ============================================================
# When Python sees:
#
#     obj.salary
#
# Python invokes the property's getter.
#
# When Python sees:
#
#     obj.salary = 50000
#
# Python invokes the property's setter.
#
# When Python sees:
#
#     del obj.salary
#
# Python invokes the property's deleter.
#
# Therefore:
#
#     @property
#     def salary(self):
#         ...
#
#     @salary.setter
#     def salary(self, value):
#         ...
#
#     @salary.deleter
#     def salary(self):
#         ...
#
# creates ONE managed attribute with three possible operations:
#
#     GET    -> getter
#     SET    -> setter
#     DELETE -> deleter
# ============================================================


# ============================================================
# 16. ADVANCED: PROPERTY + ENCAPSULATION
# ============================================================
# Properties are commonly combined with protected/private
# internal storage.
#
# External code interacts with:
#
#     account.balance
#
# while the implementation controls:
#
#     self._balance

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Insufficient valid balance")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(3000)

print(account.balance)


# ============================================================
# 17. KEY DIFFERENCE: NORMAL ATTRIBUTE VS PROPERTY
# ============================================================
# Normal attribute:
#
#     self.salary = 50000
#
# Directly stores a value.
#
# Property:
#
#     @property
#     def salary(self):
#         return self._salary
#
# Provides controlled access to the value.
#
# A property can:
#     - validate data
#     - calculate values dynamically
#     - transform data
#     - enforce rules
#     - provide read-only access
#     - control deletion
#     - preserve a clean API
# ============================================================


# ============================================================
# FINAL COMPLETE EXAMPLE
# ============================================================
# A practical example combining:
#     getter
#     setter
#     deleter
#     validation
#     dynamic data
#     encapsulation

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        parts = name.split(maxsplit=1)

        if len(parts) != 2:
            raise ValueError("Enter first and last name")

        self.first, self.last = parts

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @property
    def email(self):
        if not self.first or not self.last:
            return None
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be numeric")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


e1 = Employee("Shantanu", "Kejkar", 50000)

print(e1.fullname)
print(e1.email)
print(e1.salary)

e1.fullname = "Virat Kohli"
e1.salary = 75000

print(e1.fullname)
print(e1.email)
print(e1.salary)

del e1.fullname

print(e1.first)
print(e1.last)
print(e1.email)


# ============================================================
# CORE IDEA
# ============================================================
# @property turns a method into an attribute-like interface.
#
#     obj.value
#         ↓
#     getter
#
#     obj.value = x
#         ↓
#     setter
#
#     del obj.value
#         ↓
#     deleter
#
# The important advantage is CONTROL.
#
# Instead of allowing:
#
#     object.attribute = anything
#
# you can define rules for how that attribute is read, changed,
# or deleted while keeping the clean syntax:
#
#     object.attribute
#
# This is one of Python's most useful tools for combining
# encapsulation with a simple public API.
# ============================================================