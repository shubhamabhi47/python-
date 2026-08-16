# ============================================================
# LIMITATIONS OF __del__ (DESTRUCTOR) IN PYTHON
# ============================================================
# __del__ is a finalization hook, NOT a reliable resource-
# management mechanism.
#
# Important:
#     del obj
#         ↓
#     removes a reference
#         ↓
#     object may become unreachable
#         ↓
#     Python may finalize the object
#
# The exact timing of __del__ should not be relied upon.
# ============================================================


# ============================================================
# 1. REFERENCE DEPENDENCY
# ============================================================
# An object can remain alive because another object still holds
# a reference to it.

class Account:
    def __init__(self, number):
        self.number = number

    def __del__(self):
        print("Account finalized")


class Employee:
    def __init__(self, account):
        self.account = account

    def __del__(self):
        print("Employee finalized")


acc = Account(101)
emp = Employee(acc)

del acc

# Account is still alive because:
#
#     emp.account -> Account object
#
# Removing the name acc does not destroy the Account object.

print(emp.account.number)

del emp


# ============================================================
# 2. MULTIPLE REFERENCES
# ============================================================
# The same object can be referenced by multiple variables.

class Demo:
    def __del__(self):
        print("Demo finalized")


obj1 = Demo()
obj2 = obj1
obj3 = obj1

del obj1
del obj2

print("Object still has another reference")

del obj3


# ============================================================
# 3. CIRCULAR REFERENCES
# ============================================================
# A circular reference occurs when objects refer to each other.
#
#     A -> B
#     B -> A
#
# Reference counting alone cannot immediately remove such
# objects because each object still has a reference.

class A:
    def __init__(self):
        self.b = None

    def __del__(self):
        print("A finalized")


class B:
    def __init__(self):
        self.a = None

    def __del__(self):
        print("B finalized")


a = A()
b = B()

a.b = b
b.a = a

del a
del b


# ============================================================
# 4. GARBAGE COLLECTOR AND CIRCULAR REFERENCES
# ============================================================
# Python's cyclic garbage collector can detect unreachable
# reference cycles.

import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __del__(self):
        print(f"{self.name} finalized")


a = Node("A")
b = Node("B")

a.next = b
b.next = a

del a
del b

gc.collect()


# ============================================================
# 5. EXCEPTION INSIDE __del__
# ============================================================
# Exceptions raised inside __del__ are problematic.
#
# Python generally reports them as "Exception ignored in..."
# instead of propagating them normally to the surrounding code.

class Data:
    def __del__(self):
        x = 10 / 0


d = Data()
del d


# ============================================================
# 6. DO NOT USE __del__ FOR EXCEPTION HANDLING
# ============================================================
# __del__ is not equivalent to try/except/finally.
#
# Exception handling should happen explicitly.

try:
    raise ValueError("Critical failure")
except ValueError as error:
    print(f"Caught: {error}")
finally:
    print("Cleanup executed")


# ============================================================
# 7. finally VS __del__
# ============================================================
# finally:
#     deterministic control-flow cleanup
#
# __del__:
#     object-finalization mechanism whose timing should not
#     be relied upon.
#
# Therefore, if cleanup MUST happen after an operation,
# finally is usually safer.

resource = None

try:
    resource = "Resource acquired"
    print(resource)
    raise RuntimeError("Operation failed")
except RuntimeError as error:
    print(error)
finally:
    resource = None
    print("Resource released")


# ============================================================
# 8. FILE HANDLING: BAD VS GOOD APPROACH
# ============================================================
# BAD:
# relying on __del__ to close a file.
#
# GOOD:
# using a context manager.

with open("example.txt", "w") as file:
    file.write("Hello Python")

# The file is closed automatically when leaving the with block,
# including when an exception occurs.


# ============================================================
# 9. CONTEXT MANAGER FOR CUSTOM RESOURCES
# ============================================================
# Context managers provide deterministic acquisition and
# release of resources.

class Database:
    def connect(self):
        print("Database connected")

    def close(self):
        print("Database closed")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


with Database() as db:
    print("Executing query")


# ============================================================
# 10. CLEANUP EVEN WHEN AN EXCEPTION OCCURS
# ============================================================

class Database:
    def __enter__(self):
        print("Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Connection closed")
        return False


try:
    with Database() as db:
        print("Running query")
        raise RuntimeError("Query failed")
except RuntimeError as error:
    print(f"Caught: {error}")


# ============================================================
# 11. WHY __del__ IS DANGEROUS FOR CRITICAL CLEANUP
# ============================================================
# Suppose a database connection MUST be closed.
#
# If cleanup is placed only inside __del__, timing can depend
# on:
#
#     • remaining references
#     • circular references
#     • garbage collection
#     • interpreter shutdown
#     • object resurrection
#     • implementation details
#
# Therefore:
#
#     __del__ -> fallback/finalization
#     close()  -> explicit cleanup
#     with     -> preferred deterministic cleanup


class Connection:
    def __init__(self):
        self.closed = False
        print("Connected")

    def close(self):
        if not self.closed:
            self.closed = True
            print("Closed")

    def __del__(self):
        # Only a defensive fallback.
        self.close()


connection = Connection()

try:
    print("Using connection")
finally:
    connection.close()


# ============================================================
# 12. ADVANCED: OBJECT RESURRECTION
# ============================================================
# __del__ can theoretically make an object reachable again.
# This is called resurrection and should generally be avoided.

resurrected = None


class Demo:
    def __del__(self):
        global resurrected
        resurrected = self
        print("Finalizer executed")


obj = Demo()

del obj

print(resurrected)


# ============================================================
# 13. FINALIZATION IS NOT THE SAME AS del
# ============================================================
# Consider:
#
#     obj = Demo()
#     other = obj
#     del obj
#
# The object is NOT necessarily destroyed because `other`
# still references it.
#
# del only removes the name `obj`.

class Demo:
    def __del__(self):
        print("Finalized")


obj = Demo()
other = obj

del obj

print("Still alive:", other)

del other


# ============================================================
# 14. SAFE PATTERN FOR RESOURCE OWNERSHIP
# ============================================================
# Use explicit close() + context manager.
#
# __del__ can optionally act as a final safety net, but should
# never be the primary cleanup mechanism.

class FileResource:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def write(self, data):
        self.file.write(data)

    def close(self):
        if not self.file.closed:
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass


with FileResource("data.txt") as resource:
    resource.write("Python OOP")


# ============================================================
# 15. IMPORTANT DESIGN RULE
# ============================================================
# Never depend on:
#
#     __del__()
#
# for operations that MUST happen at a specific time.
#
# Prefer:
#
#     Explicit method:
#         obj.close()
#
#     finally:
#         cleanup()
#
#     Context manager:
#         with resource:
#             ...
#
# These approaches make the lifetime of resources explicit
# and predictable.


# ============================================================
# FINAL SUMMARY
# ============================================================
# __del__ limitations:
#
# 1. del only removes a reference.
# 2. Multiple references delay finalization.
# 3. Circular references complicate object lifetime.
# 4. Garbage collection timing is not a precise scheduling tool.
# 5. __del__ may run during interpreter shutdown.
# 6. Exceptions inside __del__ are not normally propagated.
# 7. __del__ can theoretically resurrect an object.
# 8. Critical resources should not depend on __del__.
#
# BEST PRACTICE:
#
#     Resource cleanup -> with / __exit__()
#     Guaranteed local cleanup -> finally
#     Explicit lifecycle -> close()
#     __del__ -> optional finalization/fallback
# ============================================================