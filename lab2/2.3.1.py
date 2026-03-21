import turtle
class Stem:
    def __init__(self, length):
        self.length = length

    def draw(self,t, angle):
        t.color("green")
        t.pensize(3)
        t.setheading(angle)
        t.pendown()
        t.forward(self.length)
        t.penup()

class Leaf:
    def __init__(self, radius):
        self.radius = radius

    def draw(self,t):
        t.color("green")
        t.pensize(3)
        t.begin_fill()
        t.pendown()
        t.circle(self.radius, 60)
        t.end_fill()
        t.penup()

class Petal:
    def __init__(self, radius):
        self.radius = radius

    def draw(self,t, color):
        t.color(color)
        t.pensize(3)
        t.begin_fill()
        t.pendown()
        t.circle(self.radius, 90)
        t.left(90)
        t.circle(self.radius, 90)
        t.end_fill()
        t.penup()


class Flower:
    def __init__(self, Stem, Leaf, Petal):
        self.stem = Stem
        self.leaf = Leaf
        self.petal = Petal

    def draw(self,t, x,y, n, color, angel):
        t.penup()
        t.setheading(0)
        t.goto(x,y)
        self.stem.draw(t, angel)
        top_pos = t.pos()
        t.backward(self.stem.length/2)
        t.setheading(angel+30)
        self.leaf.draw(t)
        t.goto(top_pos)
        for i in range(n):
            t.setheading(angel + i * (360 / n))
            self.petal.draw(t, color)
            t.goto(top_pos)
        t.goto(top_pos)
        t.setheading(angel)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.color("yellow")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
s = Stem(200)
l = Leaf(100)
p = Petal(60)
flower = Flower(s, l, p)
base_x, base_y = 0, -200
angles = [60, 90, 120]
colors = ["red", "pink", "orange"]
for i in range(len(angles)):
    flower.draw(t, base_x, base_y, 6, colors[i], angles[i])

turtle.done()

