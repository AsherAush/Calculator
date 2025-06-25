import  math
from Calculator import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle: radius={self.radius}, area={self.get_area()}, perimeter={self.get_perimeter()}"