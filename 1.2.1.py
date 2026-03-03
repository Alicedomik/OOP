class QuadraticEquation:
    def __init__(self, a=0.0, b=0.0, c=0.0):
        if isinstance(a, QuadraticEquation)
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)

    def solve(self):
        if self.a == 0.0:
            if self.b == 0.0:
                if self.c == 0.0:
                    return float('inf')
                else:
                    return ()
            else:
                return (-self.c / self.b,)
        discriminant = (self.b * self.b) - (4 * self.a * self.c)
        if discriminant < 0:
            return ()
        if discriminant == 0:
