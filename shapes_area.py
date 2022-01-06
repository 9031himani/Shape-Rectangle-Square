class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length*self.breadth
        print(f"area of rectangle ={area}")

    def perimeter(self):
        perimeter = (self.length+self.breadth)/2
        print(f"perimeter of rectangle = {perimeter}")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        area = pow(self.side, 2)
        print(f"area of square = {area}")

    def perimeter(self):
        perimeter = self.side*4
        print(f"perimeter of square = {perimeter}")

    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5*self.base*self.height
        print(f"area of triangle = {area}")

    def perimeter(self): # Wrong, there is no concept of OOPS, if you are rewriting methods again and again.
        perimeter = 3*self.base
        print(f"perimeter of equilateral triangle is {perimeter}")


rct = Rectangle(4, 5)
rct.area()
rct.perimeter()

sq = Square(4)
sq.area()
sq.perimeter()

tri = Triangle(3, 7)
tri.area()
tri.perimeter()
