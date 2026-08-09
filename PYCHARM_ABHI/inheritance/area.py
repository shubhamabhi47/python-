class GeometricFigure:
    def area(self):
        pass

class Rec(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area of rectangle:",self.width * self.height)


class Square(GeometricFigure):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of square:",self.side ** 2)


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("area of circle:",3.414 * self.radius ** 2)

# Example usage
rec = Rec(int(input("Enter width of rec:")), int(input("Enter height of rec:")))
rec.area()
square = Square(int(input("Enter length of side of square:")))
square.area()
circle = Circle(int(input("Enter radius of circle:")))
circle.area()





# print(f"Rectangle area: {rec.area()}")
# print(f"Square area: {square.area()}")
# print(f"Circle area: {circle.area()}")
