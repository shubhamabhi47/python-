# ============================================================
# WHY INHERITANCE? CODE REUSABILITY AND MAINTAINABILITY
# ============================================================
# Inheritance is especially useful when multiple classes share
# common state/behavior.
#
# Without inheritance -> duplicate common code.
# With inheritance    -> move common code into a parent class.
#
# This follows the DRY principle:
# DON'T REPEAT YOURSELF.
#
# If common logic changes, changing it in the parent class can
# update the behavior inherited by multiple child classes.
# ============================================================


# ============================================================
# WITHOUT INHERITANCE: CODE DUPLICATION
# ============================================================
# Customer and Employee both need name, balance and deposit().
# The common implementation has to be repeated.

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")


class Employee:
    def __init__(self, name, balance, salary):
        self.name = name
        self.balance = balance
        self.salary = salary

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")


# ============================================================
# WITH INHERITANCE: COMMON LOGIC IN ONE PLACE
# ============================================================
# BankAccount contains behavior common to account-holding
# entities.
#
# Employee inherits:
# - name
# - balance
# - deposit()
#
# Employee only needs to define its additional state: salary.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")


class Employee(BankAccount):
    def __init__(self, name, balance, salary):
        super().__init__(name, balance)
        self.salary = salary


emp = Employee("John", 1000, 50000)

emp.deposit(500)

print(emp.name)
print(emp.balance)
print(emp.salary)


# ============================================================
# MAINTAINABILITY
# ============================================================
# Common behavior exists only once.
#
# If deposit() needs validation or logging, modify it in
# BankAccount instead of duplicating the change in every child.

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        print(f"Deposited {amount}")


class Customer(BankAccount):
    pass


class Employee(BankAccount):
    def __init__(self, name, balance, salary):
        super().__init__(name, balance)
        self.salary = salary


customer = Customer("Rahul", 1000)
employee = Employee("Amit", 2000, 50000)

customer.deposit(500)
employee.deposit(1000)


# ============================================================
# INHERITANCE AS A DESIGN RELATIONSHIP
# ============================================================
# The parent should contain behavior/state that genuinely belongs
# to the general concept represented by the parent.
#
# Customer IS-A BankAccount
# Employee IS-A BankAccount
#
# The child then specializes the parent rather than duplicating
# its implementation.


# ============================================================
# CODE REUSE vs INHERITANCE
# ============================================================
# Inheritance is not simply a mechanism for avoiding duplicate
# code. The child should have a meaningful IS-A relationship with
# the parent.
#
# If two unrelated classes merely need the same utility function,
# prefer a normal function, helper class, or composition instead.
# ============================================================


# ============================================================
# MAJOR BENEFITS
# ============================================================
# 1. REUSABILITY
#    Common implementation is inherited instead of rewritten.
#
# 2. MAINTAINABILITY
#    Common behavior can be changed in one place.
#
# 3. READABILITY
#    The class hierarchy communicates relationships between types.
#
# 4. TESTABILITY
#    Shared behavior can be tested at the parent level and reused
#    by child classes.
#
# 5. EXTENSIBILITY
#    Child classes can add or override behavior without modifying
#    the parent.
# ============================================================