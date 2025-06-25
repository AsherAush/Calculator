from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side = side_length

    def __str__(self):
        return f"Square: side_length={self.side}, area={self.get_area()}, perimeter={self.get_perimeter()}"