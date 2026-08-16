# Just to clarify, destructor does not delete the object, garbage collector does. 
# Object is deleted by the Garbage Collector if there is no reference to the object. 
# Destructor just acts like a clean up code for the object. The flow is, 
# when an object is not having any reference to it, the Garbage collector will destroy the object 
# but before destroying the object, the Garbage Collector will check if there is any _del_ method written,
# which is destructor. If written, the _del_ method will be executed first 
# and then the object will be destroyed.

# In short:
# Garbage Collector: Responsible for destroying the object
# Destructor: Responsible for the clean up code just before the object is destroyed. It does not destroy the object

# ============================================================
# DESTRUCTOR (__del__) IN PYTHON
# ============================================================
# A destructor is a special method named __del__().
#
# __init__() is commonly used for initialization.
# __del__() is called when Python is finalizing an object.
#
# IMPORTANT:
# __del__() should NOT be treated as a guaranteed or precise
# resource-management mechanism.
#
# Python uses reference counting in CPython plus a cyclic
# garbage collector. Object finalization timing can differ
# between implementations and situations.
# ============================================================


# ============================================================
# 1. BASIC DESTRUCTOR
# ============================================================
class Example:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


obj = Example()
del obj


# ============================================================
# 2. OBJECT LIFECYCLE
# ============================================================
# Typical lifecycle:
#
#     Object creation
#          ↓
#     __init__()
#          ↓
#     Object is used
#          ↓
#     References disappear
#          ↓
#     Object becomes unreachable
#          ↓
#     __del__() may run during finalization
#
# del obj deletes the reference named obj.
# It does NOT directly mean "free this object immediately".
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"{self.name} created")

    def display(self):
        print(f"{self.name}: ₹{self.salary}")

    def __del__(self):
        print(f"{self.name} finalized")


e1 = Employee("Rahul", 50000)
e1.display()

del e1


# ============================================================
# 3. del vs __del__
# ============================================================
# These are completely different concepts.
#
# del obj:
#     Removes the variable/reference named obj.
#
# __del__():
#     Special method that Python may invoke while finalizing
#     an object.
#
# Therefore:
#
#     del obj
#
# does NOT directly call:
#
#     obj.__del__()
#
# It removes a reference, and if the object becomes unreachable,
# finalization can occur.


# ============================================================
# 4. MULTIPLE REFERENCES
# ============================================================
# Multiple variables can refer to the same object.
#
# The object remains alive as long as references to it remain.

class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object finalized")


obj1 = Demo()
obj2 = obj1

del obj1

print("obj2 still refers to the object")

del obj2


# ============================================================
# 5. OBJECT IDENTITY
# ============================================================
# obj1 and obj2 below refer to the SAME object.

class Demo:
    def __del__(self):
        print("Object finalized")


obj1 = Demo()
obj2 = obj1

print(id(obj1))
print(id(obj2))
print(obj1 is obj2)

del obj1
del obj2


# ============================================================
# 6. REASSIGNMENT ALSO REMOVES A REFERENCE
# ============================================================
# When obj is reassigned, the old object loses the reference
# previously held by obj.

class Demo:
    def __init__(self, name):
        self.name = name
        print(f"{name} created")

    def __del__(self):
        print(f"{self.name} finalized")


obj = Demo("A")
obj = Demo("B")


# ============================================================
# 7. DESTRUCTOR WITH RESOURCE MANAGEMENT
# ============================================================
# __del__ can sometimes be used as a final safety mechanism,
# but it is NOT the preferred way to manage critical resources.
#
# For files, sockets, database connections, locks, etc.,
# prefer deterministic cleanup using:
#
#     with
#
# context managers.
# ============================================================

class Resource:
    def __init__(self):
        self.closed = False
        print("Resource acquired")

    def close(self):
        if not self.closed:
            self.closed = True
            print("Resource released")

    def __del__(self):
        # Best treated as a fallback cleanup mechanism.
        self.close()


resource = Resource()
resource.close()


# ============================================================
# 8. PREFERRED WAY: CONTEXT MANAGER
# ============================================================
# For deterministic resource cleanup, use __enter__() and
# __exit__() with the with statement.

class Resource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with Resource() as resource:
    print("Using resource")


# ============================================================
# 9. DESTRUCTOR AND EXCEPTIONS
# ============================================================
# Exceptions raised inside __del__ are not normally propagated
# like ordinary exceptions.
#
# Therefore __del__ should be kept simple and robust.

class Demo:
    def __del__(self):
        try:
            print("Cleanup")
        except Exception:
            pass


obj = Demo()
del obj


# ============================================================
# 10. CIRCULAR REFERENCES
# ============================================================
# Objects can reference each other.
#
# Simple reference counting alone cannot immediately remove
# such cycles, so Python's cyclic garbage collector handles
# unreachable cycles.

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"{self.name} finalized")


a = Node("A")
b = Node("B")

a.other = b
b.other = a

del a
del b


# ============================================================
# 11. FORCING GARBAGE COLLECTION
# ============================================================
# Python provides the gc module for garbage-collector control.
#
# gc.collect() requests a garbage-collection cycle.
# It should not normally be required in everyday code.

import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"{self.name} finalized")


a = Node("A")
b = Node("B")

a.other = b
b.other = a

del a
del b

gc.collect()


# ============================================================
# 12. __del__ IS NOT A GUARANTEED "MEMORY FREE" HOOK
# ============================================================
# Important distinction:
#
#     __del__() -> object finalization hook
#
#     memory release -> handled by Python's implementation/
#                       allocator/garbage collector
#
# You should not use __del__ to assume an exact destruction
# time.


# ============================================================
# 13. __del__ AT PROGRAM EXIT
# ============================================================
# Objects that survive until interpreter shutdown may be
# finalized during interpreter shutdown.
#
# Do not rely on exact ordering of destruction at shutdown.
#
# This is another reason __del__ is unsuitable for critical
# cleanup logic.


# ============================================================
# 14. ADVANCED: WEAK REFERENCES
# ============================================================
# weakref allows you to refer to an object without keeping it
# alive through a strong reference.

import weakref


class Employee:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} finalized")


employee = Employee("Rahul")
weak_employee = weakref.ref(employee)

print(weak_employee())
print(weak_employee() is employee)

del employee

print(weak_employee())


# ============================================================
# 15. ADVANCED: __del__ CAN RESURRECT AN OBJECT
# ============================================================
# An object can theoretically make itself reachable again
# from __del__().
#
# This behavior is called object resurrection.
#
# It is highly discouraged because it makes object lifetime
# difficult to reason about.

resurrected = None


class Demo:
    def __del__(self):
        global resurrected
        resurrected = self
        print("Object resurrected")


obj = Demo()

del obj

print(resurrected)


# ============================================================
# 16. IMPORTANT OOP RULE
# ============================================================
# Do NOT use __del__ as the primary mechanism for:
#
#     • closing database connections
#     • closing files
#     • releasing locks
#     • network cleanup
#     • managing transactions
#
# Prefer:
#
#     with open(...) as file:
#         ...
#
# or explicit methods such as:
#
#     connection.close()
#
# or context managers:
#
#     with DatabaseConnection() as db:
#         ...


# ============================================================
# 17. FINAL COMPARISON
# ============================================================
# Constructor:
#
#     __init__()
#     → initializes an already-created object.
#
# Destructor:
#
#     __del__()
#     → finalization hook called when Python determines that
#       an object is being finalized.
#
# del:
#
#     del obj
#     → removes a reference/name.
#
# Garbage Collector:
#
#     gc
#     → detects and collects unreachable cyclic objects.
#
# Context Manager:
#
#     __enter__() / __exit__()
#     → preferred mechanism for deterministic resource cleanup.
# ============================================================


# ============================================================
# 18. INTERVIEW-LEVEL EXAMPLE
# ============================================================

class Database:
    def __init__(self):
        self.connected = True
        print("Connected")

    def close(self):
        if self.connected:
            self.connected = False
            print("Connection closed")

    def __del__(self):
        # Fallback only; deterministic cleanup should use close()
        self.close()


db = Database()

# Explicit cleanup is preferable when the API requires it.
db.close()

del db


# ============================================================
# KEY TAKEAWAYS
# ============================================================
# 1. __del__ is Python's destructor/finalization hook.
# 2. del removes a reference; it does not directly destroy
#    an object.
# 3. An object may have multiple references.
# 4. In CPython, reference counting often causes prompt
#    finalization when the reference count reaches zero.
# 5. Cyclic references are handled by the cyclic GC.
# 6. __del__ timing should not be relied upon for critical
#    resource management.
# 7. __del__ can have tricky behavior with cycles, shutdown,
#    exceptions, and resurrection.
# 8. Use context managers for deterministic resource cleanup.
# ============================================================