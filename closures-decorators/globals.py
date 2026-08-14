# ============================================================
# SYMBOL TABLES IN PYTHON
# ============================================================
#
# A symbol table stores the mapping between names (identifiers)
# and the objects/values they refer to.
#
# Python provides:
#
#     globals() → current global namespace
#     locals()  → current local namespace
#
# Both return a dictionary-like object.
#
# ============================================================
# 1. globals()
# ============================================================
#
# globals() returns a dictionary containing names available
# in the current global/module scope.
#
# For example, after:
#
#     a = 10
#
# the global symbol table contains an entry similar to:
#
#     "a" → 10
#
# Functions, imported modules, and other global names are also
# stored in this namespace.
#
# ============================================================

a = 10


def demo():
    print("Hello")


global_vars = globals()

print(global_vars)
print(global_vars["a"])  # Output: 10


# ============================================================
# 2. MODIFYING GLOBAL VARIABLES USING globals()
# ============================================================
#
# Since globals() provides access to the global namespace,
# we can change an existing name or create a new one.
#
#     globals()["a"] = 20
#
# changes the object referenced by the global name "a".
#
# Therefore:
#
#     print(a)
#
# gives:
#
#     20
#
# ============================================================

globals()["a"] = 20

print(a)


# Creating a new global variable dynamically

globals()["x"] = 100

# print(x)


# ============================================================
# 3. locals()
# ============================================================
#
# locals() returns the local namespace of the current scope.
#
# Inside a function, it can contain local variables created
# during that function's execution.
#
# Example:
#
#     b = 30
#
# creates a local name "b".
#
# locals() allows us to inspect that namespace.
#
# ============================================================

def demo_local():
    b = 30

    print(locals())
    print(locals()["b"])


demo_local()


# ============================================================
# 4. globals() VS locals()
# ============================================================
#
# globals():
#
#     Represents the current global/module namespace.
#
# locals():
#
#     Represents the current local namespace.
#
# Example:
#
#     a = 10
#
#     def demo():
#         b = 20
#
#         globals() → contains "a"
#         locals()  → contains "b"
#
# ============================================================
# 5. IMPORTANT SCOPE CONCEPT
# ============================================================
#
# A function creates its own local scope when it executes.
#
# Example:
#
#     def demo():
#         b = 30
#
# "b" belongs to demo's local scope.
#
# Once the function finishes, that local execution scope is
# no longer active.
#
# ============================================================
# 6. IMPORTANT DIFFERENCE
# ============================================================
#
# globals() can be used to dynamically create or modify global
# names:
#
#     globals()["a"] = 50
#
# locals() should primarily be treated as a way to INSPECT
# the current local namespace.
#
# Modifying the dictionary returned by locals() is not a
# reliable way to create or change local variables inside a
# function.
#
# Example:
#
#     locals()["b"] = 100
#
# does NOT reliably mean that the actual local variable "b"
# will become 100.
#
# Python implementations may optimize local variables using
# internal storage rather than treating locals() as a normal
# writable dictionary.
#
# ============================================================
# 7. DEEPER MENTAL MODEL
# ============================================================
#
# Think of namespaces as dictionaries that map:
#
#     NAME → OBJECT
#
# Example:
#
#     a = 10
#
# conceptually creates:
#
#     "a" → 10
#
# And:
#
#     def demo():
#         b = 30
#
# creates a local mapping during execution:
#
#     "b" → 30
#
# globals() and locals() allow us to inspect these mappings.
#
# ============================================================
# KEY POINTS
# ============================================================
#
# 1. globals() → current global namespace.
#
# 2. locals() → current local namespace.
#
# 3. Both provide dictionary-like mappings of names to values.
#
# 4. globals() can be used to dynamically create/modify global
#    names.
#
# 5. locals() is mainly used for inspecting the current local
#    namespace.
#
# 6. A function has its own local scope during execution.
#
# 7. Namespace lookup is fundamentally about finding the object
#    associated with a particular name.
#
# ============================================================
