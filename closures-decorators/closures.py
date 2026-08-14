# concept of **Closures in Python**. Below is the code demonstrated in chronological order:

### 1. Function as an Object (0:44)
# In Python, functions are first-class objects.
def outer_function():
    print("Hello")

print(outer_function)


### 2. Nested Functions (1:37)
# Defining a function inside another function.
def outer_function():
    def inner_function():
        print("Bye")
    # Inner function can only be accessed inside outer_function


### 3. Calling Nested Functions (2:14)
def outer_function():
    print("Hello")
    def inner_function():
        print("Bye")
    inner_function()

outer_function()


### 4. Function Aliasing (5:05)
# Creating an alias for a function name.
def outer_function():
    print("Hello")

my_alias = outer_function
my_alias()


### 5. Returning a Function (6:03)
# Returning the function object itself from an outer function.
def outer_function():
    def inner_function():
        x = 200
        return x
    return inner_function

result = outer_function()
print(result())


### 6. Closure Concept (13:00)
# A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
def outer_function():
    msg = "Hello"
    def inner_function():
        print(msg)
    return inner_function

closure_instance = outer_function()
closure_instance()  # Still remembers 'msg'
