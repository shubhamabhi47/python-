# def local(name):
#     age = 19 #local variable
#     X = 50
#     print("Age :",age)
#     print(f"{name} has age {age}")

#     #let 500 lines of code
#     print("Local varibles in key value pair:",locals())
#     variables = locals()
#     print("Length of local:",len(variables))
#     print(variables['X'])
#     print(variables['age'])

# local("Abhi")




# name = "Abhimanyu"  #global variable
# def display():
#     name = "Abhi"
#     age = 19    #local variable
#     print("Age :",age)
#     print(f"{name} has age {age}")


# display()
# print(globals())
# print(name)





#unboundlocalerror and global keyword
# num = 10
# def disp():
#     num = num + 5           #UnboundLocalError
#     num = 20
#     #print('inside',num)    #UnboundLocalError: cannot access local variable 'num' where it is not associated with a value

# disp()
# print('outside',num)



num = 10
def disp():
    global num
    num = num + 5           #UnboundLocalError
    print('inside',num)


disp()
print('outside',num)

