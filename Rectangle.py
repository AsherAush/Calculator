from Calculator import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}, area={self.get_area()}, perimeter={self.get_perimeter()}"
