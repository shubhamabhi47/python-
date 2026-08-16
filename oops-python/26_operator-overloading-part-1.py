# ============================================================
# OPERATOR OVERLOADING
# ============================================================
# Operator overloading is a form of polymorphism where the same
# operator behaves differently depending on the objects/types
# involved.
#
# Examples:
#     10 + 20       -> numerical addition
#     "A" + "B"     -> string concatenation
#     [1] + [2]     -> list concatenation
#
# Python implements operators through special/dunder methods.
#
# +  -> __add__()
# -  -> __sub__()
# *  -> __mul__()
# /  -> __truediv__()
# // -> __floordiv__()
# %  -> __mod__()
# ** -> __pow__()
# == -> __eq__()
# != -> __ne__()
# <  -> __lt__()
# <= -> __le__()
# >  -> __gt__()
# >= -> __ge__()
# ============================================================


# ============================================================
# 1. BUILT-IN OPERATOR POLYMORPHISM
# ============================================================

print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])


# ============================================================
# 2. INTERNAL WORKING OF +
# ============================================================
# For compatible operands:
#
#     a + b
#
# conceptually invokes:
#
#     a.__add__(b)
#
# Example:

x = 10
y = 20

print(x + y)
print(x.__add__(y))
print(int.__add__(x, y))


# ============================================================
# 3. INSPECTING DUNDER METHODS
# ============================================================
# dir() shows attributes and methods available on an object/type.

print(dir(int))
print("__add__" in dir(int))
print("__sub__" in dir(int))
print("__mul__" in dir(int))


# ============================================================
# 4. STRING OPERATOR OVERLOADING
# ============================================================

s1 = "Hello "
s2 = "World"

print(s1 + s2)
print(s1.__add__(s2))
print(str.__add__(s1, s2))


# ============================================================
# 5. TYPE MISMATCH
# ============================================================
# An operation only works when the operand types support the
# requested operation.

print(10 + 20)
# print(10 + "Hello")
# TypeError


# ============================================================
# 6. CUSTOM __add__()
# ============================================================
# We can define what + means for our own class.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2

print(p3)


# ============================================================
# 7. HOW p1 + p2 WORKS
# ============================================================
# This:
#
#     p1 + p2
#
# is effectively:
#
#     p1.__add__(p2)
#
# which executes:
#
#     Point.__add__(p1, p2)

print(p1.__add__(p2))
print(Point.__add__(p1, p2))


# ============================================================
# 8. MULTIPLE OPERATORS
# ============================================================
# We can overload multiple operators for the same class.

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

    def __repr__(self):
        return f"Number({self.value})"


a = Number(20)
b = Number(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# ============================================================
# 9. COMPARISON OPERATOR OVERLOADING
# ============================================================
# Comparison operators also use dunder methods.

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

    def __repr__(self):
        return f"{self.name}({self.marks})"


s1 = Student("Rahul", 90)
s2 = Student("Aman", 80)
s3 = Student("Raj", 90)

print(s1 == s3)
print(s1 > s2)


# ============================================================
# 10. IMPORTANT: NotImplemented
# ============================================================
# When an operator method doesn't know how to handle the other
# operand type, returning NotImplemented tells Python:
#
#     "I don't support this operation for this operand."
#
# Python may then try the reflected operation on the other operand.
#
# This is better than immediately raising TypeError inside the
# dunder method.

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __repr__(self):
        return f"₹{self.amount}"


m1 = Money(500)
m2 = Money(300)

print(m1 + m2)


# ============================================================
# 11. REFLECTED OPERATORS
# ============================================================
# Python also provides reflected operator methods.
#
#     a + b -> a.__add__(b)
#     a - b -> a.__sub__(b)
#
# Reflected versions include:
#
#     __radd__
#     __rsub__
#     __rmul__
#     __rtruediv__
#
# They become important when the left operand cannot handle the
# right operand.

class Price:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Price):
            return Price(self.value + other.value)
        if isinstance(other, (int, float)):
            return Price(self.value + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return f"Price({self.value})"


price = Price(100)

print(price + 50)
print(50 + price)


# ============================================================
# 12. __radd__() WITH sum()
# ============================================================
# sum() starts with 0 by default.
#
# Therefore:
#
#     sum([objects])
#
# may initially perform:
#
#     0 + object
#
# __radd__ can make custom objects work naturally with sum().

class Amount:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Amount):
            return Amount(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __repr__(self):
        return f"Amount({self.value})"


amounts = [Amount(100), Amount(200), Amount(300)]

print(sum(amounts))


# ============================================================
# 13. UNARY OPERATOR OVERLOADING
# ============================================================
# Unary operators operate on one operand.
#
#     -obj -> __neg__()
#     +obj -> __pos__()
#     abs(obj) -> __abs__()

class Number:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return Number(-self.value)

    def __pos__(self):
        return Number(+self.value)

    def __abs__(self):
        return Number(abs(self.value))

    def __repr__(self):
        return f"Number({self.value})"


n = Number(-10)

print(-n)
print(+n)
print(abs(n))


# ============================================================
# 14. IN-PLACE OPERATORS
# ============================================================
# Operators such as += can use special methods:
#
#     += -> __iadd__()
#     -= -> __isub__()
#     *= -> __imul__()
#
# If the in-place method isn't implemented, Python can fall back
# to normal operator behavior.

class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def __repr__(self):
        return f"Counter({self.value})"


counter = Counter(10)

counter += 5

print(counter)


# ============================================================
# 15. OPERATOR OVERLOADING WITH A VECTOR
# ============================================================
# A more realistic example:
#
# Vector addition:
#
#     (x1, y1) + (x2, y2)
#       =
#     (x1+x2, y1+y2)

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
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(3 * v1)


# ============================================================
# 16. __str__ + __repr__ WITH OPERATORS
# ============================================================
# Operator overloading and object representation can be combined
# to make custom objects behave naturally.

class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

    def __str__(self):
        return f"{self.currency} {self.amount}"


m1 = Money(500)
m2 = Money(300)

print(m1 + m2)
print(repr(m1 + m2))


# ============================================================
# 17. COMMON OPERATOR -> DUNDER METHOD MAP
# ============================================================
# Arithmetic:
#
#     a + b       -> __add__
#     a - b       -> __sub__
#     a * b       -> __mul__
#     a / b       -> __truediv__
#     a // b      -> __floordiv__
#     a % b       -> __mod__
#     a ** b      -> __pow__
#
# Comparison:
#
#     a == b      -> __eq__
#     a != b      -> __ne__
#     a < b       -> __lt__
#     a <= b      -> __le__
#     a > b       -> __gt__
#     a >= b      -> __ge__
#
# Unary:
#
#     -a          -> __neg__
#     +a          -> __pos__
#     abs(a)      -> __abs__
#
# In-place:
#
#     a += b      -> __iadd__
#     a -= b      -> __isub__
#     a *= b      -> __imul__
#
# Reflected:
#
#     b + a       -> __radd__ when appropriate
#     b - a       -> __rsub__
#     b * a       -> __rmul__
#     b / a       -> __rtruediv__
# ============================================================


# ============================================================
# 18. IMPORTANT CONCEPT
# ============================================================
# Operator overloading does NOT create new operators.
#
# We are defining how EXISTING Python operators behave for our
# custom objects.
#
# Example:
#
#     p1 + p2
#
# Python already knows what "+" means.
# We are simply telling Python what "+" should mean when p1 and
# p2 are instances of our class.
# ============================================================


# ============================================================
# 19. FINAL REAL-WORLD EXAMPLE
# ============================================================
# Shopping cart totals are a good example of operator overloading.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ₹{self.price}"


class Cart:
    def __init__(self, products=None):
        self.products = products or []

    def __add__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented
        return Cart(self.products + other.products)

    def __len__(self):
        return len(self.products)

    def total(self):
        return sum(product.price for product in self.products)

    def __repr__(self):
        return f"Cart({self.products!r})"


cart1 = Cart([
    Product("Keyboard", 2000),
    Product("Mouse", 1000)
])

cart2 = Cart([
    Product("Headphones", 3000)
])

combined_cart = cart1 + cart2

print(combined_cart)
print("Items:", len(combined_cart))
print("Total:", combined_cart.total())


# ============================================================
# CORE IDEA
# ============================================================
# Operator overloading connects normal Python syntax with custom
# object behavior.
#
#     p1 + p2
#          ↓
#     __add__()
#
#     p1 == p2
#          ↓
#     __eq__()
#
#     len(p1)
#          ↓
#     __len__()
#
#     -p1
#          ↓
#     __neg__()
#
# This is one of the main reasons Python objects can behave like
# native types while still containing custom application logic.
# ============================================================