from typing import Tuple, List
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.constraints = []

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, point1, point2):
        if isinstance(point1, Point):
            self.p1 = point1
        elif isinstance(point1, (Tuple, List)):
            self.p1 = Point(*point1)
        else:
            raise TypeError("Incorrect types")

        if isinstance(point2, Point):
            self.p2 = point2
        elif isinstance(point1, (Tuple, List)):
            self.p2 = Point(*point2)
        else:
            raise TypeError("Incorrect types")

        self.constraints = []

    def middle(self):
        x = (self.p1.x + self.p2.x)/2
        y = (self.p1.y + self.p2.y)/2
        return Point(x, y)

    def length(self):
        return math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)

    def tang(self):
        return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)

    def __str__(self):
        return f"p1={self.p1} p2={self.p2}"


class Constraints:
    def __init__(self):
        pass


class Parallelism(Constraints):
    def __init__(self, line1, line2):
        super().__init__()
        self.line1 = line1
        self.line2 = line2

    def get_const(self):
        dx = self.line2.length() / math.sqrt(1 + self.line1.tang()**2)
        dy = self.line1.tang() * dx

        self.line2.p2.x, self.line2.p2.y = self.line2.p1.x + dx, self.line2.p2.y + dy


p1 = Point(0, 0)
p2 = Point(2, 6)

p3 = Point(7, 0)
p4 = Point(10, 6)

line11 = Line(p1, p2)
line22 = Line(p3, p4)

parall = Parallelism(line11, line22)
parall.get_const()

print(line22)
