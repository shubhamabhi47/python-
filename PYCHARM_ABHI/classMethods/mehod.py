class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def dog_years(human_years):
        return human_years * 7


# Usage
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(Dog.get_species())
print(Dog.dog_years(3))

# Output: Buddy says woof!
# Output: Canis lupus familiaris
# Output: 21
