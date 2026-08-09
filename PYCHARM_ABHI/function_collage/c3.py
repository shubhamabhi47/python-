class Book:
    def __init__(self, title, author, price=20):
        self.title = title
        self.author = author
        self.price = price

    def disp(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: INR{self.price}")


# Creating two instances: one with a specified price and one without
b1 = Book("Metamorphosis", "Franz Kafka", 20)
b2 = Book("Bhagavad Gita", "Vyasa", 20)

# b1 = Book(input("Enter the name of the book: "), "Franz Kafka", int(input("Enter price of that book:")))
# b2 = Book("Bhagavad Gita", "Vyasa", 20)

# Printing the details of both books
b1.disp()
b2.disp()
