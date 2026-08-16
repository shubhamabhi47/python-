# ============================================================
# NESTED CLASSES (INNER CLASSES) IN PYTHON
# ============================================================
# A nested class is a class defined inside another class.
#
# Outer class -> contains/organizes the inner class.
# Inner class -> represents a concept strongly related to the
#                outer class.
#
# Important:
# A nested class does NOT automatically receive the outer object
# as self. It is simply a class stored inside the outer class's
# namespace.
# ============================================================


# ============================================================
# 1. BASIC NESTED CLASS
# ============================================================
class Outer:
    class Inner:
        def show(self):
            print("Inner class method")


outer = Outer()
inner = Outer.Inner()
inner.show()


# ============================================================
# 2. CREATING INNER OBJECT THROUGH OUTER OBJECT
# ============================================================
# Because Inner is a class attribute of Outer, this also works:
#
#     outer.Inner()
#
# But this does NOT mean Inner automatically gets access to
# outer's instance variables.

class Outer:
    class Inner:
        def show(self):
            print("Inside Inner")


outer = Outer()
inner = outer.Inner()
inner.show()


# ============================================================
# 3. CREATING INNER OBJECT INSIDE OUTER CLASS
# ============================================================
# A common pattern is to create the inner object as an attribute
# of the outer object.

class Outer:
    def __init__(self):
        self.inner = self.Inner()

    class Inner:
        def show(self):
            print("Inner object belongs to Outer")


outer = Outer()
outer.inner.show()


# ============================================================
# 4. OUTER + INNER CLASS WITH RELATED DATA
# ============================================================
# Nested classes are useful when the inner object represents a
# component of the outer object.

class Student:
    def __init__(self, name, roll, day, month, year):
        self.name = name
        self.roll = roll
        self.dob = self.DateOfBirth(day, month, year)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        self.dob.display()

    class DateOfBirth:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

        def display(self):
            print(
                f"Date of Birth: "
                f"{self.day:02d}/{self.month:02d}/{self.year}"
            )


student = Student("Ajay", 101, 15, 8, 2002)
student.display()


# ============================================================
# 5. IMPORTANT: INNER CLASS DOES NOT AUTOMATICALLY KNOW
#    ABOUT THE OUTER OBJECT
# ============================================================
# This does NOT work:
#
# class Outer:
#     def __init__(self):
#         self.name = "Outer"
#
#     class Inner:
#         def show(self):
#             print(self.name)
#
# self inside Inner refers to the Inner object, NOT Outer.

class Outer:
    def __init__(self):
        self.name = "Outer Object"

    class Inner:
        def show(self):
            print("Inner Object")


outer = Outer()
inner = outer.Inner()
inner.show()


# ============================================================
# 6. PASSING OUTER OBJECT EXPLICITLY
# ============================================================
# If the inner object needs access to the outer object's state,
# pass the outer object explicitly.

class Student:
    def __init__(self, name):
        self.name = name
        self.details = self.Details(self)

    class Details:
        def __init__(self, student):
            self.student = student

        def display(self):
            print(f"Student Name: {self.student.name}")


student = Student("Rahul")
student.details.display()


# ============================================================
# 7. BETTER DESIGN: PASS ONLY REQUIRED DATA
# ============================================================
# Passing the entire outer object creates stronger coupling.
# Often it is cleaner to pass only the data the inner class needs.

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.details = self.Details(name, roll)

    class Details:
        def __init__(self, name, roll):
            self.name = name
            self.roll = roll

        def display(self):
            print(f"Name: {self.name}, Roll: {self.roll}")


student = Student("Rahul", 101)
student.details.display()


# ============================================================
# 8. ACCESSING INNER CLASS FROM OUTSIDE
# ============================================================
# The inner class can be accessed through the outer class itself.

class Company:
    class Employee:
        def work(self):
            print("Employee is working")


employee = Company.Employee()
employee.work()


# ============================================================
# 9. NESTED CLASS AS A DATA COMPONENT
# ============================================================
# This is useful for hierarchical/structured data.

class Person:
    class Address:
        def __init__(self, city, state, pin):
            self.city = city
            self.state = state
            self.pin = pin

        def __str__(self):
            return f"{self.city}, {self.state} - {self.pin}"

    def __init__(self, name, city, state, pin):
        self.name = name
        self.address = self.Address(city, state, pin)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")


person = Person("Rahul", "Kolkata", "West Bengal", 700001)
person.display()


# ============================================================
# 10. NESTED CLASS WITH MULTIPLE OBJECTS
# ============================================================
# Each outer object can contain its own independent inner object.

class University:
    class Department:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    def __init__(self, name, department):
        self.name = name
        self.department = self.Department(department)


u1 = University("SMIT", "Computer Science")
u2 = University("MIT", "Mechanical Engineering")

print(u1.department)
print(u2.department)


# ============================================================
# 11. NESTED CLASS AS A HELPER/IMPLEMENTATION DETAIL
# ============================================================
# A nested class can hide implementation details that are only
# meaningful to the outer class.

class ShoppingCart:
    class Item:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def total(self):
            return self.price * self.quantity

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append(self.Item(name, price, quantity))

    def total(self):
        return sum(item.total() for item in self.items)


cart = ShoppingCart()
cart.add_item("Keyboard", 2000, 2)
cart.add_item("Mouse", 1000, 1)

print(cart.total())


# ============================================================
# 12. NESTED CLASS VS INHERITANCE
# ============================================================
# Nested classes represent a "has-a"/containment relationship.
#
#     Student HAS-A DateOfBirth
#
# Inheritance represents an "is-a" relationship.
#
#     Manager IS-A Employee
#
# Therefore, nested classes and inheritance solve different
# design problems.


# ============================================================
# 13. NESTED CLASS VS INSTANCE ATTRIBUTE
# ============================================================
# The class itself is stored in the outer class namespace.
#
#     Student.DateOfBirth
#
# An instance of that class can then be stored inside an object:
#
#     student.dob
#
# These are two different levels:
#
#     Student.DateOfBirth -> class
#     student.dob         -> object


class Student:
    class DateOfBirth:
        pass


student = Student()

print(Student.DateOfBirth)
print(student.DateOfBirth)
print(type(student.DateOfBirth))


# ============================================================
# 14. ADVANCED: CLASS ATTRIBUTE INSPECTION
# ============================================================
# The nested class is simply an attribute of the outer class.

class Company:
    class Employee:
        pass


print(Company.__dict__["Employee"])
print(Company.Employee)


# ============================================================
# 15. NESTED CLASS DOES NOT MEAN PRIVATE CLASS
# ============================================================
# A nested class is still accessible from outside unless you
# deliberately use naming conventions such as _Helper.
#
# Nesting provides logical organization, not true privacy.

class Service:
    class _Helper:
        def process(self):
            print("Processing...")


helper = Service._Helper()
helper.process()


# ============================================================
# 16. ADVANCED REAL-WORLD EXAMPLE
# ============================================================
# A BankAccount can contain a Transaction type because a
# transaction is conceptually related to an account.

class BankAccount:
    class Transaction:
        def __init__(self, transaction_type, amount):
            self.transaction_type = transaction_type
            self.amount = amount

        def __repr__(self):
            return (
                f"Transaction("
                f"{self.transaction_type!r}, "
                f"{self.amount})"
            )

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount
        self.transactions.append(
            self.Transaction("Deposit", amount)
        )

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.transactions.append(
            self.Transaction("Withdrawal", amount)
        )

    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)


account = BankAccount("Rahul", 10000)

account.deposit(5000)
account.withdraw(2000)

account.statement()


# ============================================================
# KEY TAKEAWAYS
# ============================================================
# Nested class:
#
#     class Outer:
#         class Inner:
#             pass
#
# It is mainly useful when:
#
#     • Inner class is strongly related to Outer.
#     • Inner class is mainly used by Outer.
#     • You want logical grouping/organization.
#     • A complex component belongs naturally to another object.
#
# IMPORTANT:
#
#     outer.Inner()
#
# does NOT automatically pass outer to Inner.
#
# If Inner needs Outer:
#
#     self.inner = self.Inner(self)
#
# or pass only the required data.
#
# Also remember:
#
#     Nested class  -> organizational relationship
#     Composition   -> object contains another object
#     Inheritance   -> "is-a" relationship
#
# Nested classes are therefore mainly a tool for organization
# and modeling closely related components, not a special form
# of inheritance or automatic encapsulation.
# ============================================================