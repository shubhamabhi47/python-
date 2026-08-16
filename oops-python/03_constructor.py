# ============================================================
#  OOP: CONSTRUCTORS AND __init__() IN PYTHON
#  ============================================================
#  A constructor/initializer is used to initialize an object
#  when it is created.
# 
#  In Python, __init__() is the initializer method automatically
#  called after a new object is created.
# 
#  General flow:
#  Employee(...) -> object creation -> __init__(...) -> object initialized
#  ============================================================


# ============================================================
# 1. DEFAULT / NON-PARAMETERIZED CONSTRUCTOR
# ============================================================
# A no-argument __init__() initializes every object with the
# same predefined/default values.
#
# It is called automatically whenever Employee() is executed.

class Employee:
    def __init__(self):
        self.name = "Default"
        self.salary = 20000
        print("Object is created automatically")


emp1 = Employee()
emp2 = Employee()
print(emp1.__dict__)

# ============================================================
# 2. ACCESSING INSTANCE ATTRIBUTES
# ============================================================
# Attributes created using self belong to the individual object.
# They are called INSTANCE ATTRIBUTES.
#
# Dot notation is used to access them:
# object.attribute
#
# Each object maintains its own instance namespace/state.

print(emp1.name)
print(emp1.salary)
print(emp2.name)
print(emp2.salary)


# ============================================================
# 3. PARAMETERIZED CONSTRUCTOR
# ============================================================
# Hard-coding the same values for every object is usually not
# useful.
#
# A parameterized __init__() accepts values during object
# creation, allowing every object to have different state.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("Rahul", 50000)
emp2 = Employee("Shantanu", 60000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)


# ============================================================
# 4. UNDERSTANDING self
# ============================================================
# self represents the CURRENT INSTANCE of the class.
#
# When we write:
#     emp1 = Employee("Rahul", 50000)
#
# Python effectively calls:
#     Employee.__init__(emp1, "Rahul", 50000)
#
# Therefore:
#     self  -> emp1
#     name  -> "Rahul"
#     salary -> 50000
#
# And:
#     self.name = name
#
# means:
#     emp1.name = "Rahul"
#
# For emp2:
#     Employee.__init__(emp2, "Shantanu", 60000)
#
# so:
#     self -> emp2
#     emp2.name -> "Shantanu"
#
# self is NOT explicitly passed when using:
#     Employee("Rahul", 50000)
#
# Python supplies the instance automatically when calling the
# instance method internally.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)


emp1 = Employee("Rahul", 50000)
emp2 = Employee("Shantanu", 60000)

emp1.show()
emp2.show()


# ============================================================
# 5. LOCAL VARIABLE vs INSTANCE ATTRIBUTE
# ============================================================
# name is a local parameter/variable.
# self.name is an attribute stored inside the object.
#
# They are different things even though they have the same name.

class Employee:
    def __init__(self, name):
        self.name = name
        # self.name -> stored inside the object
        # name      -> local parameter


emp = Employee("Rahul")
print(emp.name)


# ============================================================
# 6. self IS THE OBJECT
# ============================================================
# The following two objects contain independent state.

class Employee:
    def __init__(self, name):
        self.name = name

emp1 = Employee("Rahul")
emp2 = Employee("Shantanu")

emp1.name = "Amit"

print(emp1.name)  # Amit
print(emp2.name)  # Shantanu


# ============================================================
# 7. METHODS ALSO USE self
# ============================================================
# self is not limited to __init__().
# Every normal instance method receives the current object as
# its first parameter.
#
# Calling:
#     emp.show()
#
# is conceptually equivalent to:
#     Employee.show(emp)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def show(self):
        print(f"{self.name}: {self.salary}")


emp = Employee("Rahul", 50000)
emp.increase_salary(5000)
emp.show()


# ============================================================
# 8. DEFAULT VALUES IN A PARAMETERIZED CONSTRUCTOR
# ============================================================
# Python also allows constructor parameters to have default
# values. This provides flexibility without requiring multiple
# constructors.

class Employee:
    def __init__(self, name="Unknown", salary=0):
        self.name = name
        self.salary = salary


emp1 = Employee()
emp2 = Employee("Rahul")
emp3 = Employee("Shantanu", 60000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
print(emp3.name, emp3.salary)


# ============================================================
# IMPORTANT NOTE
# ============================================================
# Python does not support traditional constructor overloading
# like:
#
# __init__()
# __init__(name)
# __init__(name, salary)
#
# Defining the same method multiple times simply replaces the
# previous definition.
#
# Use default arguments, *args/**kwargs, or alternative class
# methods when different construction patterns are required.
# ============================================================


# ============================================================
# QUICK SUMMARY
# ============================================================
# __init__()      -> automatically initializes a new instance
# self            -> reference to the current instance
# self.name       -> instance attribute
# name            -> local parameter/variable
#
# emp = Employee("Rahul", 50000)
#              ↓
# object created
#              ↓
# __init__(emp, "Rahul", 50000)
#              ↓
# emp.name = "Rahul"
# emp.salary = 50000
#
# Most important idea:
# self.attribute stores data INSIDE THAT PARTICULAR OBJECT.
# ============================================================
