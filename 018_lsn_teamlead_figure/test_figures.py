import pytest
from figure_class import Rectangle, Circle, Triangle


class TestFigures:
    def test_rectangle(self):
        r = Rectangle(4, 6)
        assert r.area() == 24
        assert r.perimeter() == 20

    def test_circle(self):
        c = Circle(2)
        assert round(c.area(), 2) == round(2 * 3.1415926535 * 2, 2)
        assert round(c.perimeter(), 2) == round(3.1415926535 * 2 ** 2, 2)

    def test_triangle(self):
        t = Triangle(3, 4, 5)
        assert t.perimeter() == 12
        assert round(t.area(), 2) == 6.0
