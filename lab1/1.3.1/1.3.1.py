import math
class Shape:
    def __str__(self):
        return f"{self.__class__.__name__}: Площа = {self.square():.2f}, Периметр = {self.perimeter():.2f}"
class Triangle(Shape):
    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and b + c > a
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s ** 0.5

class Rectangle(Shape):
    def __init__(self, a, b):
        assert a>0 and b>0
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a*2+self.b*2

    def square(self):
        return self.a*self.b


class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        assert abs(c-d)<abs(a-b)<(c+d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a+self.b+self.c+self.d

    def square(self):
        x = (self.a+self.b)/(4*abs(self.a-self.b))
        y = (-self.a+self.b+self.c+self.d)*(self.a-self.b+self.c+self.d)*(self.a-self.b+self.c-self.d)*(self.a-self.b-self.c+self.d)
        return x*(y**0.5)


class Parallelogram(Shape):
    def __init__(self, a, b, h):
        assert a>=h or b>=h
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return self.a*2+self.b*2

    def square(self):
        if self.h<=self.b:
            return self.a*self.h
        elif self.h<=self.a:
            return self.b*self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return self.r*2*math.pi

    def square(self):
        return self.r**2*math.pi

def processing(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            shapes = []
            for line in f:
                shape = line.split()
                name = shape[0]
                if name == "Triangle":
                    shapes.append(Triangle(*map(float, shape[1:])))
                elif name == "Rectangle":
                    shapes.append(Rectangle(*map(float, shape[1:])))
                elif name == "Trapeze":
                    shapes.append(Trapeze(*map(float, shape[1:])))
                elif name == "Parallelogram":
                    shapes.append(Parallelogram(*map(float, shape[1:])))
                elif name == "Circle":
                    shapes.append(Circle(*map(float, shape[1:])))
        max_square = max(shapes, key=lambda s: s.square())
        max_perimeter = max(shapes, key=lambda s: s.perimeter())
        res = f"Фігура з найбільшою площею: {max_square}\n"
        res += f"Фігура з найбільшим периметром: {max_perimeter}"
        return res
    except FileNotFoundError:
        print("Файл не знайдено")
    except TypeError:
        print("Неправильні дані вводу")
    except AssertionError:
        print("Такої фігури не існує")


with open("../output.txt", 'a', encoding='utf-8') as f:
    print(processing("input01.1.3.1"), file=f)
    print(processing("input02.1.3.1"), file=f)
    print(processing("input03.1.3.1"), file=f)