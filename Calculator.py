from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"This is a {self.__class__.__name__} shape"
