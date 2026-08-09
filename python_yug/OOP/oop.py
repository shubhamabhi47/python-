# class Employee:
#     def __init__(self , nm , ag):
#         self.name = nm
#         self.age = ag
#     def disp(self):
#         print("Name of employee:",self.name)

# e1 = Employee("Abhi",19)
# e2 = Employee("Shub",20)
# e1.disp()
# e2.disp()

#NON PARAMETRISED CONSTRUCTOR

# class Employee:
#     def __init__(self):
#         self.salary = 2200
#         self.age = 21
# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)


#PARAMETERISED CONSTRUCTOR

# class Employee:
#     def __init__(self , sal , ag):
#         self.salary = sal
#         self.age = ag
# e1 = Employee(40000, 22)
# e2 = Employee(45000 , 23)
# print("first Employee:",e1.__dict__)
# print("Second Employee:",e2.__dict__)



#DEFAULT CONSTRUCTOR

class Employee:
    def __init__(self):
        pass
e1 = Employee()
e2 = Employee()
print(e1.__dict__)


#self is a memory reference for current object