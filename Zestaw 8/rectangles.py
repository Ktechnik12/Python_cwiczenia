class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Współrzędne muszą tworzyć poprawny prostokąt.")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Lista lub krotka musi zawierać dokładnie dwa punkty.")
        return cls(points[0][0], points[0][1], points[1][0], points[1][1])

    def __str__(self):
        return f"[({self.x1}, {self.y1}), ({self.x2}, {self.y2})]"

    def __repr__(self):
        return f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    def __eq__(self, other):
        return (self.x1, self.y1, self.x2, self.y2) == (other.x1, other.y1, other.x2, other.y2)

    @property
    def center(self):
        return ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)

    @property
    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def move(self, x, y):
        return Rectangle(
            self.x1 + x, self.y1 + y,
            self.x2 + x, self.y2 + y
        )

    @property
    def top(self):
        return self.y2

    @property
    def bottom(self):
        return self.y1

    @property
    def left(self):
        return self.x1

    @property
    def right(self):
        return self.x2

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def topleft(self):
        return (self.x1, self.y2)

    @property
    def bottomleft(self):
        return (self.x1, self.y1)

    @property
    def topright(self):
        return (self.x2, self.y2)

    @property
    def bottomright(self):
        return (self.x2, self.y1)
