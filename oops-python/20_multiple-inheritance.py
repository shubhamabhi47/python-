# ============================================================
# MULTIPLE INHERITANCE
# ============================================================
# Multiple inheritance occurs when one child class inherits from
# more than one parent class.
#
# class Child(Parent1, Parent2):
#
# Python uses MRO (Method Resolution Order) to determine the order
# in which classes are searched for attributes and methods.
#
# MRO generally follows the order declared in the inheritance list
# while also maintaining Python's C3 linearization rules.
# ============================================================


# ============================================================
# 1. BASIC MULTIPLE INHERITANCE
# ============================================================
# District inherits from both State and Country.
#
# MRO:
# District -> State -> Country -> object
#
# Therefore State has higher lookup priority than Country.

class Country:
    def __init__(self):
        self.office = "Delhi"


class State:
    def __init__(self):
        self.office = "Mumbai"


class District(State, Country):
    pass


d = District()

print(d.office)  # Mumbai


# ============================================================
# 2. CHECKING THE MRO
# ============================================================
# __mro__ shows the exact method/attribute lookup order.

print(District.__mro__)


# ============================================================
# 3. CONSTRUCTOR PRIORITY
# ============================================================
# Since District does not define __init__(), Python searches its
# MRO and finds State.__init__() first.
#
# Country.__init__() is not automatically called afterward.

class Country:
    def __init__(self):
        print("Country Constructor")
        self.office = "Delhi"


class State:
    def __init__(self):
        print("State Constructor")
        self.office = "Mumbai"


class District(State, Country):
    pass


d = District()

print(d.office)


# ============================================================
# 4. COOPERATIVE MULTIPLE INHERITANCE WITH super()
# ============================================================
# super() does NOT simply mean "call the parent".
#
# It continues method lookup from the next class in the MRO.
#
# MRO:
# District -> State -> Country -> object
#
# District.super() -> State
# State.super()    -> Country
#
# This allows every class to participate in initialization.

class Country:
    def __init__(self):
        print("Country Constructor")
        self.office = "Delhi"


class State:
    def __init__(self):
        print("State Constructor")
        self.office = "Mumbai"
        super().__init__()


class District(State, Country):
    def __init__(self):
        print("District Constructor")
        super().__init__()
        self.office = "Pune"


d = District()

print(d.office)


# ============================================================
# 5. EXECUTION FLOW
# ============================================================
# Creating District():
#
# District.__init__()
#       ↓
# super() -> State.__init__()
#       ↓
# super() -> Country.__init__()
#       ↓
# Country finishes
#       ↓
# State finishes
#       ↓
# District continues
#       ↓
# self.office = "Pune"
#
# Final value:
# d.office == "Pune"
# ============================================================


# ============================================================
# 6. WHY super() IS IMPORTANT
# ============================================================
# Without cooperative super(), calling only one parent constructor
# can prevent another parent from being initialized.
#
# With super(), each class delegates to the next class in the MRO.
#
# This pattern is called cooperative multiple inheritance.
# ============================================================


# ============================================================
# 7. METHODS ALSO FOLLOW MRO
# ============================================================
# MRO applies to normal methods as well as constructors.

class Country:
    def show(self):
        print("Country")


class State:
    def show(self):
        print("State")


class District(State, Country):
    pass


d = District()

d.show()  # State


# ============================================================
# 8. METHOD OVERRIDING + super()
# ============================================================
# A child can extend behavior while allowing the MRO chain to
# continue.

class Country:
    def show(self):
        print("Country")
        super().show()


class State:
    def show(self):
        print("State")
        super().show()


class Base:
    def show(self):
        print("Base")


class District(State, Country, Base):
    def show(self):
        print("District")
        super().show()


d = District()
d.show()

print(District.__mro__)


# ============================================================
# KEY IDEA
# ============================================================
# Multiple inheritance:
#
#             Parent A   Parent B
#                  \       /
#                   \     /
#                    Child
#
# Python determines lookup using MRO.
#
# class Child(A, B):
#     A has priority over B for normal lookup.
#
# super():
#     Moves to the NEXT class in the MRO.
#
# Cooperative multiple inheritance:
#     Each class calls super() so the complete MRO chain can
#     participate instead of one parent stopping the chain.
#
# Important:
# super() should be understood as "next in MRO", not simply
# "my parent".
# ============================================================