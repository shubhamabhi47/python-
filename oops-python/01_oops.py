# ============================================================
# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
# ============================================================
# Python supports multiple programming paradigms:
# 1. Procedural Programming
# 2. Functional Programming
# 3. Object-Oriented Programming (OOP)
#
# A programming paradigm is a style/approach used to structure
# and organize programs.
# ============================================================


# ============================================================
# 1. PROCEDURAL PROGRAMMING
# ============================================================
# Procedural programming is based on procedures/functions.
# The program is primarily organized around a sequence of
# operations that manipulate data.
#
# Main focus: WHAT TO DO -> functions/procedures
# Data and logic are generally handled separately.
#
# Advantages:
# - Simple and straightforward
# - Good for small programs/scripts
# - Easy to understand initially
#
# Limitations for large systems:
# - Data can be accessed/modified from many places
# - Maintaining relationships between data and operations
#   becomes difficult
# - Code can become tightly coupled as the project grows

def process_data():
    print("Step 1: Data input")
    print("Step 2: Processing logic")
    print("Step 3: Result output")

process_data()


# ============================================================
# 2. FUNCTIONAL PROGRAMMING
# ============================================================
# Functional programming organizes programs around functions.
# Functions can receive data and return results.
#
# Core ideas:
# - Functions are treated as first-class objects
# - Prefer pure functions
# - Avoid unnecessary mutation/state changes
# - Functions can be composed together
#
# A pure function generally:
# - Gives the same output for the same input
# - Does not modify external state
#
# Python supports functional programming but is not purely
# functional.

def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print(result)


# ============================================================
# 3. OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================
# OOP organizes programs around OBJECTS.
#
# An object combines:
# - Data     -> attributes/properties
# - Behavior -> methods
#
# Example:
# BankAccount object
#   Data     -> owner, balance
#   Behavior -> deposit(), withdraw()
#
# Procedural programming mainly asks:
# "What operations should the program perform?"
#
# OOP mainly asks:
# "What objects exist, what data do they own, and what
#  operations are allowed on that data?"
#
# This makes OOP useful for modeling complex real-world systems.


class BankAccount:
    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    # __init__() runs automatically when an object is created.
    # self refers to the current object.
    #
    # self.owner and self.balance are INSTANCE ATTRIBUTES.
    # Each object gets its own copy of these attributes.

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # --------------------------------------------------------
    # METHOD
    # --------------------------------------------------------
    # A method is a function defined inside a class.
    # It operates on the object's data through self.

    def deposit(self, amount):
        self.balance += amount
        return self.balance


# ------------------------------------------------------------
# OBJECT / INSTANCE CREATION
# ------------------------------------------------------------
# BankAccount is the CLASS (blueprint).
# my_account is an OBJECT/INSTANCE created from that class.

my_account = BankAccount("User", 1000)

print(my_account.owner)
print(my_account.balance)
print(my_account.deposit(500))


# ============================================================
# CLASS VS OBJECT
# ============================================================
# Class:
#   Blueprint/template describing what an object contains.
#
# Object:
#   Actual instance created from the class.
#
# One class can create many independent objects.

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.deposit(200)
account2.deposit(100)

print(account1.balance)  # 1200
print(account2.balance)  # 600


# ============================================================
# ENCAPSULATION
# ============================================================
# Encapsulation means bundling data and the methods that operate
# on that data inside a class.
#
# It also allows us to control how internal data is accessed or
# modified instead of exposing everything directly.
#
# Python does not enforce traditional private fields like some
# languages. Naming conventions are commonly used:
#
# _balance  -> intended for internal/protected use
# __balance -> name mangling; stronger protection convention
#
# Good encapsulation exposes controlled operations rather than
# allowing arbitrary modification of internal state.

class SecureBankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = SecureBankAccount("User", 1000)
account.deposit(500)
print(account.get_balance())


# ============================================================
# WHY OOP?
# ============================================================
# OOP becomes especially useful as programs become larger.
#
# 1. Encapsulation
#    Keep related data and behavior together.
#
# 2. Abstraction
#    Expose only the necessary interface while hiding
#    implementation details.
#
# 3. Inheritance
#    Create new classes based on existing classes.
#
# 4. Polymorphism
#    Different objects can provide the same interface with
#    different implementations.
#
# 5. Modularity
#    Large systems can be divided into independent classes.
#
# 6. Reusability
#    Classes and methods can be reused across the application.
#
# The major OOP concepts are commonly summarized as:
# ENCAPSULATION + ABSTRACTION + INHERITANCE + POLYMORPHISM
# ============================================================

# give me the code of each point in the video in the chronological order with topic name  and technical definition with deep dive and do not skip anything in the code
