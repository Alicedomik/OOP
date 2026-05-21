import math

class RationalError(ZeroDivisionError):
    def __init__(self, message = "Знаменник не може бути рівним нулю."):
        self.message = message
        super().__init__(self.message)

class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise RationalError()

        common = math.gcd(n, d)
        self._n = n // common
        self._d = d // common

        if self._d < 0:
            self._n *= -1
            self._d *= -1

    @property
    def n(self):
        return self._n

    @property
    def d(self):
        return self._d

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"

if __name__ == "__main__":
    try:
        r1 = Rational(3, 4)
        print(r1)

        r2 = Rational(5, 0)
        print(r2)

    except RationalError as e:
        print(e)