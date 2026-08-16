# ============================================================
# isinstance()
# ============================================================
# isinstance(object, classinfo) returns True if object is an
# instance of the specified class/type, otherwise False.
#
# Unlike type(obj) == Class, isinstance() also considers the
# inheritance hierarchy.
# ============================================================


class Demo:
    pass


obj = Demo()

print(isinstance(obj, Demo))  # True
print(isinstance(obj, int))   # False


# ============================================================
# USING isinstance() WITH CONTROL FLOW
# ============================================================
# isinstance() is useful when program behavior needs to depend
# on the runtime type of an object.

if isinstance(obj, Demo):
    print("Object belongs to Demo")
else:
    print("Object belongs to another type")


# ============================================================
# isinstance() WITH BUILT-IN TYPES
# ============================================================
# classinfo can also be a built-in type.

value = 100

print(isinstance(value, int))    # True
print(isinstance(value, str))    # False
print(isinstance(value, object)) # True


# ============================================================
# MULTIPLE TYPES
# ============================================================
# The second argument can be a tuple of types.
# The result is True if the object matches ANY type in the tuple.

value = 10

print(isinstance(value, (int, float)))  # True
print(isinstance("10", (int, float)))   # False


# ============================================================
# isinstance() AND INHERITANCE
# ============================================================
# An object of a child class is also considered an instance of
# its parent class.
#
# This is the major advantage over:
#
# type(obj) == Parent
#
# which only checks the object's exact class.

class Employee:
    pass


class Manager(Employee):
    pass


manager = Manager()

print(isinstance(manager, Manager))  # True
print(isinstance(manager, Employee)) # True
print(isinstance(manager, object))   # True


# ============================================================
# type() vs isinstance()
# ============================================================
# type(obj) == Class checks the EXACT runtime class.
#
# isinstance(obj, Class) checks whether the object belongs to
# Class OR derives from Class.

print(type(manager) == Manager)  # True
print(type(manager) == Employee) # False

print(isinstance(manager, Manager))  # True
print(isinstance(manager, Employee)) # True


# ============================================================
# PRACTICAL POLYMORPHIC CHECK
# ============================================================
# isinstance() can be used when different objects need different
# handling based on their type/class.
#
# However, in Python, EAFP and duck typing are often preferred
# when explicit type checking is unnecessary.

def process(value):
    if isinstance(value, int):
        return value * 2
    if isinstance(value, str):
        return value.upper()
    return value


print(process(10))
print(process("hello"))


# ============================================================
# KEY IDEA
# ============================================================
# isinstance(obj, Class)
#        ↓
# Checks whether obj is an instance of Class
#        ↓
# Also considers subclasses/inheritance
#
# type(obj) == Class
#        ↓
# Checks only the exact runtime class
#
# Prefer isinstance() when an inheritance-aware type check is
# actually required.
# ============================================================