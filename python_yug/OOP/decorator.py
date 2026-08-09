#@classmethod
class Employee:
    company_name = "Infosys"  #Class variable
    def __init__(self , nm , sal , ag):
        self.name = nm
        self.salary = sal
        self.age = ag
    @classmethod
    def get_company_name(cls):
        cls.company_name = "TCS"  #we can modify class variable
        print(f"Company name is :",cls.company_name)

e1 = Employee("Abhi",45000,19)
e2 = Employee("Shub",50000,20)

Employee.get_company_name()  #no need to pass as cls is  automaticall pass implicitly
print(e1.company_name)
print(e2.company_name)


