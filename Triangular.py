from Rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return 0.5 * self.width * self.height

    def get_perimeter(self):
        permit = (self.width**2 + self.height**2)**0.5
        return self.width + self.height + permit

    def __str__(self):
        return f"Triangle with base {self.width} and height {self.height} and area {self.get_area()} and perimeter {self.get_perimeter()}"