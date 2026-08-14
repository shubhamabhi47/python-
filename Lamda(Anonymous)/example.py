add = lambda x, y: (x + y , x - y)

addition , subtraction = add(3, 4)
print(addition)
print(subtraction)

# print(add(3, 4))

# Incrementing a number: Adds 1 to the input.
increment = lambda x: x + 1

# Finding the power of a number: Calculates the square (or any power) of the input.
square = lambda x: x ** 2

# Converting string to uppercase: Transforms a given string to all capital letters.
to_upper = lambda s: s.upper()

# Converting Celsius to Fahrenheit: Uses the conversion formula 
to_fahrenheit = lambda c: (c * 9/5) + 32