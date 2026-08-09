# in first class function function is working as an instance of an object so we can store the function as a variable and
# it can be passed as a parameter or argument to another function
# we can return a function from another function
# we can store the this type of function in different data structure like list, hash tables ,
from prog1 import uppercase

# definee a function shout
def fun():
    print("passing arguments.")

def shout(s):
     s.upper()
     print(s)

def whispering(s):
    s.lower()

def greet(fun):
    s = "Abhi"
    shout(s)
    whispering(s)
    f = fun()
    return f

# var = fun()
greet(fun)


