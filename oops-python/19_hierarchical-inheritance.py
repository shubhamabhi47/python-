# ============================================================
# HIERARCHICAL INHERITANCE
# ============================================================
# Hierarchical inheritance occurs when multiple child classes
# inherit from the same parent class.
#
#             Person
#             /    \
#            ↓      ↓
#       Employee  Student
#
# Common behavior belongs in the parent.
# Child-specific behavior belongs in the respective child.
# ============================================================


# ============================================================
# 1. BASIC HIERARCHICAL INHERITANCE
# ============================================================
# Employee and Student both inherit from Person.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    pass


class Student(Person):
    pass


employee = Employee("Rahul", 25)
student = Student("Aman", 21)

print(employee.name)
print(student.name)


# ============================================================
# 2. CHILD-SPECIFIC ATTRIBUTES
# ============================================================
# Each child can extend the parent's initialization using
# super() and add its own attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks


employee = Employee("Rahul", 25, 60000)
student = Student("Aman", 21, 90)

print(employee.name)
print(employee.age)
print(employee.salary)

print(student.name)
print(student.age)
print(student.marks)


# ============================================================
# 3. PARENT METHODS ARE SHARED BY ALL CHILDREN
# ============================================================
# A method defined in Person is available to both Employee and
# Student through inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_employee(self):
        print(f"Salary: {self.salary}")


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display_student(self):
        print(f"Marks: {self.marks}")


employee = Employee("Rahul", 25, 60000)
student = Student("Aman", 21, 90)

employee.display()
employee.display_employee()

student.display()
student.display_student()


# ============================================================
# 4. SIBLING CLASSES CANNOT ACCESS EACH OTHER
# ============================================================
# Employee and Student are sibling classes.
#
# Student inherits from Person, NOT Employee.
#
# Therefore Student cannot access Employee-specific methods.

# student.display_employee()  # AttributeError


# ============================================================
# 5. METHOD OVERRIDING IN CHILDREN
# ============================================================
# Each child can override the same parent method independently.
#
# The parent implementation remains available through super().

class Person:
    def display(self):
        print("Person")


class Employee(Person):
    def display(self):
        super().display()
        print("Employee")


class Student(Person):
    def display(self):
        super().display()
        print("Student")


Employee().display()
Student().display()


# ============================================================
# 6. isinstance() IN HIERARCHICAL INHERITANCE
# ============================================================
# Each child object is an instance of its own class and also of
# the parent class.

employee = Employee()
student = Student()

print(isinstance(employee, Employee)) # True
print(isinstance(employee, Person))   # True

print(isinstance(student, Student))   # True
print(isinstance(student, Person))    # True


# ============================================================
# 7. MRO
# ============================================================
# Each child has its own MRO.
#
# Employee:
# Employee -> Person -> object
#
# Student:
# Student -> Person -> object

print(Employee.__mro__)
print(Student.__mro__)


# ============================================================
# KEY IDEA
# ============================================================
# Hierarchical inheritance:
#
#             Parent
#            /      \
#        Child A   Child B
#
# Parent members:
#     Accessible by both children.
#
# Child A members:
#     Accessible by Child A only.
#
# Child B members:
#     Accessible by Child B only.
#
# Sibling classes do NOT inherit from each other.
#
# Use hierarchical inheritance when multiple classes share a
# common base but require different specialized behavior.
# ============================================================