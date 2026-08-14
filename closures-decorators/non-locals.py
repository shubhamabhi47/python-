# explains variable scopes in Python using the **LEGB rule**. Here are the code examples for each concept in chronological order:

# 1. **Local Variables** (0:33):
# Defined inside a function, these variables are only accessible within that function's scope.
def my_func():
    x = 10
    print(x)
my_func()


# 2. **Global Variables** (1:23):
# Declared outside any function, these can be accessed throughout the module, but cannot be modified inside a function without the `global` keyword.
x = 20
def my_func():
    print(x)
my_func()


# 3. **Updating Global Variables** (2:35):
# To modify a global variable from inside a function, you must use the `global` keyword.
x = 10
def my_func():
    global x
    x = x + 5
    print(x)
my_func()


# 4. **Enclosing (Nonlocal) Variables** (4:37):
# When you have a function inside another function, the inner function can access variables from the outer (enclosing) scope. To modify them, use `nonlocal`.
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)
outer()


# 5. **Built-in Scope** (3:11):
# The final layer of the LEGB rule, which includes Python's built-in functions like `print()` or `len()`.