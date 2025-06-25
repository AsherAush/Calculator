from  Calculator import Shape
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return 4 * self.side_length

    def __str__(self):
        return f"Square: side_length={self.side_length}, area={self.get_area()}, perimeter={self.get_perimeter()}"