# ============================================================
# ACCESSING MEMBERS OF ONE CLASS FROM ANOTHER CLASS
# ============================================================
# Objects can be passed between classes just like any other
# Python object.
#
# A method of one class can receive an object belonging to
# another class and access its public attributes/methods.
#
# This is NOT inheritance.
#
# Employee and Salary are independent classes.
# Salary simply receives an Employee object as an argument.
# ============================================================


# ============================================================
# 1. BASIC CROSS-CLASS OBJECT INTERACTION
# ============================================================
# Salary.increment() receives an Employee object and modifies
# its state directly.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Salary:
    @staticmethod
    def increment(emp_obj):
        emp_obj.salary += 1000


e1 = Employee("Shantanu", 50000)

Salary.increment(e1)

e1.display()


# ============================================================
# 2. WHY THE ORIGINAL OBJECT CHANGES
# ============================================================
# Python passes object references.
#
# When:
#
#     Salary.increment(e1)
#
# emp_obj refers to the same Employee object as e1.
#
# Therefore:
#
#     emp_obj.salary += 1000
#
# modifies the original object.
#
# There is NOT a separate copy of e1 being created.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Salary:
    @staticmethod
    def increment(emp):
        emp.salary += 1000


e1 = Employee("Rahul", 50000)

print(e1.salary)

Salary.increment(e1)

print(e1.salary)


# ============================================================
# 3. STATIC METHOD IS NOT REQUIRED
# ============================================================
# @staticmethod is useful here because Salary.increment() does
# not need a Salary object.
#
# It operates entirely on the Employee object supplied as an
# argument.
#
# The following design would also work.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Salary:
    def increment(self, emp):
        emp.salary += 1000


salary = Salary()
employee = Employee("Rahul", 50000)

salary.increment(employee)

print(employee.salary)


# ============================================================
# 4. MULTIPLE OPERATIONS ON ANOTHER CLASS'S OBJECT
# ============================================================
# A helper/service class can perform multiple operations on
# another class's object.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name}: ₹{self.salary}")


class Salary:
    @staticmethod
    def increment(emp, amount):
        if amount < 0:
            raise ValueError("Increment cannot be negative")
        emp.salary += amount

    @staticmethod
    def deduct(emp, amount):
        if amount < 0:
            raise ValueError("Deduction cannot be negative")
        if amount > emp.salary:
            raise ValueError("Insufficient salary")
        emp.salary -= amount


e1 = Employee("Rahul", 50000)

Salary.increment(e1, 5000)
Salary.deduct(e1, 2000)

e1.display()


# ============================================================
# 5. PASSING OBJECTS TO NORMAL FUNCTIONS
# ============================================================
# The same concept does not require classes at all.
#
# Any function can receive an object and interact with it.
#
# This shows that the important concept is OBJECT COMPOSITION/
# COLLABORATION, not inheritance.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


def give_increment(employee, amount):
    employee.salary += amount


e1 = Employee("Aman", 40000)

give_increment(e1, 5000)

print(e1.salary)


# ============================================================
# 6. ONE CLASS USING ANOTHER CLASS'S METHODS
# ============================================================
# An object can also be passed to another object's method.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


class Payroll:
    def process(self, employee):
        employee.salary += 5000
        employee.display()


e1 = Employee("Raj", 60000)
payroll = Payroll()

payroll.process(e1)


# ============================================================
# 7. CONTROLLED ACCESS THROUGH METHODS
# ============================================================
# Directly modifying another object's attributes can tightly
# couple the classes.
#
# A better design is often to expose behavior through methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def increase_salary(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._salary += amount

    def get_salary(self):
        return self._salary


class Payroll:
    @staticmethod
    def increment(employee, amount):
        employee.increase_salary(amount)


e1 = Employee("Rahul", 50000)

Payroll.increment(e1, 5000)

print(e1.get_salary())


# ============================================================
# 8. ENCAPSULATION + CROSS-CLASS INTERACTION
# ============================================================
# Combining this concept with encapsulation gives a cleaner
# design.
#
# Payroll does not directly modify the internal salary state.
# It asks Employee to perform the operation.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount <= 0:
            raise ValueError("Increment must be positive")
        self.__salary += amount


class Payroll:
    @staticmethod
    def give_increment(employee, amount):
        employee.increase_salary(amount)


e1 = Employee("Shantanu", 50000)

Payroll.give_increment(e1, 10000)

print(e1.salary)


# ============================================================
# 9. DEPENDENCY INJECTION
# ============================================================
# Passing an object into another class/method is also a basic
# form of dependency injection.
#
# Instead of Payroll creating an Employee itself, the Employee
# is supplied from outside.
#
# This makes the code easier to test and reuse.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    def __init__(self, employee):
        self.employee = employee

    def increment(self, amount):
        self.employee.salary += amount


employee = Employee("Rahul", 50000)

payroll = Payroll(employee)

payroll.increment(5000)

print(employee.salary)


# ============================================================
# 10. MULTIPLE OBJECTS
# ============================================================
# A service class can work with multiple objects.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    @staticmethod
    def increment_all(employees, amount):
        for employee in employees:
            employee.salary += amount


employees = [
    Employee("Rahul", 50000),
    Employee("Aman", 60000),
    Employee("Raj", 70000)
]

Payroll.increment_all(employees, 5000)

for employee in employees:
    print(employee.name, employee.salary)


# ============================================================
# 11. ADVANCED: TYPE VALIDATION
# ============================================================
# If a method specifically expects an Employee, validating the
# type can prevent accidental misuse.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    @staticmethod
    def increment(employee, amount):
        if not isinstance(employee, Employee):
            raise TypeError("Expected an Employee object")
        employee.salary += amount


e1 = Employee("Rahul", 50000)

Payroll.increment(e1, 5000)

print(e1.salary)


# ============================================================
# 12. CROSS-CLASS INTERACTION VS INHERITANCE
# ============================================================
# IMPORTANT DIFFERENCE:
#
# INHERITANCE:
#
#     class Manager(Employee):
#
# Manager IS an Employee.
#
# CROSS-CLASS INTERACTION:
#
#     Payroll.increment(employee)
#
# Payroll is NOT an Employee.
# It simply works WITH an Employee object.
#
# This represents collaboration rather than an "is-a"
# relationship.
# ============================================================


# ============================================================
# 13. COMPOSITION / HAS-A RELATIONSHIP
# ============================================================
# If one class stores another object as an attribute, we often
# describe this as composition or aggregation depending on the
# ownership/lifecycle relationship.
#
# Example:
#
#     Company HAS employees.
#
# Company does not inherit from Employee.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary(self):
        return sum(employee.salary for employee in self.employees)


company = Company()

company.add_employee(Employee("Rahul", 50000))
company.add_employee(Employee("Aman", 60000))
company.add_employee(Employee("Raj", 70000))

print(company.total_salary())


# ============================================================
# KEY IDEA
# ============================================================
# One class can interact with another class simply by receiving
# its object as an argument or storing that object.
#
# Example:
#
#     Payroll.increment(employee)
#
# employee is the actual Employee object.
#
# This is different from inheritance:
#
#     Inheritance -> IS-A relationship
#     Collaboration -> WORKS-WITH relationship
#     Composition -> HAS-A relationship
#
# GOOD OOP DESIGN:
#     • Use inheritance when there is a genuine IS-A relationship.
#     • Use composition/collaboration when objects work together.
#     • Keep internal state encapsulated.
#     • Prefer methods/properties for controlled state changes.
#     • Avoid unnecessary inheritance just to reuse code.
# ============================================================