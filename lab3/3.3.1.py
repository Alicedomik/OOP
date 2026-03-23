import math
class Figure:
    def __init__(self, *args):
        self.args = args
    def dimension(self):
        pass
    def perimetr(self):
        return None
    def square(self):
        return None
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        if self.dimension() == 2:
            return None
        else:
            pass
    def volume(self):
        if self.dimension() == 2:
            return self.square()
        else:
            pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        Figure.__init__(self,a,b,c)
    def dimension(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c
    def square(self):
        p = self.perimetr()/2
        s = p*(p-self.a)*(p-self.b)*(p-self.c)
        if s < 0 :
            return 0
        return s**0.5


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Figure.__init__(self,a,b)
    def dimension(self):
        return 2
    def perimetr(self):
        return (self.a+self.b)*2
    def square(self):
        return self.a*self.b


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        Figure.__init__(self,a,b,c,d)
    def dimension(self):
        return 2
    def square(self):
        if self.a != self.b :
            x = (self.a + self.b) / (4 * abs(self.a - self.b))
            y = (-self.a + self.b + self.c + self.d) * (self.a - self.b + self.c + self.d) * (
                        self.a - self.b + self.c - self.d) * (self.a - self.b - self.c + self.d)
            if y < 0 :
                return 0
            return x * (y ** 0.5)
        else :
            return self.a * self.b


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        Figure.__init__(self, a,b)
    def dimension(self):
        return 2
    def perimetr(self):
        return (self.a+self.b)*2
    def square(self):
        if self.h<=self.b:
            return self.a*self.h
        elif self.h<=self.a:
            return self.b*self.h
        else:
            return 0


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        Figure.__init__(self,r)
    def dimension(self):
        return 2
    def perimetr(self):
        return self.r*2*math.pi
    def square(self):
        return math.pi*self.r**2


class Ball(Figure):
    def __init__(self, r):
        self.r = r
        Figure.__init__(self,r)
    def dimension(self):
        return 3
    def squareSurface(self):
        return 4*math.pi*self.r**2
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        return 4*math.pi*self.r**3/3


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        self.a = a
        self.h = h
        Triangle.__init__(self,a, a, a)
    def dimension(self):
        return 3
    def squareSurface(self):
        m = (self.a ** 2 - (self.a / 2) ** 2) ** 0.5
        return m * self.perimetr() / 2
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def volume(self):
        return (self.squareBase() * self.h)/3


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        Rectangle.__init__(self,a,b)
    def dimension(self):
        return 3
    def squareSurface(self):
        m = ((self.a/2) ** 2 + self.h**2) ** 0.5
        return m * self.perimetr() / 2
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def volume(self):
        return super().square()*self.h/3


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        Rectangle.__init__(self,a,b)
    def dimension(self):
        return 3
    def squareSurface(self):
        return 2*self.c*(self.a+self.b)
    def squareBase(self):
        return super().square()
    def height(self):
        return self.c
    def volume(self):
        return self.a*self.b*self.c


class Cone(Circle):
    def __init__(self, r,h):
        self.r = r
        self.h = h
        Circle.__init__(self,r)
    def dimension(self):
        return 3
    def squareSurface(self):
        x = (self.r**2 + self.h**2)**0.5
        return x*self.r*math.pi
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def volume(self):
        return self.r**2*self.h*math.pi/3


class TriangularPrism(Triangle):
    def __init__(self, a,b,c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        Triangle.__init__(self,a,b,c)
    def dimension(self):
        return 3
    def squareSurface(self):
        return super().perimetr()*self.h
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def volume(self):
        return super().square()*self.h

def processing(filename):
    max_measure = 0
    largest_figure = None
    shape_map = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapeze,
        "Parallelogram": Parallelogram,
        "Circle": Circle,
        "Ball": Ball,
        "TriangularPyramid": TriangularPyramid,
        "QuadrangularPyramid": QuadrangularPyramid,
        "RectangularParallelepiped": RectangularParallelepiped,
        "Cone": Cone,
        "TriangularPrism": TriangularPrism
    }
    try:
        with open(filename) as f:
            for line in f:
                x = line.split()
                name = x[0]
                params = [float(i) for i in x[1:]]
                if name in shape_map:
                    figure = shape_map[name](*params)
                    measure = figure.volume()

                    if isinstance(measure, (int, float)) and measure > max_measure:
                        max_measure = measure
                        largest_figure = figure

        return largest_figure, max_measure
    except FileNotFoundError:
       print("File not found.")

result = processing("input01.txt")
figure, val = result
print(f"Найбільша фігура: {figure.__class__.__name__}, міра: {val:.2f}")
