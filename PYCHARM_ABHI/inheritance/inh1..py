class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


# Creating an instance of the Person class
emp = Person("Abhi", 579)

emp.display()
