# ============================================================
# HYBRID INHERITANCE AND METHOD RESOLUTION ORDER (MRO)
# ============================================================
# HYBRID INHERITANCE:
# A combination of multiple inheritance patterns such as
# hierarchical + multiple + multilevel inheritance.
#
# MRO:
# Method Resolution Order defines the order Python follows when
# searching for methods and attributes in an inheritance hierarchy.
#
# Python uses C3 Linearization to calculate the MRO.
# ============================================================


# ============================================================
# 1. HYBRID INHERITANCE
# ============================================================
# A
# ├── B
# └── C
#     \ /
#      D
#
# B and C both inherit from A -> hierarchical inheritance.
# D inherits from B and C    -> multiple inheritance.
#
# Together they form hybrid inheritance.

class A:
    def feature(self):
        print("Feature from A")


class B(A):
    def feature(self):
        print("Feature from B")


class C(A):
    def feature(self):
        print("Feature from C")


class D(B, C):
    pass


d = D()

d.feature()


# ============================================================
# 2. MRO
# ============================================================
# Python searches D's hierarchy according to its MRO.
#
# For D(B, C), the MRO is:
#
# D -> B -> C -> A -> object
#
# Therefore d.feature() finds B.feature() first.

print(D.mro())
print(D.__mro__)


# ============================================================
# 3. MRO WITH NO OVERRIDDEN METHOD
# ============================================================
# If D and B do not define feature(), Python continues searching
# according to the MRO.

class A:
    def feature(self):
        print("Feature from A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

d.feature()

print(D.mro())


# ============================================================
# 4. DIAMOND INHERITANCE / DIAMOND PROBLEM
# ============================================================
# The structure forms a diamond:
#
#          A
#         / \
#        B   C
#         \ /
#          D
#
# B and C both inherit A, while D inherits B and C.
#
# Python's MRO ensures A is not searched repeatedly and is placed
# after B and C in the MRO.

class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

d.show()

print(D.mro())


# ============================================================
# 5. WHY A COMES AFTER B AND C
# ============================================================
# MRO for D(B, C):
#
# D -> B -> C -> A -> object
#
# Python first gives priority to the current class, then follows
# the inheritance constraints while preserving the declared
# parent order.
#
# Therefore the common ancestor A is not searched before B and C.


# ============================================================
# 6. MRO + super()
# ============================================================
# super() follows the MRO rather than simply jumping to a
# particular parent.
#
# In this hierarchy:
#
# D -> B -> C -> A -> object
#
# D.super() -> B
# B.super() -> C
# C.super() -> A

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


d = D()

d.show()

print(D.mro())


# ============================================================
# 7. C3 LINEARIZATION
# ============================================================
# Python uses C3 Linearization to construct a consistent MRO.
#
# Important properties:
#
# 1. The child appears before its parents.
# 2. Parent order is preserved.
# 3. A class appears only once in the MRO.
# 4. The resulting order remains consistent with inheritance
#    relationships.
#
# This prevents ambiguous method lookup in complex hierarchies.


# ============================================================
# 8. INCONSISTENT MRO
# ============================================================
# Python rejects inheritance structures for which a consistent
# C3 MRO cannot be created.

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A, B):
#     pass
#
# This raises TypeError because A would have conflicting ordering
# requirements in the resulting hierarchy.


# ============================================================
# KEY IDEA
# ============================================================
# HYBRID INHERITANCE:
#     Combination of multiple inheritance patterns.
#
# MRO:
#     Exact order Python uses for method/attribute lookup.
#
# Example:
#
#             A
#            / \
#           B   C
#            \ /
#             D
#
# MRO:
#     D -> B -> C -> A -> object
#
# DIAMOND PROBLEM:
#     Two parents share the same ancestor.
#
# Python solves it using C3 Linearization, ensuring a consistent
# lookup order and avoiding duplicate traversal of the common
# ancestor.
# ============================================================