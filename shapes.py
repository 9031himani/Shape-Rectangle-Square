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


class Square(Rectangle):
    pass

    

sq = Square(2, 3)
print(sq.area())
