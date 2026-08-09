class demo:
    pass
d1 = demo()


class Employee:
    def __init__(self , nm , sal , ag):
        self.name = nm
        self.salary = sal
        self.age = ag
    def disp(self):
        print(f"Name is {self.name} , Salary is {self.salary} and age is {self.age}")

e1 = Employee("Abhi",45000,19)
e2 = Employee("Shub",50000,20)

print(isinstance(e1 , Employee))

# if isinstance(obj name d1 ,Classname demo):
#     pass