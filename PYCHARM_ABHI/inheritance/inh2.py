# Assuming the person class exists
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Person name: {self.name}")


# Defining the Emp class inheriting from Person
class Emp(Person):
    def __init__(self, name, id):
        super().__init__(name)  # Inheriting the name from Person
        self.id = id

    def Print(self):
        print("Employee class called")

    def display(self):
        super().display()  # Calling the display method from the Person class
        print(f"Employee ID: {self.id}")


# Creating an instance of the Emp class
e = Emp("Abhi", 579)

# Calling the display method
e.display()



#1)create a parent class geometric figure and child classes rectangle , square , circle each of which calculate the area of each


# 2)create a base class names parent which will get the name of the person by using getName function.
# Derive a subclass class named child that will get the name and age of the person
# now implement a class named grandchild which may be inherited from child and
# this class is taking the location the person display all the information as output


# 3)create  two classes DAD and MOM both classes have their own features  derive a class child
# which will be inherited the features from both the MOM and DAD classes
#  in first class function function is working as an instance of an object so we can store the function as a variable and
# it can be passed as a parameter or argument to another function
# we can return a functin from another function
# we can store the this type of function in different data structure like list, hash tables ,