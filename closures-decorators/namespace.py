# **Namespaces in Python**, which are essentially systems that manage the naming of objects to avoid conflicts. Here is the chronological breakdown:

### 1. What is a Name? (0:44)
# In Python, a 'name' is an identifier used to refer to an object (variables, functions, classes). If you have two variables with the same value, they often point to the same memory ID.

### 2. What is a Namespace? (1:53)
# A namespace is a collection of names mapped to objects, similar to a dictionary. It ensures that names are unique and organized so the interpreter knows exactly which object you are referring to.

### 3. Global (Module-Level) Namespace (4:35)
# This is created when a module is imported or a script is executed. It contains names defined at the main level of the script.
# Example: Accessing global names
import builtins
print(globals()) # Displays all global variables/functions


### 4. Local Namespace (11:57)
# Created when a function is called and destroyed when the function returns. Names inside a function are local to that function and do not conflict with names outside.
def my_function():
    x = 10  # Local scope
    print(locals()) # Shows current local namespace

my_function()


### 5. Nested and Global Interaction (10:27)
# When functions are nested, Python searches for a name in the Local scope first, then Enclosing (non-local) scopes, followed by Global, and finally Built-in.

### 6. Using `globals()` and `locals()` (4:23, 13:13)
# These are built-in functions used to inspect the contents of the current namespace. They return a dictionary representing the current variable mappings.

