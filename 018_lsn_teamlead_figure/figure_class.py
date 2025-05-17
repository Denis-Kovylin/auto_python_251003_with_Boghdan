from abc import ABC, abstractmethod
from math import pi
from math import sqrt


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Невірне значення ширини фігури")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Невірне значення висоти фігури")

        self.__width = width
        self.__height = height

    def __str__(self):
        return (
            f"Ця фигура є прямокутником.\n"
            f"Ширина: {self.__width}\n"
            f"Висота: {self.__height}\n"
        )

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Невірне значення радиусу")

        self.__radius = radius

    def __str__(self):
        return (
            f"Ця фигура є колом.\n"
            f"Радіус: {self.__radius}\n"
        )

    def area(self) -> float:
        return 2 * pi * self.__radius

    def perimeter(self) -> float:
        return pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if not isinstance(side_a, (int, float)) or side_a <= 0:
            raise ValueError("Невірне значення для сторони А")
        if not isinstance(side_b, (int, float)) or side_b <= 0:
            raise ValueError("Невірне значення для сторони B")
        if not isinstance(side_c, (int, float)) or side_c <= 0:
            raise ValueError("Невірне значення для сторони C")
        if not (side_a + side_b > side_c and
                side_a + side_c > side_b and
                side_b + side_c > side_a):
            raise ValueError("Сторони не утворюють трикутник")

        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def __str__(self):
        return (
            f"Ця фігура є трикутником.\n"
            f"Сторона A: {self.__side_a}\n"
            f"Сторона B: {self.__side_b}\n"
            f"Сторона C: {self.__side_c}\n"
        )


    def perimeter(self) -> int | float:
        return self.__side_a + self.__side_b + self.__side_c


    def area(self) -> int | float:
        p = self.perimeter()
        s = p / 2
        return sqrt(
            s *
            (s - self.__side_a) *
            (s - self.__side_b) *
            (s - self.__side_c)
        )

