# ============================================================
# MULTIPLE DECORATORS IN PYTHON
# ============================================================
#
# Multiple decorators can be applied to the same function.
#
# The important concept is:
#
#     The decorator closest to the function is applied FIRST.
#
# For example:
#
#     @decor1
#     @decor2
#     def get_name():
#         ...
#
# is equivalent to:
#
#     get_name = decor1(decor2(get_name))
#
# Therefore:
#
#     get_name
#         ↓
#     decor2
#         ↓
#     decor1
#
# But when the function is CALLED, the execution starts from
# the outermost decorator:
#
#     decor1 wrapper
#         ↓
#     decor2 wrapper
#         ↓
#     original function
#
# ============================================================
# 1. DEFINING THE FIRST DECORATOR
# ============================================================
#
# decor1 receives a function as an argument.
#
# Inside decor1:
#
#     func
#
# refers to the function that is being decorated.
#
# The inner() function acts as a wrapper around that function.
#
# When inner() is called:
#
#     1. The original function is executed.
#     2. Its returned value is stored in x.
#     3. x.upper() converts the string to uppercase.
#     4. The modified value is returned.
#
# ============================================================

def decor1(func):
    def inner():
        x = func()
        return x.upper()  # Converts result to uppercase

    return inner


# ============================================================
# 2. DEFINING THE SECOND DECORATOR
# ============================================================
#
# decor2 follows the same decorator pattern.
#
# It:
#
#     1. Receives a function.
#     2. Creates an inner wrapper.
#     3. Calls the original function.
#     4. Takes the returned string.
#     5. Uses split() to convert the string into a list.
#     6. Returns the list.
#
# Example:
#
#     "shantanu kumar"
#
# becomes:
#
#     ["shantanu", "kumar"]
#
# ============================================================

def decor2(func):
    def inner():
        x = func()
        return x.split()  # Splits string into a list

    return inner


# ============================================================
# 3. ORIGINAL FUNCTION
# ============================================================
#
# This is the function whose behavior we want to extend.
#
# At this point, get_name() simply returns:
#
#     "shantanu"
#
# It does not know anything about uppercase conversion or
# splitting.
#
# Those responsibilities will be added by decorators.
#
# ============================================================

def get_name():
    return "shantanu"


# ============================================================
# 4. MANUALLY APPLYING MULTIPLE DECORATORS
# ============================================================
#
# We can apply decorators without using @ syntax.
#
# The following:
#
#     result = decor1(decor2(get_name))
#
# happens in two stages.
#
# FIRST:
#
#     decor2(get_name)
#
# decor2 receives the original get_name function and returns
# its inner() function.
#
# SECOND:
#
#     decor1(result_from_decor2)
#
# decor1 receives the function returned by decor2 and wraps it
# again.
#
# Therefore the final structure becomes:
#
#     get_name
#         ↓
#     decor2
#         ↓
#     decor1
#
# ============================================================

result = decor1(decor2(get_name))

print(result())


# ============================================================
# 5. UNDERSTANDING WHAT ACTUALLY HAPPENS
# ============================================================
#
# This line:
#
#     result = decor1(decor2(get_name))
#
# can be understood from the inside out.
#
# First:
#
#     decor2(get_name)
#
# returns decor2's inner function.
#
# Conceptually:
#
#     temp = decor2(get_name)
#
# Then:
#
#     decor1(temp)
#
# returns decor1's inner function.
#
# Finally:
#
#     result = decor1(temp)
#
# So result points to decor1's wrapper.
#
# The structure is approximately:
#
#     result
#       |
#       v
#     decor1.inner
#       |
#       | calls func()
#       v
#     decor2.inner
#       |
#       | calls func()
#       v
#     original get_name
#
# ============================================================
# 6. EXECUTION ORDER
# ============================================================
#
# This is one of the most important concepts with multiple
# decorators.
#
# Consider:
#
#     @decor1
#     @decor2
#     def get_name():
#         return "shantanu"
#
# Decoration happens from BOTTOM to TOP:
#
#     get_name
#         ↓
#     decor2(get_name)
#         ↓
#     decor1(result)
#
# Therefore:
#
#     get_name = decor1(decor2(get_name))
#
#
# But when we CALL get_name(), execution happens from TOP
# to BOTTOM:
#
#     decor1.inner()
#         ↓
#     decor2.inner()
#         ↓
#     original get_name()
#
# This gives us two different things to remember:
#
#     DECORATION ORDER  → bottom to top
#     EXECUTION ORDER   → top to bottom
#
# ============================================================


# ============================================================
# 7. USING @ SYNTAX
# ============================================================
#
# The @ syntax is simply a cleaner way of writing the same
# decorator assignment.
#
# This:
#
#     @decor1
#     @decor2
#     def get_name():
#         return "shantanu"
#
# is equivalent to:
#
#     def get_name():
#         return "shantanu"
#
#     get_name = decor2(get_name)
#     get_name = decor1(get_name)
#
# Therefore the final function stored under the name
# "get_name" is the outer wrapper created by decor1.
#
# ============================================================

@decor1
@decor2
def get_name():
    return "shantanu"


print(get_name())


# ============================================================
# 8. DEEP DIVE: FOLLOW THE VALUE THROUGH EVERY LAYER
# ============================================================
#
# Original function:
#
#     get_name()
#
# returns:
#
#     "shantanu"
#
# decor2 receives that result:
#
#     x = "shantanu"
#
# Then:
#
#     x.split()
#
# produces:
#
#     ["shantanu"]
#
# decor2 therefore returns a LIST.
#
# Now decor1 receives that list as the result of:
#
#     func()
#
# But decor1 performs:
#
#     x.upper()
#
# A list does not have an upper() method.
#
# Therefore:
#
#     @decor1
#     @decor2
#
# will actually raise:
#
#     AttributeError
#
# because decor2 changes the string into a list before decor1
# tries to call upper() on it.
#
# This is a very important lesson:
#
# A decorator does not only change behavior.
# It can also change the TYPE of the returned value.
#
# ============================================================


# ============================================================
# 9. CORRECT ORDER FOR THIS PARTICULAR EXAMPLE
# ============================================================
#
# If we want:
#
#     "shantanu"
#
# to become:
#
#     "SHANTANU"
#
# and then:
#
#     ["SHANTANU"]
#
# we need uppercase conversion FIRST and splitting SECOND.
#
# Therefore:
#
#     decor1
#         ↓
#     converts string to uppercase
#         ↓
#     decor2
#         ↓
#     converts string to list
#
# The correct decorator order is:
#
#     @decor2
#     @decor1
#
# because decor1 is applied first.
#
# ============================================================

@decor2
@decor1
def get_name():
    return "shantanu"


print(get_name())


# ============================================================
# 10. WHAT HAPPENS INTERNALLY?
# ============================================================
#
# This:
#
#     @decor2
#     @decor1
#     def get_name():
#         return "shantanu"
#
# becomes:
#
#     def get_name():
#         return "shantanu"
#
#     get_name = decor1(get_name)
#     get_name = decor2(get_name)
#
# After the first assignment:
#
#     get_name
#         ↓
#     decor1.inner
#         ↓
#     original get_name
#
# After the second assignment:
#
#     get_name
#         ↓
#     decor2.inner
#         ↓
#     decor1.inner
#         ↓
#     original get_name
#
# Calling:
#
#     get_name()
#
# therefore starts at decor2.inner().
#
# ============================================================
# 11. COMPLETE EXECUTION FLOW
# ============================================================
#
# Suppose we have:
#
#     @decor2
#     @decor1
#     def get_name():
#         return "shantanu"
#
# Calling get_name() causes:
#
#     get_name()
#         |
#         v
#     decor2.inner()
#         |
#         | x = func()
#         v
#     decor1.inner()
#         |
#         | x = func()
#         v
#     original get_name()
#         |
#         v
#     "shantanu"
#
# Then execution returns upward:
#
#     original get_name()
#         |
#         v
#     "shantanu"
#         |
#         v
#     decor1.inner()
#         |
#         | x.upper()
#         v
#     "SHANTANU"
#         |
#         v
#     decor2.inner()
#         |
#         | x.split()
#         v
#     ["SHANTANU"]
#
# Final result:
#
#     ["SHANTANU"]
#
# ============================================================
# 12. DECORATORS FORM A CHAIN
# ============================================================
#
# Multiple decorators can be visualized as a chain of
# functions.
#
#     original function
#            |
#            v
#     decorator 1
#            |
#            v
#     decorator 2
#            |
#            v
#     decorator 3
#            |
#            v
#     final function
#
# Each decorator receives the function produced by the
# previous layer.
#
# This is why decorators are often described as "wrappers".
#
# One function wraps another function, which may itself be
# wrapping another function.
#
# ============================================================
# 13. DECORATORS CAN CHANGE RETURN TYPES
# ============================================================
#
# A decorator is allowed to return anything.
#
# For example, a function might originally return:
#
#     string
#
# A decorator could change it into:
#
#     list
#
# Another decorator could change it into:
#
#     dictionary
#
# Another could change it into:
#
#     integer
#
# Therefore, when stacking decorators, you must understand
# what type each decorator produces.
#
# Example:
#
#     string
#        ↓
#     uppercase decorator
#        ↓
#     string
#        ↓
#     split decorator
#        ↓
#     list
#
# If the next decorator expects a string but receives a list,
# an error can occur.
#
# ============================================================
# 14. DECORATORS MUST AGREE ON THEIR INPUT AND OUTPUT
# ============================================================
#
# Think of every decorator as a processing stage.
#
#     INPUT → DECORATOR → OUTPUT
#
# For decorators to work correctly together:
#
#     output of decorator A
#
# must be compatible with:
#
#     input expected by decorator B
#
# This is similar to a pipeline.
#
# Example:
#
#     string
#       ↓
#     uppercase
#       ↓
#     string
#       ↓
#     split
#       ↓
#     list
#
# This works.
#
# But:
#
#     string
#       ↓
#     split
#       ↓
#     list
#       ↓
#     uppercase
#
# does NOT work because list does not provide .upper().
#
# ============================================================
# 15. IMPORTANT: DECORATORS ARE NOT ONLY FOR RETURN VALUES
# ============================================================
#
# A decorator can add behavior:
#
#     BEFORE the function
#     AFTER the function
#     AROUND the function
#
# Common uses include:
#
#     - Logging
#     - Authentication
#     - Authorization
#     - Timing functions
#     - Caching
#     - Validation
#     - Error handling
#     - Debugging
#     - Transaction management
#     - Rate limiting
#
# For example:
#
#     @login_required
#     @log_function
#     @timer
#     def process_data():
#         ...
#
# Each decorator adds a separate responsibility.
#
# ============================================================
# 16. IMPORTANT ADVANCED PROBLEM: FUNCTIONS WITH ARGUMENTS
# ============================================================
#
# So far our decorators use:
#
#     def inner():
#
# This only works for functions that take NO arguments.
#
# If we have:
#
#     def addition(a, b):
#         return a + b
#
# then a decorator with:
#
#     def inner():
#
# cannot directly accept those arguments.
#
# The general solution is:
#
#     *args
#     **kwargs
#
# This allows a decorator to work with functions having
# different numbers and types of arguments.
#
# ============================================================

def decorator(func):
    def inner(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result

    return inner


@decorator
def addition(a, b):
    return a + b


print(addition(10, 20))


# ============================================================
# 17. WHY *args AND **kwargs ARE IMPORTANT
# ============================================================
#
# *args collects positional arguments.
#
# Example:
#
#     addition(10, 20)
#
# becomes conceptually:
#
#     args = (10, 20)
#
# **kwargs collects keyword arguments.
#
# Example:
#
#     person(name="John", age=25)
#
# becomes conceptually:
#
#     kwargs = {
#         "name": "John",
#         "age": 25
#     }
#
# Then:
#
#     func(*args, **kwargs)
#
# forwards those arguments to the original function.
#
# This makes the decorator flexible.
#
# ============================================================
# 18. ADVANCED: functools.wraps
# ============================================================
#
# There is another important issue with decorators.
#
# After decorating a function, the function's metadata can
# appear to belong to the wrapper instead of the original
# function.
#
# For example, Python functions have attributes such as:
#
#     __name__
#     __doc__
#
# Without additional handling, a decorated function may have
# the wrapper's metadata.
#
# Python provides:
#
#     functools.wraps
#
# to preserve important metadata from the original function.
#
# ============================================================

from functools import wraps


def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Before function")

        result = func(*args, **kwargs)

        print("After function")

        return result

    return inner


@decorator
def addition(a, b):
    """Add two numbers."""
    return a + b


print(addition(10, 20))

# Because of @wraps(func), metadata such as the function name
# and documentation is preserved.
#
# This is considered best practice when writing reusable
# decorators.
#
# ============================================================
# 19. DECORATORS CAN WRAP OTHER DECORATORS
# ============================================================
#
# A decorator is just a function.
#
# Therefore decorators can themselves be decorated.
#
# This is an advanced concept and becomes useful when building
# reusable frameworks and libraries.
#
# The important thing is to remember:
#
#     @something
#
# always means that something is being used as a decorator
# for the object immediately below it.
#
# ============================================================
# 20. DECORATORS ARE EXECUTED WHEN THE FUNCTION IS DEFINED
# ============================================================
#
# This is another important distinction.
#
# Consider:
#
#     @decorator
#     def hello():
#         print("Hello")
#
# The decorator is applied when Python reaches the function
# definition.
#
# It does NOT wait until:
#
#     hello()
#
# is called.
#
# The wrapping happens first.
#
# Later, when hello() is called, the already-wrapped function
# is executed.
#
# Therefore:
#
#     DECORATION → happens when definition is executed
#
#     FUNCTION CALL → happens when () is used
#
# These are two separate events.
#
# ============================================================
# 21. THE MOST IMPORTANT FORMULA
# ============================================================
#
# For:
#
#     @decor1
#     @decor2
#     @decor3
#     def function():
#         pass
#
# the internal equivalent is:
#
#     function = decor1(
#                    decor2(
#                        decor3(function)
#                    )
#                )
#
# Or step by step:
#
#     function = decor3(function)
#     function = decor2(function)
#     function = decor1(function)
#
# Therefore:
#
#     APPLICATION → bottom to top
#
#     EXECUTION → top to bottom
#
# ============================================================
# 22. FINAL MENTAL MODEL
# ============================================================
#
# Whenever you see:
#
#     @A
#     @B
#     def function():
#         ...
#
# immediately translate it in your head to:
#
#     function = A(B(function))
#
# Then ask two questions:
#
#     1. What does B return?
#     2. Can A work with what B returns?
#
# This will help you understand both the execution order and
# possible errors.
#
# For the example:
#
#     @decor2
#     @decor1
#     def get_name():
#         return "shantanu"
#
# think:
#
#     get_name = decor2(decor1(get_name))
#
# Therefore:
#
#     original get_name
#         ↓
#     decor1 → "SHANTANU"
#         ↓
#     decor2 → ["SHANTANU"]
#
# Final output:
#
#     ["SHANTANU"]
#
# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. A decorator is a callable that receives another callable
#    and usually returns a new callable.
#
# 2. @decorator is syntactic sugar for:
#
#       function = decorator(function)
#
# 3. With multiple decorators:
#
#       @A
#       @B
#       def function():
#           ...
#
#    becomes:
#
#       function = A(B(function))
#
# 4. Decorators are applied from bottom to top.
#
# 5. When the final function is called, execution starts from
#    the outermost decorator.
#
# 6. Decorators commonly use closures to remember the original
#    function.
#
# 7. A decorator can change the return value or return type.
#
# 8. The output of one decorator must be compatible with the
#    next decorator in the chain.
#
# 9. Use *args and **kwargs when writing general-purpose
#    decorators.
#
# 10. Use functools.wraps to preserve the original function's
#     metadata.
#
# 11. Decorators are applied when the function definition is
#     executed, not when the function is eventually called.
#
# 12. The most important formula to remember is:
#
#       @A
#       @B
#       def f():
#           ...
#
#       f = A(B(f))
#
# ============================================================
