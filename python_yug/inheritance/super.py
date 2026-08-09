class Computer(object):
    def __init__(self,ram , storage):
        self.ram = ram
        self.storage = storage
        print("Computer class constructor called.")

    def display(self):
        print("Hello, all Done!")


class Mobile(Computer):
    def __init__(self, ram , storage):
        super().display()
        self.model = "Iphone X"
        print("Mobile class constructor called.")

ram = input("Enter ram:")
storage = input("Enter storage:")
Apple = Mobile(ram , storage)
print(Apple.__dict__)