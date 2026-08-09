class Employee:
    '''This is employee class for maintaining employee data'''
    def __init__(self , nm , ag):
        self.name = nm
        self.age = ag
    def disp(self):
        print(f"name is : {self.name} and age is {self.age}")

e1 = Employee("Abhi",19)
e2 = Employee("Shub",20)

print(Employee.__doc__)
print('-'*50)
print(Employee.__dict__)
print('-'*50)
print(Employee.__name__)
print('-'*50)
print(Employee.__module__)