class Employee:
    def __init__(self , nm , sal , ag):
        self.name = nm
        self.salary = sal
        self.age = ag
    def disp(self):
        print(f"Name is {self.name} , Salary is {self.salary} and age is {self.age}")

e1 = Employee("Abhi",45000,19)
e2 = Employee("Shub",50000,20)
e1.disp()
e2.disp()
#accessing attributes outside the class
print(e1.age)
print(e2.salary)
e2.salary = 60000   #updating attribute
print(e2.salary)