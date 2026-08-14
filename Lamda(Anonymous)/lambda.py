### 1. Traditional If-Else Statement (0:30)
# Used to compare two variables and print the larger one.
num1 = 10
num2 = 20
if num1 >= num2:
    print(num1)
else:
    print(num2)


### 2. Short-hand If-Else (1:17)
# A concise, one-line way to write conditional logic.
num1 = 10
num2 = 20
# Syntax: value_if_true if condition else value_if_false
print(num1 if num1 >= num2 else num2)


### 3. Lambda Function with If-Else (2:41)
# Applying the short-hand logic inside an anonymous (lambda) function.
num1 = 37
num2 = 19
# Lambda function assigned to an alias
max_val = lambda n1, n2: n1 if n1 >= n2 else n2
print(max_val(num1, num2))


### 4. Lambda Function with List Comprehension (5:13)
# Using a lambda to process a list and transform elements using list comprehension.
nums = [3, 5, 6, 7]
# Lambda function that returns a new list of squares
squares = lambda data: [i * i for i in data]
print(squares(nums))
