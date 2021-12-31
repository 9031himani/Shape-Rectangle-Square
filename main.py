class Shape:

    def __init__(self, dimension):
        self.dimension = dimension


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = (self.length)*(self.breadth)
        return area

        Shape.__init__(self, dimension)

class Square(Rectangle):
    def __init__(self):
        super().__init__(Rectangle)
        if self.length == True and self.breadth == True:
            print("It is a 2 dimensional figure.")
