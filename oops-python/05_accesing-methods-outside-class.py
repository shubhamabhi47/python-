# ============================================================
# ACCESSING ATTRIBUTES AND METHODS FROM OUTSIDE A CLASS
# ============================================================
# A class-level attribute is stored on the class itself and can
# be accessed through an object using dot notation.
#
# IMPORTANT:
# If an object does not have an attribute in its own namespace,
# Python can look for it in the class namespace.
# ============================================================

class Employee:
    salary = 2000
    name = "John"

e1 = Employee()

print(e1.salary)
print(e1.name)


# ============================================================
# MODIFYING A CLASS ATTRIBUTE THROUGH AN OBJECT
# ============================================================
# This is an important Python behavior:
#
# e1.salary = 3000 does NOT normally modify Employee.salary.
#
# Instead, Python creates an instance attribute named salary in
# e1's namespace.
#
# This instance attribute now SHADOWS the class attribute for e1.
# ============================================================

e1.salary = 3000

print(e1.salary)       # 3000
print(Employee.salary) # 2000


# ============================================================
# ATTRIBUTE SHADOWING
# ============================================================
# e1 has its own salary, while e2 still finds salary on the class.

e2 = Employee()

print(e1.__dict__)  # {'salary': 3000}
print(e2.__dict__)  # {}

print(e1.salary)    # 3000 -> instance attribute
print(e2.salary)    # 2000 -> class attribute


# ============================================================
# CLASS ATTRIBUTE CHANGES
# ============================================================
# If no instance attribute shadows the class attribute, changing
# the class attribute is visible through all such objects.

Employee.salary = 5000

print(e2.salary)    # 5000
print(e1.salary)    # 3000 -> still shadowed by e1's own attribute


# ============================================================
# ATTRIBUTE LOOKUP
# ============================================================
# Simplified lookup:
#
# e1.salary
#     ↓
# Check e1's instance namespace
#     ↓
# Found? -> use it
# Not found?
#     ↓
# Check class namespace
#     ↓
# Found? -> use class attribute
#
# Therefore:
#
# e1.__dict__["salary"] -> 3000
# Employee.__dict__["salary"] -> 5000


# ============================================================
# ACCESSING METHODS FROM OUTSIDE THE CLASS
# ============================================================
# A method can be called using:
#
# object.method()
#
# Python automatically binds the object as the first argument
# (self) when an instance method is accessed through an object.

class Employee:
    salary = 2000

    def display(self):
        print("Displaying method output")


e1 = Employee()
e1.display()


# ============================================================
# METHOD ACCESS IS ALSO ATTRIBUTE LOOKUP
# ============================================================
# e1.display searches for 'display'.
# It is not found in e1.__dict__, so Python finds it in the class.
#
# Because display is a function defined on the class, accessing it
# through e1 produces a bound method with e1 attached as self.
#
# Conceptually:
#
# e1.display()
# is equivalent to:
# Employee.display(e1)


Employee.display(e1)


# ============================================================
# CLASS ATTRIBUTE vs INSTANCE ATTRIBUTE
# ============================================================
# Class attribute:
#     Shared by instances through class lookup.
#
# Instance attribute:
#     Belongs specifically to one object.
#
# Assigning through an object:
#     e1.salary = 3000
#
# creates/shadows an instance attribute rather than changing the
# class attribute.
# ============================================================

class Employee:
    company = "ABC"

e1 = Employee()
e2 = Employee()

e1.company = "XYZ"

print(e1.company)       # XYZ
print(e2.company)       # ABC
print(Employee.company) # ABC