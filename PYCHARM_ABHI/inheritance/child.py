# Base class
class Base:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


# Subclass inheriting from Parent
class Child(Base):
    def __init__(self, name, age):
        # Call Parent class constructor
        super().__init__(name)
        self.age = age

    def getAge(self):
        return self.age


class Grand(Child):
    def __init__(self, name, age, location):
        super().__init__(name, age)
        self.location = location

    def getLocation(self):
        return self.location

    def displayInfo(self):
        print(f"Name: {self.getName()}")
        print(f"Age: {self.getAge()}")
        print(f"Location: {self.getLocation()}")


# Creating an instance of Grandchild and displaying the information
grand= Grand("abhi", 19, "Sasaram")
grand.displayInfo()
