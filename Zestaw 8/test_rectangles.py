import pytest
from rectangles import Rectangle

def test_str():
    r = Rectangle(1, 2, 4, 6)
    assert str(r) == "[(1, 2), (4, 6)]"

def test_eq():
    assert Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4)
    assert Rectangle(1, 2, 3, 4) != Rectangle(0, 0, 3, 4)

def test_center():
    r = Rectangle(0, 0, 4, 4)
    assert r.center == (2, 2)

def test_area():
    r = Rectangle(0, 0, 4, 5)
    assert r.area == 20

def test_move():
    r = Rectangle(1, 2, 3, 4)
    moved = r.move(1, 1)
    assert moved == Rectangle(2, 3, 4, 5)

def test_invalid_rectangle():
    with pytest.raises(ValueError):
        Rectangle(2, 3, 1, 1)

def test_from_points():
    r = Rectangle.from_points(((1, 1), (4, 4)))
    assert r == Rectangle(1, 1, 4, 4)

def test_virtual_properties():
    r = Rectangle(1, 2, 5, 6)
    assert r.top == 6
    assert r.bottom == 2
    assert r.left == 1
    assert r.right == 5
    assert r.width == 4
    assert r.height == 4
    assert r.topleft == (1, 6)
    assert r.bottomleft == (1, 2)
    assert r.topright == (5, 6)
    assert r.bottomright == (5, 2)
