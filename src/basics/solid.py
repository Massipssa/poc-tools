from abc import ABC, abstractmethod

from math import pi


# Open-Closed Principal
class Shape(ABC):
    def __int__(self, shape_type: str):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self) -> int:
        pass


class Circle(Shape):

    def __init__(self, radius: int):
        super.__init__("circle")
        self.radius = radius

    def calculate_area(self) -> int:
        return pi * self.radius ** 2
