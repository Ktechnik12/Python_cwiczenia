import unittest

class Poly:
    def __init__(self, c=0, n=0):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Stopień wielomianu musi być liczbą całkowitą nieujemną")
        self.size = n + 1
        self.a = [0] * self.size
        self.a[-1] = c

    def __str__(self):
        return " + ".join(f"{coeff}*x^{i}" for i, coeff in enumerate(self.a) if coeff != 0) or "0"

    def __add__(self, other):
        if isinstance(other, Poly):
            size = max(self.size, other.size)
            result = [0] * size
            for i in range(self.size):
                result[i] += self.a[i]
            for i in range(other.size):
                result[i] += other.a[i]
            return Poly.from_coeffs(result)
        elif isinstance(other, (int, float)):
            result = self.a[:]
            result[0] += other
            return Poly.from_coeffs(result)
        else:
            raise ValueError("Dodawanie wspiera tylko Poly lub liczby")

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Poly):
            size = max(self.size, other.size)
            result = [0] * size
            for i in range(self.size):
                result[i] += self.a[i]
            for i in range(other.size):
                result[i] -= other.a[i]
            return Poly.from_coeffs(result)
        elif isinstance(other, (int, float)):
            result = self.a[:]
            result[0] -= other
            return Poly.from_coeffs(result)
        else:
            raise ValueError("Odejmowanie wspiera tylko Poly lub liczby")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            result = [-coeff for coeff in self.a]
            result[0] += other
            return Poly.from_coeffs(result)
        else:
            raise ValueError("Odejmowanie wspiera tylko liczby")

    def __mul__(self, other):
        if isinstance(other, Poly):
            result = [0] * (self.size + other.size - 1)
            for i, coeff1 in enumerate(self.a):
                for j, coeff2 in enumerate(other.a):
                    result[i + j] += coeff1 * coeff2
            return Poly.from_coeffs(result)
        elif isinstance(other, (int, float)):
            result = [coeff * other for coeff in self.a]
            return Poly.from_coeffs(result)
        else:
            raise ValueError("Mnożenie wspiera tylko Poly lub liczby")

    __rmul__ = __mul__

    def __neg__(self):
        return Poly.from_coeffs([-coeff for coeff in self.a])

    def is_zero(self):
        return all(coeff == 0 for coeff in self.a)

    def __eq__(self, other):
        return isinstance(other, Poly) and self.a == other.a

    def eval(self, x):
        result = 0
        for coeff in reversed(self.a):
            result = result * x + coeff
        return result

    def __len__(self):
        return len(self.a)

    def __getitem__(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Indeks poza zakresem")
        return self.a[i]

    def __setitem__(self, i, value):
        if i < 0 or i >= self.size:
            raise IndexError("Indeks poza zakresem")
        self.a[i] = value

    def __iter__(self):
        return iter(self.a)

    def __call__(self, x):
        if isinstance(x, (int, float)):
            return self.eval(x)
        elif isinstance(x, Poly):
            return self.combine(x)
        else:
            raise ValueError("Nieprawidłowy argument")

    def combine(self, other):
        result = Poly(0)
        power = Poly(1)
        for coeff in self.a:
            result += power * coeff
            power *= other
        return result

    @classmethod
    def from_coeffs(cls, coeffs):
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        obj = cls()
        obj.size = len(coeffs)
        obj.a = coeffs
        return obj


class TestPoly(unittest.TestCase):
    def test_init_and_str(self):
        p = Poly(3, 2)
        self.assertEqual(str(p), "3*x^2")

    def test_addition(self):
        p1 = Poly(3, 2)
        p2 = Poly(2, 1)
        self.assertEqual(str(p1 + p2), "2*x^1 + 3*x^2")
        self.assertEqual(str(p1 + 5), "5*x^0 + 3*x^2")

    def test_subtraction(self):
        p1 = Poly(3, 2)
        p2 = Poly(2, 1)
        self.assertEqual(str(p1 - p2), "-2*x^1 + 3*x^2")
        self.assertEqual(str(p1 - 5), "-5*x^0 + 3*x^2")

    def test_multiplication(self):
        p1 = Poly(2, 1)
        p2 = Poly(3, 1)
        self.assertEqual(str(p1 * p2), "6*x^2")
        self.assertEqual(str(p1 * 5), "10*x^1")

    def test_eval(self):
        p = Poly(3, 2)
        self.assertEqual(p.eval(2), 12)

    def test_len(self):
        p = Poly(3, 2)
        self.assertEqual(len(p), 3)

    def test_get_set_item(self):
        p = Poly(3, 2)
        self.assertEqual(p[2], 3)
        p[2] = 5
        self.assertEqual(p[2], 5)

    def test_iter(self):
        p = Poly(3, 2)
        coeffs = [coeff for coeff in p]
        self.assertEqual(coeffs, [0, 0, 3])

if __name__ == "__main__":
    unittest.main()
