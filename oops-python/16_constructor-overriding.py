# ============================================================
# CONSTRUCTOR OVERRIDING IN INHERITANCE
# ============================================================
# If a child class does not define __init__(), it can use the
# parent's __init__() through normal method lookup.
#
# If the child defines its own __init__(), the child's version
# takes precedence.
# ============================================================


# ============================================================
# CHILD WITHOUT ITS OWN CONSTRUCTOR
# ============================================================
# Son has no __init__(), so Python searches the inheritance
# hierarchy and finds Father.__init__().
#
# Simplified lookup:
# Son.__init__() -> not found
#       ↓
# Father.__init__() -> found
# ============================================================

class Father:
    def __init__(self):
        print("Father constructor called")


class Son(Father):
    pass


s1 = Son()


# ============================================================
# CONSTRUCTOR OVERRIDING
# ============================================================
# Once Son defines __init__(), its constructor takes precedence.
#
# Father.__init__() is NOT automatically executed.

class Father:
    def __init__(self):
        print("Father owns a classic car")


class Son(Father):
    def __init__(self):
        print("Son owns a BMW")


s1 = Son()


# ============================================================
# CALLING BOTH CONSTRUCTORS WITH super()
# ============================================================
# If the child needs both parent initialization and its own
# initialization, explicitly call super().__init__().
#
# Execution order:
# Son()
#   ↓
# Son.__init__()
#   ↓
# super().__init__()
#   ↓
# Father.__init__()
#   ↓
# return to Son.__init__()
#   ↓
# child-specific initialization
# ============================================================

class Father:
    def __init__(self):
        print("Father's car")


class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son's car")


s1 = Son()


# ============================================================
# PRACTICAL EXAMPLE
# ============================================================
# The parent initializes common data.
# The child initializes additional data.
#
# super().__init__() prevents duplication of the parent's
# initialization logic.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


manager = Manager("Rahul", 80000, "Engineering")

print(manager.name)
print(manager.salary)
print(manager.department)


# ============================================================
# IMPORTANT DISTINCTION
# ============================================================
# Defining a child constructor does NOT mean the parent object
# initialization happens automatically.
#
# Child:
#     def __init__(...):
#
# must explicitly delegate to the parent when required:
#
#     super().__init__(...)
#
# Otherwise, only the child's initialization logic executes.
# ============================================================


# ============================================================
# super() IS NOT SIMPLY "THE PARENT CLASS"
# ============================================================
# super() follows Python's Method Resolution Order (MRO).
# This becomes especially important with multiple inheritance.
#
# Therefore, prefer:
#     super().method()
#
# over directly writing:
#     Parent.method(self)
#
# because super() cooperates with Python's inheritance system.
# ============================================================


class Father:
    def __init__(self):
        print("Father")


class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son")


s = Son()

print(Son.__mro__)


# ============================================================
# KEY IDEA
# ============================================================
# No child __init__:
#     Parent constructor can be inherited.
#
# Child defines __init__:
#     Child constructor overrides the inherited one.
#
# Need both:
#     super().__init__(...)
#
# Constructor overriding is therefore a special case of method
# overriding applied to object initialization.
# ============================================================