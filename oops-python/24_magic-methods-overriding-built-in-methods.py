# ============================================================
# MAGIC METHODS / DUNDER METHODS
# ============================================================
# Magic methods are special methods whose names start and end
# with double underscores, e.g. __init__, __str__, __len__.
#
# Python automatically calls them when specific operations are
# performed on objects.
#
# Examples:
# print(obj) -> obj.__str__()
# len(obj)   -> obj.__len__()
# obj1 + obj2 -> obj1.__add__(obj2)
# obj1 == obj2 -> obj1.__eq__(obj2)
#
# They allow custom objects to behave like built-in Python types.
# ============================================================


# ============================================================
# 1. __str__() -> print(obj)
# ============================================================
# __str__ defines the user-friendly string representation of an
# object.
#
# print(obj) effectively requests:
#     obj.__str__()

class Example:
    def __str__(self):
        return "This is a custom object"


obj = Example()

print(obj)
print(str(obj))


# ============================================================
# 2. __repr__() -> repr(obj)
# ============================================================
# __repr__ is intended to provide an unambiguous/developer-friendly
# representation of an object.
#
# Ideally, repr(obj) should contain enough information to understand
# what the object represents.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}"

    def __repr__(self):
        return f"Employee(name={self.name!r}, salary={self.salary!r})"


emp = Employee("Rahul", 50000)

print(emp)
print(repr(emp))


# ============================================================
# 3. __str__ VS __repr__
# ============================================================
# str(obj):
#     Human-readable representation.
#
# repr(obj):
#     Developer/debugging representation.
#
# If __str__ is absent, Python can fall back to __repr__ for
# string conversion.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"


product = Product("Laptop", 70000)

print(product)
print(repr(product))


# ============================================================
# 4. __len__() -> len(obj)
# ============================================================
# A custom object does not automatically have a meaningful length.
#
# Implement __len__ to define what "length" means for that object.

class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


cart = Cart(["Shirt", "Phone", "Book"])

print(len(cart))


# ============================================================
# 5. __len__ MUST RETURN AN INTEGER
# ============================================================
# __len__ must return a non-negative integer.
#
# Returning another type causes TypeError.

class Demo:
    def __len__(self):
        return 10


print(len(Demo()))


# ============================================================
# 6. OPERATOR OVERLOADING
# ============================================================
# Operators are implemented through special methods.
#
# +  -> __add__()
# -  -> __sub__()
# *  -> __mul__()
# /  -> __truediv__()
# == -> __eq__()
# <  -> __lt__()
# >  -> __gt__()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1 + p2)
print(p1 - p2)


# ============================================================
# 7. __eq__() -> ==
# ============================================================
# Without __eq__, equality normally compares object identity.
# By defining __eq__, we can compare object values.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.marks == other.marks


s1 = Student("Rahul", 90)
s2 = Student("Rahul", 90)
s3 = Student("Aman", 90)

print(s1 == s2)
print(s1 == s3)


# ============================================================
# 8. __lt__() -> <
# ============================================================
# Comparison operators can also be customized.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks < other.marks

    def __repr__(self):
        return f"{self.name}: {self.marks}"


students = [
    Student("Rahul", 90),
    Student("Aman", 75),
    Student("Raj", 95)
]

print(sorted(students))


# ============================================================
# 9. __bool__() -> bool(obj)
# ============================================================
# __bool__ controls whether an object is considered True or False
# in boolean contexts.

class Cart:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return bool(self.items)


empty_cart = Cart([])
full_cart = Cart(["Phone"])

print(bool(empty_cart))
print(bool(full_cart))

if full_cart:
    print("Cart contains items")


# ============================================================
# 10. __contains__() -> item in obj
# ============================================================
# __contains__ defines membership testing.

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


cart = ShoppingCart(["Phone", "Laptop", "Book"])

print("Phone" in cart)
print("Car" in cart)


# ============================================================
# 11. __getitem__() -> obj[index]
# ============================================================
# Allows an object to support indexing and key-based access.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __getitem__(self, index):
        return self.songs[index]


playlist = Playlist(["Song A", "Song B", "Song C"])

print(playlist[0])
print(playlist[1])


# ============================================================
# 12. __setitem__() -> obj[index] = value
# ============================================================
# Allows indexed assignment.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __getitem__(self, index):
        return self.songs[index]

    def __setitem__(self, index, value):
        self.songs[index] = value


playlist = Playlist(["Song A", "Song B"])

playlist[0] = "New Song"

print(playlist[0])


# ============================================================
# 13. __iter__() -> for item in obj
# ============================================================
# __iter__ makes an object iterable.

class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)


team = Team(["Rahul", "Aman", "Raj"])

for member in team:
    print(member)


# ============================================================
# 14. __call__() -> obj()
# ============================================================
# __call__ makes an object callable like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)

print(double(10))
print(double(25))


# ============================================================
# 15. __enter__() AND __exit__()
# ============================================================
# These methods implement the context manager protocol used by
# the "with" statement.
#
# with obj:
#     ...
#
# roughly uses:
#     obj.__enter__()
#     ...
#     obj.__exit__()

class Demo:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with Demo():
    print("Using resource")


# ============================================================
# 16. __slots__ (ADVANCED)
# ============================================================
# __slots__ can restrict which instance attributes exist and can
# reduce per-object memory overhead by avoiding a normal
# instance __dict__.

class User:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Rahul", 21)

print(user.name)
print(user.age)

# user.email = "x@example.com"  # AttributeError


# ============================================================
# 17. IMPORTANT: DUNDER METHODS ARE PROTOCOLS
# ============================================================
# Magic methods are better understood as Python protocols.
#
# Instead of thinking:
#
#     "Python has special random functions."
#
# Think:
#
#     "Objects participate in Python's language protocols."
#
# Examples:
#
# len(obj)       -> __len__
# str(obj)       -> __str__
# repr(obj)      -> __repr__
# obj + other    -> __add__
# obj == other   -> __eq__
# item in obj    -> __contains__
# obj[index]     -> __getitem__
# for x in obj   -> __iter__
# obj()          -> __call__
# with obj       -> __enter__/__exit__
# ============================================================


# ============================================================
# 18. ADVANCED: A PYTHONIC CUSTOM COLLECTION
# ============================================================
# Multiple protocols can be combined to make a custom object
# behave naturally like a built-in collection.

class Cart:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Cart({self.items!r})"

    def __bool__(self):
        return bool(self.items)


cart = Cart(["Phone", "Laptop", "Book"])

print(cart)
print(len(cart))
print(cart[0])
print("Laptop" in cart)

for item in cart:
    print(item)

if cart:
    print("Cart is not empty")


# ============================================================
# 19. IMPORTANT: DON'T IMPLEMENT DUNDER METHODS RANDOMLY
# ============================================================
# Dunder methods should follow the expected semantics of Python.
#
# For example:
#
# __len__ -> non-negative integer
# __bool__ -> boolean
# __repr__ -> string
# __str__ -> string
# __eq__ -> boolean or NotImplemented
#
# Following these conventions makes custom objects behave
# naturally with Python's built-in ecosystem.


# ============================================================
# 20. KEY MAGIC METHODS TO REMEMBER
# ============================================================
# OBJECT CREATION / REPRESENTATION
#     __init__
#     __new__
#     __str__
#     __repr__
#
# OPERATORS
#     __add__
#     __sub__
#     __mul__
#     __truediv__
#     __eq__
#     __lt__
#     __gt__
#
# CONTAINER BEHAVIOR
#     __len__
#     __getitem__
#     __setitem__
#     __delitem__
#     __contains__
#     __iter__
#
# OBJECT BEHAVIOR
#     __bool__
#     __call__
#
# CONTEXT MANAGERS
#     __enter__
#     __exit__
#
# ============================================================
# CORE IDEA
# ============================================================
# Magic methods allow custom objects to integrate with Python's
# syntax and built-in functions.
#
# Instead of calling:
#
#     cart.get_length()
#
# we can implement __len__ and write:
#
#     len(cart)
#
# Instead of:
#
#     p1.add(p2)
#
# we can implement __add__ and write:
#
#     p1 + p2
#
# This is the foundation of Python's operator overloading and
# object protocols.
# ============================================================