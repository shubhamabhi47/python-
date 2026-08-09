class Employee:
    def setName(self , nm):    #setter mathod
        self.name = nm
    
    def getName(self):         #getter method
        print("The name is :", self.name)

e1 = Employee()
e2 = Employee()
e1.setName(input("Enter the name for e1 obj :"))
e2.setName(input("Enter the name for e2 obj :"))
print("e1 oject is :", e1.__dict__)
print("e2 oject is :", e2.__dict__)
e1.getName()
e2.getName()
# e2 = Employee("Sumnn")
# e3 = Employee("Rizzz")
