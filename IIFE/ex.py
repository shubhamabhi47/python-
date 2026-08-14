# **IIFE (Immediately Invoked Function Expression)**. While primarily a JavaScript feature, the video demonstrates how to simulate this behavior in **Python** using **lambda expressions**.

### 1. The IIFE Concept in JavaScript (0:00 - 1:36)
# In *JavaScript*, an IIFE is a function that is defined and executed simultaneously. The syntax uses parentheses to surround the function definition, immediately followed by another set of parentheses to invoke it.

# **Example logic:**
# (function(a, b) {
#     console.log(a + b);
# })(5, 7);   #Output: 12


### 2. Why Standard Python Functions Don't Support IIFE (1:36 - 2:28)
# Attempting the same syntax with a standard Python `def` function results in a `SyntaxError` because Python does not allow wrapping a function definition in parentheses to treat it as an expression.

# **Incorrect approach:**
# This will raise a SyntaxError
# (def addition(a, b):
#     return a + b)(5, 7)


### 3. Implementing IIFE in Python using Lambda (2:28 - 4:09)
# To achieve IIFE behavior in *Python*, you can wrap a **lambda function** in parentheses. Since lambda expressions in Python are already expressions, they can be invoked immediately.

# **Correct approach:**
# Syntax: (lambda parameters: expression)(arguments)
result = (lambda a, b: a + b)(3, 4)
print(result) # Output: 7


### 4. Practical Example: Handling User Input (4:09 - 4:50)
# This shows how to apply the IIFE pattern to perform an operation on input values immediately.
# Using IIFE to increment a number provided by the user
output = (lambda num: num + 1)(int(input("Enter the number: ")))
print(output)


### 5. Conclusion on Usage (4:50 - 5:26)
# While *Python* has many built-in features that make IIFEs largely unnecessary compared to *JavaScript*, this technique is useful if you specifically need a function to execute exactly **one time** and then discard it.

