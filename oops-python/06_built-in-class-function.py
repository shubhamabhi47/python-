# ============================================================
# BUILT-IN ATTRIBUTE FUNCTIONS
# ============================================================
# Python provides built-in functions for dynamically accessing,
# modifying, checking and deleting object attributes.
#
# getattr() -> read an attribute
# setattr() -> create/update an attribute
# delattr() -> delete an attribute
# hasattr() -> check whether an attribute exists
#
# These are especially useful when the attribute name is known
# only at runtime, such as in configuration systems, serializers,
# APIs and metaprogramming.
# ============================================================


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


e = Employee("Rahul", 101)


# ============================================================
# 1. getattr()
# ============================================================
# getattr(object, attribute_name)
# Returns the value of the specified attribute.
#
# If the attribute does not exist, getattr() raises
# AttributeError unless a default value is supplied.
#
# getattr(object, attribute_name, default)
# ============================================================

print(getattr(e, "name"))
print(getattr(e, "id"))
print(getattr(e, "salary", 0))  # 0 because salary doesn't exist


# ============================================================
# 2. setattr()
# ============================================================
# setattr(object, attribute_name, value)
# Sets an existing attribute or creates a new instance attribute
# if it does not already exist.
# ============================================================

setattr(e, "name", "Rohit")
setattr(e, "salary", 50000)

print(e.name)
print(e.salary)
print(e.__dict__)


# ============================================================
# 3. delattr()
# ============================================================
# delattr(object, attribute_name)
# Deletes an attribute from the object.
#
# It is equivalent to:
# del object.attribute
# ============================================================

delattr(e, "salary")

print(hasattr(e, "salary"))  # False


# ============================================================
# 4. hasattr()
# ============================================================
# hasattr(object, attribute_name)
# Returns True if the attribute can be accessed, otherwise False.
#
# Useful before performing operations on dynamically named
# attributes.
# ============================================================

if hasattr(e, "name"):
    print("Name attribute exists")

if not hasattr(e, "salary"):
    print("Salary attribute does not exist")


# ============================================================
# 5. DYNAMIC ATTRIBUTE ACCESS
# ============================================================
# The major advantage is that the attribute name can come from
# a variable instead of being hard-coded.
#
# This is useful when processing dictionaries, user input,
# configuration files, API data, serializers, etc.
# ============================================================

attribute = "name"
print(getattr(e, attribute))

attribute = "id"
print(getattr(e, attribute))


# ============================================================
# 6. DYNAMIC ATTRIBUTE UPDATE
# ============================================================

attribute = "name"
value = "Amit"

setattr(e, attribute, value)

print(e.name)


# ============================================================
# 7. DYNAMIC ATTRIBUTE CREATION
# ============================================================

attribute = "department"
value = "Engineering"

setattr(e, attribute, value)

print(getattr(e, attribute))


# ============================================================
# 8. DYNAMIC ATTRIBUTE DELETION
# ============================================================

attribute = "department"

if hasattr(e, attribute):
    delattr(e, attribute)

print(hasattr(e, attribute))


# ============================================================
# 9. getattr() vs DOT NOTATION
# ============================================================
# Static attribute name:
#     e.name
#
# Dynamic attribute name:
#     getattr(e, "name")
#
# These are useful in different situations.

print(e.name)
print(getattr(e, "name"))


# ============================================================
# 10. getattr() WITH DEFAULT VALUE
# ============================================================
# The third argument prevents AttributeError when an attribute
# is missing.

salary = getattr(e, "salary", 0)
department = getattr(e, "department", "Not Assigned")

print(salary)
print(department)


# ============================================================
# 11. USING ALL FOUR FUNCTIONS TOGETHER
# ============================================================

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


e = Employee("Rahul", 101)

attribute = "salary"

if not hasattr(e, attribute):
    setattr(e, attribute, 50000)

print(getattr(e, attribute))

delattr(e, attribute)

print(hasattr(e, attribute))


# ============================================================
# ADVANCED: DYNAMIC METHOD CALLING
# ============================================================
# getattr() can retrieve methods as well as data attributes.
#
# If the attribute name refers to a method, getattr() returns a
# callable bound method that can then be invoked dynamically.

class Employee:
    def display(self):
        print("Employee details")

    def greet(self):
        print("Hello")


e = Employee()

method_name = "display"
method = getattr(e, method_name)
method()

# Equivalent:
# getattr(e, "display")()


# ============================================================
# KEY IDEA
# ============================================================
# getattr() -> GET attribute dynamically
# setattr() -> SET/CREATE attribute dynamically
# delattr() -> DELETE attribute dynamically
# hasattr() -> CHECK attribute dynamically
#
# These functions become powerful when attribute names are not
# known until runtime.
# ============================================================