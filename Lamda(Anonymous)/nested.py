### 1. Using Normal Functions 
# This approach uses the standard `def` keyword for both the outer and inner functions.
def outer():
    def add(num1, num2):
        return num1 + num2
    return add

result = outer()(3, 4)
print(result) # Output: 7


### 2. Using Normal Function and Lambda
# The inner function is replaced with a `lambda` expression.
def outer():
    add = lambda num1, num2: num1 + num2
    return add

result = outer()(3, 4)
print(result) # Output: 7


### 3. Using Lambda and Lambda 
# Both the outer and inner functions are written using `lambda` expressions, creating a fully nested lambda structure.
outer = lambda: lambda num1, num2: num1 + num2

result = outer()(3, 4)
print(result) # Output: 7
