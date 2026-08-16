# ============================================================
# OPERATOR OVERLOADING: __add__(), OBJECT RETURN & __str__()
# ============================================================
# Operator overloading allows a class to define how operators
# behave with its objects.
#
# For:
#     a + b
#
# Python looks for:
#     a.__add__(b)
#
# __add__() can return any meaningful result, including another
# object of the same class.
# ============================================================


# ============================================================
# 1. BASIC __add__()
# ============================================================
# Here __add__() returns an integer containing the total pages.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(200)

print(b1 + b2)
# b1 + b2 -> b1.__add__(b2) -> 300


# ============================================================
# 2. RETURNING A NEW OBJECT
# ============================================================
# Returning an integer works for one addition, but:
#
#     b1 + b2 + b3
#
# becomes:
#
#     (b1 + b2) + b3
#
# Therefore the first operation must return an object that can
# participate in another + operation.
#
# Returning Book(...) makes chaining possible.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)

result = b1 + b2 + b3

print(result.pages)


# ============================================================
# 3. HOW CHAINING ACTUALLY WORKS
# ============================================================
# This:
#
#     b1 + b2 + b3
#
# is evaluated as:
#
#     (b1 + b2) + b3
#
# Step 1:
#     b1 + b2
#     -> Book(300)
#
# Step 2:
#     Book(300) + b3
#     -> Book(600)

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)

step1 = b1 + b2
step2 = step1 + b3

print(step1.pages)
print(step2.pages)


# ============================================================
# 4. __str__(): HUMAN-READABLE OBJECT REPRESENTATION
# ============================================================
# __str__() controls what print(object) displays.
#
# Without __str__(), print(book) normally shows a default
# representation containing the object's type and identity.
#
# __str__() must return a string.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"Total pages: {self.pages}"


b1 = Book(100)
b2 = Book(200)

print(b1 + b2)


# ============================================================
# 5. COMPLETE CHAINING EXAMPLE
# ============================================================
# Every + returns another Book object, so any number of books
# can be chained.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"Total pages: {self.pages}"


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
b4 = Book(400)

final = b1 + b2 + b3 + b4

print(final)


# ============================================================
# 6. __add__() SHOULD HANDLE INVALID OPERANDS
# ============================================================
# A robust implementation should not blindly assume that
# 'other' is always a Book.
#
# Returning NotImplemented tells Python that this operation is
# not supported for the given operand type.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"Book({self.pages} pages)"


b1 = Book(100)
b2 = Book(200)

print(b1 + b2)

# print(b1 + 50)  # TypeError


# ============================================================
# 7. ADDING BOOK + INTEGER
# ============================================================
# We can intentionally support:
#
#     Book + int
#
# while still returning a Book object.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.pages + other.pages)
        if isinstance(other, int):
            return Book(self.pages + other)
        return NotImplemented

    def __str__(self):
        return f"Total pages: {self.pages}"


book = Book(100)

print(book + Book(200))
print(book + 50)


# ============================================================
# 8. REFLECTED ADDITION: __radd__()
# ============================================================
# The previous example supports:
#
#     Book + int
#
# but not necessarily:
#
#     int + Book
#
# __radd__() handles the reflected operation.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.pages + other.pages)
        if isinstance(other, int):
            return Book(self.pages + other)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return f"Total pages: {self.pages}"


book = Book(100)

print(book + 50)
print(50 + book)


# ============================================================
# 9. ADVANCED: SUM() WITH CUSTOM OBJECTS
# ============================================================
# Python's sum() starts with 0 by default:
#
#     sum([book1, book2])
#
# effectively begins with:
#
#     0 + book1
#
# Therefore __radd__() can be used to make custom objects work
# naturally with sum().

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.pages + other.pages)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __str__(self):
        return f"Total pages: {self.pages}"


books = [Book(100), Book(200), Book(300)]

total = sum(books)

print(total)


# ============================================================
# 10. __repr__() VS __str__()
# ============================================================
# __str__() -> user-friendly representation.
# __repr__() -> developer/debug representation.
#
# A good __repr__() should ideally make the object state clear.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Total pages: {self.pages}"

    def __repr__(self):
        return f"Book(pages={self.pages!r})"


book = Book(500)

print(book)
print(repr(book))


# ============================================================
# 11. ADVANCED: IMMUTABLE-STYLE OPERATION
# ============================================================
# __add__() should generally avoid modifying self or other.
#
# Instead:
#
#     result = a + b
#
# creates a new object while a and b remain unchanged.
#
# This makes chained operations predictable.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"Book({self.pages} pages)"


b1 = Book(100)
b2 = Book(200)

result = b1 + b2

print(b1)
print(b2)
print(result)


# ============================================================
# 12. OPERATOR OVERLOADING IS METHOD DISPATCH
# ============================================================
# These expressions are conceptually connected:
#
#     b1 + b2
#     b1.__add__(b2)
#
#     print(b1)
#     b1.__str__()
#
# Python operators are syntax that trigger special methods.
#
# This is why operator overloading is sometimes called
# "protocol-based behavior".
# ============================================================


# ============================================================
# 13. OTHER COMMON OPERATOR METHODS
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
# Comparisons:
#     ==     __eq__
#     !=     __ne__
#     <      __lt__
#     <=     __le__
#     >      __gt__
#     >=     __ge__
#
# Representation:
#     str()  __str__
#     repr() __repr__
#
# Other useful protocols:
#     len()  __len__
#     bool() __bool__
#     obj[x] __getitem__
#     x in obj __contains__
# ============================================================


# ============================================================
# FINAL CONCEPT
# ============================================================
# For:
#
#     b1 + b2 + b3
#
# Python evaluates:
#
#     (b1 + b2) + b3
#
# Therefore:
#
#     __add__() -> must return an object compatible with the next
#                  operation if chaining is required.
#
# Returning:
#     integer -> one addition is possible, but chaining with Book
#                objects stops.
#
# Returning:
#     Book    -> chaining remains possible.
#
# BEST PRACTICE:
#     • Return a meaningful result.
#     • Return a new object when appropriate.
#     • Validate operand types.
#     • Return NotImplemented for unsupported types.
#     • Use __str__() for readable output.
#     • Use __repr__() for debugging/development representation.
# ============================================================