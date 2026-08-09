# def AbyB(a,b):
#     try:
#         c = ((a+b)/(a-b))
#     except ZeroDivisionError:
#         print("a/b result in 0.")
#     else:
#         print(c)
# AbyB(2.0,3.0)
# AbyB(3.0,3.0)
#




num1 = int(input("Enter  a number:"))
num2 = int(input("Enter  another number:"))

try:
    div = num1/num2
    print(div)    #NameError
except (ZeroDivisionError , NameError) as obj:
    print(obj)
else:
    print("Exception didnt occured.")
finally:
    print("finally block executed.")

print("Rest of the code.")

    