import math
from abc import ABC, abstractmethod as abm

class Shape(ABC):
    @abm
    def area(self):
        pass
    
    @abm
    def perimeter(self):
        pass

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def get_point(self):
        return self.x, self.y


class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.point_one = Point(self.x1, self.y1)
        self.point_two = Point(self.x2, self.y2)

    def length(self):
        if self.point_one.y != self.point_two.y:
            a = (self.point_one.x - self.point_two.x) ** 2
            b = (self.point_one.y - self.point_two.y) ** 2
            self.length = math.sqrt(a + b)
            return self.length
        else:
            self.length = math.sqrt((self.point_one.x - self.point_two.x) ** 2)
            return self.length


class Square(Line, Shape):

    def area(self):
        return self.length() ** 2

    def perimeter(self):
        return self.length() * 4


class Cube(Square):
    def volume(self):
        side = self.length()
        return side ** 3


class Rect(Shape):
    def __init__(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.side_a = Line(x1, x2, y1, y2).length()
        self.side_b = Line(x3, x4, y3, y4).length()

    def area(self):
        return self.side_b * self.side_a

    def perimeter(self):
        return (self.side_b * 2) + (self.side_a * 2)


point = Point(5, 3).get_point()
area = Square(5, 3, 8, 12).area()
perimeter = Square(5, 3, 8, 12).perimeter()
length = Square(5, 3, 8, 12).length()
volume = Cube(5, 3, 8, 12).volume()
rect_area = Rect(2, 3, 5, 6, 8, 10, 23, 41).area()
rect_perimeter = Rect(2, 3, 5, 6, 8, 10, 23, 41).perimeter()
print(point, area, perimeter, length, volume, rect_area, rect_perimeter)

