class circle:
    def area(self, rad):
        self.area = 3.424*rad*rad
        self.perimeter = 2*3.414*rad

    def display(self):
        print(f"Area of the circle: {self.area}")
        print(f"circumference of the circle: {self.perimeter}")

c1 = circle()
c1.area(int(input("Enter radius of the circle:")))
c1.display()



#efine a class cirle with an attribute radius include method to calculate area and circumference of the circle
