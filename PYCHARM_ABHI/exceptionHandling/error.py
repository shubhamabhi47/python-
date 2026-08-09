#SyntaxError:This exception is raised when the interpreter encounters a syntax error in the code such as
# misspelled keyeord,a missing colon,or an unbalance parenthesis.
# try:
#     x = 1/0
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# NameError: raised when a variable is not defined
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined.")
# except:
#     print("somthing else went wrong.")
# TypeError: raised when an operation is attempted on a value of an inappropriate type
# IndexError: raised when a list index is out of range
# KeyError: raised when a dictionary key is not found
# IOError: raised when an input/output operation fails
# ZeroDivisionError: raised when a number is divided by zero
def fun(a):
    if (a<4):
        b=a/(a-3)
    print("Value of b =" ,b)
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivision Occured and Handled.")
except NameError:
    print("NameError Occured and Handled.")
    
    
# def fun(a):
#     if (a < 4):
#         b = a / (a - 3)
#     else:
#         # Reference an undefined variable to trigger NameError
#         b = c  
#     print("Value of b =", b)

# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivision Occurred and Handled.")
# except NameError:
#     print("NameError Occurred and Handled.")



#ImportError:raised when an import statement fails to find module when it is not installed or not present in the python environment
#ValueError:raised when the correct type is passed but an inappropriate value is used