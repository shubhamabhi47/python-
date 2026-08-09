class Student:
    def __init__(self, nm, grd):
        self.name = nm
        self.grade = grd

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")

s1 = Student(input("Enter name of the student:"), input("Enter grade of that student:"))
s1.display()



#efine a class cirle with an attribute radius include method to calculate area and circumference of the circle

#define  a book class with attribute name title , author , and price .
# give price a default of 20
# create two instances of book one with  specied price and one without and print their details

#define a class Employee with private attributes name , salary , write a method to set and get the values of their attributes
# then create an instance of employee and use methods to set and display its details 