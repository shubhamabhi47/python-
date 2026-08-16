# ============================================================
# OPERATOR OVERLOADING: RICH COMPARISON METHODS
# ============================================================
# Python allows comparison operators to work with user-defined
# objects by implementing special comparison methods.
#
# >   -> __gt__()
# <   -> __lt__()
# ==  -> __eq__()
# !=  -> __ne__()
# >=  -> __ge__()
# <=  -> __le__()
#
# Example:
#     h1 > h2
#
# Internally Python attempts:
#     h1.__gt__(h2)
# ============================================================


# ============================================================
# 1. COMPARING OBJECTS WITHOUT __gt__()
# ============================================================
# Python does not automatically know which property of a Hotel
# should determine whether one hotel is "greater" than another.

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price


h1 = Hotel("Taj", 5000)
h2 = Hotel("Oberoi", 3000)

# print(h1 > h2)  # TypeError


# ============================================================
# 2. OVERLOADING > WITH __gt__()
# ============================================================
# __gt__(self, other):
#
# self  -> left-hand object
# other -> right-hand object
#
# h1 > h2
#     ↓
# h1.__gt__(h2)

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


h1 = Hotel("Taj", 5000)
h2 = Hotel("Oberoi", 3000)

print(h1 > h2)
print(h1.__gt__(h2))


# ============================================================
# 3. USING COMPARISON IN CONDITIONAL LOGIC
# ============================================================
# Since __gt__() returns a boolean, the result can directly be
# used in if/else statements.

if h1 > h2:
    print(f"{h1.name} is more expensive than {h2.name}")
else:
    print(f"{h2.name} is more expensive or equal")


# ============================================================
# 4. ROBUST TYPE HANDLING
# ============================================================
# Returning NotImplemented for unsupported types is preferred
# over blindly accessing attributes on the other object.
#
# NotImplemented tells Python that this implementation does not
# support the given operand type.

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price > other.price


h1 = Hotel("Taj", 5000)
h2 = Hotel("Oberoi", 3000)

print(h1 > h2)


# ============================================================
# 5. IMPLEMENTING ALL RICH COMPARISON OPERATORS
# ============================================================
# Python provides six primary rich comparison methods:
#
# __eq__ -> ==
# __ne__ -> !=
# __lt__ -> <
# __le__ -> <=
# __gt__ -> >
# __ge__ -> >=

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price == other.price

    def __ne__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price != other.price

    def __lt__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price >= other.price


h1 = Hotel("Taj", 5000)
h2 = Hotel("Oberoi", 3000)

print(h1 == h2)
print(h1 != h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)


# ============================================================
# 6. COMPARING BASED ON MULTIPLE ATTRIBUTES
# ============================================================
# A comparison does not have to depend on only one attribute.
#
# Here:
#     1. Higher rating wins.
#     2. If ratings are equal, lower price wins.

class Hotel:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __lt__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented

        if self.rating != other.rating:
            return self.rating < other.rating

        return self.price > other.price


h1 = Hotel("Taj", 5000, 4.5)
h2 = Hotel("Oberoi", 3000, 4.5)

print(h1 < h2)


# ============================================================
# 7. USING sorted() WITH CUSTOM OBJECTS
# ============================================================
# sorted() can use comparison behavior defined by the class.
#
# However, for real-world code, key= is often clearer and more
# efficient than implementing every comparison method.

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}({self.price})"

    def __lt__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price < other.price


hotels = [
    Hotel("Taj", 5000),
    Hotel("Oberoi", 3000),
    Hotel("ITC", 4000)
]

print(sorted(hotels))


# ============================================================
# 8. BETTER APPROACH FOR sorted(): key=
# ============================================================
# If the only requirement is sorting by a particular attribute,
# key= is generally preferable.
#
# It avoids implementing comparison methods unnecessarily.

hotels = [
    Hotel("Taj", 5000),
    Hotel("Oberoi", 3000),
    Hotel("ITC", 4000)
]

print(sorted(hotels, key=lambda hotel: hotel.price))
print(sorted(hotels, key=lambda hotel: hotel.price, reverse=True))


# ============================================================
# 9. functools.total_ordering
# ============================================================
# Python's functools.total_ordering can generate missing ordering
# methods when you define __eq__() and one ordering method such as
# __lt__().
#
# It reduces boilerplate but can add some runtime overhead.
#
# For small/simple classes it is convenient; for performance-
# sensitive code, explicitly implementing comparisons can be better.

from functools import total_ordering


@total_ordering
class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.price < other.price


h1 = Hotel("Taj", 5000)
h2 = Hotel("Oberoi", 3000)

print(h1 > h2)
print(h1 >= h2)
print(h1 <= h2)


# ============================================================
# 10. POLYMORPHISM THROUGH OPERATORS
# ============================================================
# The same > syntax can operate on completely different types.
#
# int:
#     10 > 5
#
# Hotel:
#     h1 > h2
#
# The operator dispatches according to the operand types.
#
# This is one example of Python's polymorphic behavior.

print(10 > 5)
print(h1 > h2)


# ============================================================
# 11. ADVANCED: COMPARISON BY VALUE VS IDENTITY
# ============================================================
# == checks VALUE EQUALITY through __eq__().
#
# is checks OBJECT IDENTITY and cannot be overloaded.
#
# Two different Hotel objects can represent equal data while
# still being different objects.

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.name == other.name and self.price == other.price


h1 = Hotel("Taj", 5000)
h2 = Hotel("Taj", 5000)
h3 = h1

print(h1 == h2)  # Same value
print(h1 is h2)  # Different objects

print(h1 == h3)  # Same value
print(h1 is h3)  # Same object


# ============================================================
# 12. IMPORTANT: __eq__() AND HASHING
# ============================================================
# If a class defines custom equality, be careful with hashing.
#
# Objects used as dictionary keys or set members must have a
# compatible __hash__() implementation.
#
# Mutable objects should generally NOT be hashable based on
# mutable attributes.

class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Hotel):
            return NotImplemented
        return self.name == other.name and self.price == other.price


h1 = Hotel("Taj", 5000)

print(h1.__hash__)  # None because custom __eq__ disables hashing


# ============================================================
# 13. REVERSE COMPARISON AND SUBCLASSES
# ============================================================
# Rich comparison dispatch is more sophisticated than simply
# calling the left operand's method.
#
# Python can consider the reflected/reverse comparison method
# and gives a more-specific subclass implementation priority
# when appropriate.
#
# This is another reason to return NotImplemented instead of
# False when an operand type is unsupported.


# ============================================================
# KEY IDEA
# ============================================================
# Rich comparison methods allow objects to define meaningful
# relationships:
#
#     h1 > h2   -> __gt__()
#     h1 < h2   -> __lt__()
#     h1 == h2  -> __eq__()
#
# The operator itself remains unchanged.
# Only the behavior of that operator for your class is defined.
#
# BEST PRACTICE:
#     • Compare meaningful attributes.
#     • Return NotImplemented for unsupported types.
#     • Return a boolean for normal comparisons.
#     • Use key= with sorted() when you only need sorting.
#     • Keep equality logically consistent.
#     • Understand == (value equality) vs is (identity).
# ============================================================