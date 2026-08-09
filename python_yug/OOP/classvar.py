class Employee:
    company_name = "Infosys"  #Class variable
    def __init__(self , nm , sal , ag):
        self.name = nm
        self.salary = sal
        self.age = ag
    def disp(self):
        print(f"Name is {self.name} , Salary is {self.salary} and age is {self.age}")

e1 = Employee("Abhi",45000,19)
e2 = Employee("Shub",50000,20)

#we can access class variable by using class refrence or
# print(Employee.company_name) 
# print(e1.company_name)


#we can change class variable by using class refrence
# print("Before changing company name: ",Employee.company_name)
# Employee.company_name = "TCS"
# print("After changing company name:  ",Employee.company_name)


#e2.company_name = "TCS"  #it will create a variable in e2 object however it will not effect the class variable
#print(e2.__dict__)
#print(Employee.company_name)



#DECORATOR "@CLASSMETHOD"

