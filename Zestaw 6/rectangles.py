from points import Point
import unittest

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Współrzędne muszą tworzyć poprawny prostokąt.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def center(self):
        return Point(
            (self.pt1.x + self.pt2.x) / 2, 
            (self.pt1.y + self.pt2.y) / 2
        )

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        return Rectangle(
            self.pt1.x + x, self.pt1.y + y, 
            self.pt2.x + x, self.pt2.y + y
        )

class TestRectangle(unittest.TestCase):
    def test_str(self):
        r = Rectangle(1, 2, 4, 6)
        self.assertEqual(str(r), "[(1, 2), (4, 6)]")

    def test_eq(self):
        self.assertTrue(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4))
        self.assertFalse(Rectangle(1, 2, 3, 4) == Rectangle(0, 0, 3, 4))

    def test_center(self):
        r = Rectangle(0, 0, 4, 4)
        self.assertEqual(r.center(), Point(2, 2))

    def test_area(self):
        r = Rectangle(0, 0, 4, 5)
        self.assertEqual(r.area(), 20)

    def test_move(self):
        r = Rectangle(1, 2, 3, 4)
        moved = r.move(1, 1)
        self.assertEqual(moved, Rectangle(2, 3, 4, 5))

    def test_invalid_rectangle(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 1, 1)

if __name__ == "__main__":
    unittest.main()
