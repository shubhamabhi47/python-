# ============================================================
# BUILT-IN CLASS ATTRIBUTES / CLASS METADATA
# ============================================================
# Python automatically provides classes with special attributes
# containing metadata about the class.
#
# These attributes are useful for introspection/reflection:
# __doc__    -> documentation string
# __name__   -> class name
# __module__ -> module where the class was defined
#
# These are different from normal application attributes such as
# salary or name.
# ============================================================


# ============================================================
# 1. __doc__
# ============================================================
# __doc__ stores the class's docstring.
#
# The docstring must be a string literal appearing as the first
# statement in the class body.
#
# If no docstring is provided, __doc__ is usually None.

class Student:
    """Represents a student and stores student-related data."""
    pass

print(Student.__doc__)


# ============================================================
# 2. __name__
# ============================================================
# __name__ contains the class's name as a string.
#
# It is useful when class information needs to be inspected
# dynamically.

class Student:
    pass

print(Student.__name__)


# ============================================================
# 3. __module__
# ============================================================
# __module__ contains the name of the module in which the class
# was defined.
#
# A class defined directly in the executed Python file normally
# has:
#
# __module__ == "__main__"
#
# When imported from another module, it contains that module's
# name instead.

class Student:
    pass

print(Student.__module__)


# ============================================================
# 4. COMBINING CLASS METADATA
# ============================================================
# These attributes allow a program to inspect information about
# a class without manually storing that metadata.

class MyClass:
    """Information about MyClass."""

    def show_info(self):
        pass


print(f"Class Name: {MyClass.__name__}")
print(f"Docstring: {MyClass.__doc__}")
print(f"Defined in Module: {MyClass.__module__}")


# ============================================================
# 5. INTROSPECTION
# ============================================================
# Introspection means examining objects/classes at runtime.
#
# Python provides many tools for this:
# type()       -> determines an object's type
# getattr()    -> dynamically retrieves an attribute
# hasattr()    -> checks for an attribute
# __dict__     -> exposes a namespace mapping
#
# The metadata attributes above are part of Python's broader
# introspection/reflection capabilities.

print(type(MyClass))
print(MyClass.__dict__.keys())


# ============================================================
# ADVANCED: __qualname__
# ============================================================
# __qualname__ stores the qualified name of a class/function.
#
# For a top-level class it is usually the same as __name__.
# For nested classes it preserves the containing scope.

class Outer:
    class Inner:
        pass

print(Outer.__name__)          # Outer
print(Outer.Inner.__name__)    # Inner
print(Outer.Inner.__qualname__) # Outer.Inner


# ============================================================
# KEY IDEA
# ============================================================
# __doc__     -> What documentation does the class have?
# __name__    -> What is the class called?
# __module__  -> Where was the class defined?
# __qualname__-> What is its qualified name?
#
# These attributes allow Python code to inspect class metadata
# dynamically at runtime.
# ============================================================