# create two classes, one is Address with attributes street , city and zip_code and other is person
# with attribute name and address attributes that holds an instance of address class
# write a method in person that display person's name along with their address details


class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def disp(self):
        print(f"Name: {self.name}")
        print(f"Address: street_name-> {self.address.street}, City_name->{self.address.city}, Zip_code->{self.address.zip_code}")


a1 = Address("Prabhakar_road", "Sasaram", "821115")

p1 = Person(input("Enter name of the person:"), a1)

p1.disp()
