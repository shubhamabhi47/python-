# TOPIC: Operator Overloading
# Operator overloading allows user-defined objects to work with
# operators such as +, -, *, ==, <, etc.
# Python maps operators to special (dunder) methods.
#
# +  -> __add__()
# -  -> __sub__()
# *  -> __mul__()
# == -> __eq__()
#
# When Python evaluates:
# b1 + b2
#
# it effectively calls:
# b1.__add__(b2)
#
# self  -> left-hand operand
# other -> right-hand operand

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        # Defines what + means between two Book objects.
        return self.pages + other.pages

b1 = Book("Python", 100)
b2 = Book("Java", 200)
print(b1 + b2)  # 300

# ADVANCED: Returning an Object from __add__()
# __add__() does not have to return a number.
# It can return another object.
#
# This allows chained operations:
# b1 + b2 + b3
#
# Python evaluates this as:
# (b1 + b2) + b3
#
# Therefore, if b1 + b2 returns a Book object,
# that returned object can participate in another + operation.

class BookCollection:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, BookCollection):
            return NotImplemented
        return BookCollection(
            f"{self.title} + {other.title}",
            self.pages + other.pages
        )

    def __str__(self):
        return f"{self.title}: {self.pages} pages"

b1 = BookCollection("Python", 100)
b2 = BookCollection("Java", 200)
b3 = BookCollection("C++", 300)

total = b1 + b2 + b3
print(total)  # Python + Java + C++: 600 pages

# TOPIC: Type Safety
# "other" is not automatically guaranteed to be the same type.
# Returning NotImplemented tells Python that this operand type
# is not supported instead of blindly accessing its attributes.
#
# This is better than:
# return self.pages + other.pages
#
# because other might not have a "pages" attribute.

class SafeBook:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, SafeBook):
            return NotImplemented
        return SafeBook(
            f"{self.title} + {other.title}",
            self.pages + other.pages
        )

    def __str__(self):
        return f"{self.title}: {self.pages} pages"

b1 = SafeBook("Python", 100)
b2 = SafeBook("Java", 200)
print(b1 + b2)

# TOPIC: Other Arithmetic Operators
# Operator overloading is not limited to +.
#
# -  -> __sub__()
# *  -> __mul__()
# /  -> __truediv__()
# // -> __floordiv__()
# %  -> __mod__()
# ** -> __pow__()
#
# Example:
# a - b -> a.__sub__(b)
# a * b -> a.__mul__(b)

class BookMath:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, BookMath):
            return NotImplemented
        return self.pages + other.pages

    def __sub__(self, other):
        if not isinstance(other, BookMath):
            return NotImplemented
        return self.pages - other.pages

    def __mul__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        return self.pages * value

b1 = BookMath(500)
b2 = BookMath(200)

print(b1 + b2)  # 700
print(b1 - b2)  # 300
print(b1 * 2)   # 1000

# TOPIC: Meaningful Operator Overloading
# Operator overloading should represent a logical operation.
# Python allows us to overload an operator, but we should only
# do so when its meaning is intuitive for the class.
#
# For example, adding two books could logically mean:
# - total pages
# - combined price
# - a new collection
#
# The chosen behavior should make sense to someone reading the code.

class BookDetails:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def __add__(self, other):
        if not isinstance(other, BookDetails):
            return NotImplemented
        return BookDetails(
            f"{self.title} + {other.title}",
            self.pages + other.pages,
            self.price + other.price
        )

    def __str__(self):
        return f"{self.title} | {self.pages} pages | ₹{self.price}"

b1 = BookDetails("Python", 100, 500)
b2 = BookDetails("Java", 200, 700)

total = b1 + b2
print(total)

# ADVANCED: Reflected Operators
# Binary operators also have reflected methods.
#
# +  -> __add__() / __radd__()
# -  -> __sub__() / __rsub__()
# *  -> __mul__() / __rmul__()
#
# For:
# a + b
#
# Python first tries:
# a.__add__(b)
#
# If the operation is unsupported and returns NotImplemented,
# Python can try:
# b.__radd__(a)
#
# This is useful when supporting:
# number + custom_object

class PageCount:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if isinstance(other, PageCount):
            return self.pages + other.pages
        if isinstance(other, int):
            return self.pages + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.pages
        return NotImplemented

book = PageCount(100)

print(book + 50)  # 150
print(50 + book)  # 150

# KEY TAKEAWAYS
# 1. Operator overloading allows custom objects to work with operators.
# 2. Operators are implemented using special/dunder methods.
# 3. a + b normally invokes a.__add__(b).
# 4. self represents the left operand.
# 5. other represents the right operand.
# 6. __add__() can return a number, string, object, or another value.
# 7. Returning a new object allows chained operations.
# 8. Return NotImplemented for unsupported operand types.
# 9. Reflected methods such as __radd__() support reversed operands.
# 10. Operator overloading should have a meaningful and intuitive purpose.

# ============================================================
# OPERATOR OVERLOADING
# ============================================================
# Operator overloading allows user-defined objects to work with
# built-in operators such as +, -, *, ==, <, >, etc.
#
# Python implements operators through SPECIAL METHODS (dunder
# methods).
#
# Examples:
#     +   -> __add__()
#     -   -> __sub__()
#     *   -> __mul__()
#     ==  -> __eq__()
#     <   -> __lt__()
#     >   -> __gt__()
#     len -> __len__()
#     str -> __str__()
#
# When Python evaluates:
#
#     a + b
#
# it essentially looks for:
#
#     a.__add__(b)
# ============================================================


# ============================================================
# 1. WITHOUT OPERATOR OVERLOADING
# ============================================================
# User-defined objects do not automatically know what + should
# mean for them.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


b1 = Book("Python", 100)
b2 = Book("Java", 200)

# print(b1 + b2)  # TypeError


# ============================================================
# 2. OVERLOADING +
# ============================================================
# __add__(self, other):
#
# self   -> left-hand object
# other  -> right-hand object
#
# b1 + b2
#    ↓
# b1.__add__(b2)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book("Python", 100)
b2 = Book("Java", 200)

print(b1 + b2)
print(b1.__add__(b2))


# ============================================================
# 3. TYPE CHECKING INSIDE __add__
# ============================================================
# A robust implementation should decide what types it supports.
#
# Returning NotImplemented is preferred when the other operand is
# unsupported because Python can then try the reflected operation
# or raise an appropriate TypeError.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages


b1 = Book("Python", 100)

print(b1 + Book("Java", 200))

# print(b1 + 50)  # TypeError


# ============================================================
# 4. RETURNING A NEW OBJECT
# ============================================================
# __add__ does not have to return a number.
#
# It can return another object.
#
# This is important when supporting chained operations:
#
#     b1 + b2 + b3
#
# Evaluation happens from left to right:
#
#     (b1 + b2) + b3
#
# Therefore b1 + b2 must return an object that can again be
# used with +.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return Book(f"{self.title} + {other.title}",
                    self.pages + other.pages)

    def __str__(self):
        return f"{self.title}: {self.pages} pages"


b1 = Book("Python", 100)
b2 = Book("Java", 200)
b3 = Book("C++", 300)

total = b1 + b2 + b3

print(total)
print(total.pages)


# ============================================================
# 5. MULTIPLE OPERATORS
# ============================================================
# Different operators map to different special methods.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __str__(self):
        return str(self.value)


a = Number(20)
b = Number(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# ============================================================
# 6. COMPARISON OPERATOR OVERLOADING
# ============================================================
# Comparison operators are also implemented through special
# methods.
#
# == -> __eq__()
# != -> __ne__()
# <  -> __lt__()
# <= -> __le__()
# >  -> __gt__()
# >= -> __ge__()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks == other.marks

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks < other.marks


s1 = Student("Rahul", 90)
s2 = Student("Aman", 85)
s3 = Student("Raj", 90)

print(s1 == s3)
print(s1 == s2)
print(s2 < s1)


# ============================================================
# 7. __str__() AND __repr__()
# ============================================================
# These are also special methods.
#
# __str__  -> human-readable representation
# __repr__ -> developer/debug representation
#
# print(obj) normally uses __str__().
# repr(obj) explicitly uses __repr__().

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book({self.title!r}, {self.pages!r})"


book = Book("Python", 500)

print(book)
print(str(book))
print(repr(book))


# ============================================================
# 8. __len__()
# ============================================================
# len(obj) internally calls obj.__len__().

class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)


library = Library(["Python", "Java", "C++"])

print(len(library))
print(library.__len__())


# ============================================================
# 9. REFLECTED OPERATORS
# ============================================================
# Python also provides reflected operator methods.
#
#     __add__  -> a + b
#     __radd__ -> b + a when the left operand cannot handle it
#
# This is especially useful when supporting operations involving
# different types.

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        if isinstance(other, (int, float)):
            return Money(self.amount + other)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return f"₹{self.amount}"


money = Money(500)

print(money + 100)
print(100 + money)


# ============================================================
# 10. IN-PLACE OPERATORS
# ============================================================
# Operators such as += can use special methods like:
#
# += -> __iadd__()
# -= -> __isub__()
# *= -> __imul__()
#
# If __iadd__() is not implemented, Python can fall back to
# __add__() and assignment.

class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        self.value += amount
        return self


counter = Counter(10)

counter += 5

print(counter.value)


# ============================================================
# 11. ADVANCED: VECTOR OPERATOR OVERLOADING
# ============================================================
# Operator overloading becomes particularly useful when an
# object's natural mathematical meaning is clear.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(3 * v1)


# ============================================================
# 12. IMPORTANT: OPERATOR OVERLOADING DOES NOT CHANGE PYTHON'S
#     OPERATORS
# ============================================================
# We are not modifying the + operator globally.
#
# We are defining how + behaves FOR OUR CLASS.
#
# int:
#     5 + 3
#
# Book:
#     book1 + book2
#
# Python dispatches the operation according to the operand types.


# ============================================================
# 13. OPERATOR OVERLOADING WITH IMMUTABLE-STYLE OBJECTS
# ============================================================
# A good design is often to return a NEW object instead of
# modifying the existing operands.
#
# This makes:
#
#     c = a + b
#
# conceptually similar to operations on built-in numbers.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(10, 20)
p2 = Point(5, 7)

p3 = p1 + p2

print(p1)
print(p2)
print(p3)


# ============================================================
# IMPORTANT DUNDER METHODS
# ============================================================
# Arithmetic:
#     +      __add__
#     -      __sub__
#     *      __mul__
#     /      __truediv__
#     //     __floordiv__
#     %      __mod__
#     **     __pow__
#
# Comparison:
#     ==     __eq__
#     !=     __ne__
#     <      __lt__
#     <=     __le__
#     >      __gt__
#     >=     __ge__
#
# Object behavior:
#     str()  __str__
#     repr() __repr__
#     len()  __len__
#     bool() __bool__
#
# Container behavior:
#     obj[x]       __getitem__
#     obj[x] = y   __setitem__
#     del obj[x]   __delitem__
#     x in obj     __contains__
#
# Construction:
#     __new__
#     __init__
#
# Context manager:
#     __enter__
#     __exit__
# ============================================================


# ============================================================
# FINAL CONCEPT
# ============================================================
# Operator overloading connects Python's operators with the
# special methods defined by your class.
#
# Example:
#
#     a + b
#       ↓
#     a.__add__(b)
#
# For:
#
#     a + b + c
#
# Python evaluates:
#
#     (a + b) + c
#
# Therefore the return value of __add__() determines whether
# further chaining is possible.
#
# BEST PRACTICE:
#     • Validate operand types.
#     • Return NotImplemented for unsupported types.
#     • Return a meaningful result type.
#     • Keep operator behavior intuitive.
#     • Avoid overloading operators in surprising ways.
# ============================================================