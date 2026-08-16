# ============================================================
# TOPIC: Class Attributes vs Instance Attributes
# ============================================================
# Class attributes are defined directly inside the class body.
# They belong to the class and are shared by all instances.
# Instance attributes belong to a specific object and are unique
# to that object.
# ============================================================

class Employee:
    # Class attribute: shared by every Employee object.
    company = "Google"

    def __init__(self, name, salary):
        # Instance attributes: each object gets its own values.
        self.name = name
        self.salary = salary

e1 = Employee("Alice", 3000)
e2 = Employee("Bob", 4000)

print(e1.company)   # Google
print(e2.company)   # Google
print(e1.name)      # Alice
print(e2.name)      # Bob
print(e1.salary)    # 3000
print(e2.salary)    # 4000

# ============================================================
# TOPIC: Accessing Class Attributes
# ============================================================
# Class attributes can be accessed through the class itself.
# This is generally the clearest way to modify shared class data.

print(Employee.company)

Employee.company = "Microsoft"

print(e1.company)   # Microsoft
print(e2.company)   # Microsoft

# ============================================================
# TOPIC: Instance Attribute Override
# ============================================================
# Assigning an attribute through an instance creates/updates an
# instance attribute. It does NOT modify the class attribute.
# The instance attribute shadows the class attribute for that object.

e1.company = "Amazon"

print(e1.company)   # Amazon
print(e2.company)   # Microsoft
print(Employee.company)  # Microsoft

# e1 now has its own company attribute, while e2 still reads
# the shared class attribute.

# ============================================================
# TOPIC: Attribute Lookup
# ============================================================
# Python generally looks for an attribute in this order:
# 1. Instance
# 2. Class
# 3. Parent classes through the MRO
# This is why e1.company returns "Amazon" after the override.

print(e1.__dict__)  # {'name': 'Alice', 'salary': 3000, 'company': 'Amazon'}
print(e2.__dict__)  # {'name': 'Bob', 'salary': 4000}

# ============================================================
# TOPIC: Inspecting Class Attributes
# ============================================================
# __dict__ shows attributes stored directly on an object/class.
# vars() provides a convenient equivalent for inspecting __dict__.

print(Employee.__dict__)
print(vars(Employee))

# ============================================================
# TOPIC: Dynamic Instance Attributes
# ============================================================
# Python allows attributes to be added to an existing instance.
# This creates data only for that particular object.

e2.department = "Engineering"

print(e2.department)
print(e1.__dict__)
print(e2.__dict__)

# ============================================================
# TOPIC: Important Mutable Class Attribute Pitfall
# ============================================================
# Mutable class attributes such as lists/dictionaries are shared.
# Modifying the object through one instance affects every instance
# that is still referencing the same class-level object.

class Team:
    members = []

t1 = Team()
t2 = Team()

t1.members.append("Alice")

print(t1.members)  # ['Alice']
print(t2.members)  # ['Alice']
print(Team.members)  # ['Alice']

# ============================================================
# TOPIC: Correct Use of Per-Instance Mutable Data
# ============================================================
# Create mutable data inside __init__ so every instance receives
# its own independent object.

class Team:
    def __init__(self):
        self.members = []

t1 = Team()
t2 = Team()

t1.members.append("Alice")

print(t1.members)  # ['Alice']
print(t2.members)  # []

# ============================================================
# TOPIC: When to Use Class vs Instance Attributes
# ============================================================
# Use class attributes for constants/configuration/shared state
# that conceptually belongs to the class.
# Use instance attributes for data that varies between objects.

class Employee:
    company = "Microsoft"
    minimum_salary = 1500

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Alice", 3000)
e2 = Employee("Bob", 4000)

# Shared data
print(Employee.company)
print(Employee.minimum_salary)

# Object-specific data
print(e1.name, e1.salary)
print(e2.name, e2.salary)

# ============================================================
# TOPIC: Advanced Example
# ============================================================
# Class attributes can also represent shared counters or metadata.
# Here, every object contributes to the same class-level counter.

class Employee:
    company = "Microsoft"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

e1 = Employee("Alice", 3000)
e2 = Employee("Bob", 4000)

print(Employee.employee_count)  # 2

# Use the class explicitly when modifying shared state.
# Using self.employee_count += 1 would create an instance attribute
# instead of reliably updating the shared class attribute.

# ============================================================
# KEY TAKEAWAY
# ============================================================
# Class attribute:
#     Employee.company
#     Shared at class level.
#
# Instance attribute:
#     e1.salary
#     Stored separately for each object.
#
# Important rule:
#     e1.x = value
#     normally creates/updates x on e1, not on the class.
#
# Attribute lookup:
#     instance -> class -> parent classes
#
# Therefore, an instance attribute can shadow a class attribute
# without changing the original class attribute.