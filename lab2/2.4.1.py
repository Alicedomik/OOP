import math
import turtle
import datetime
class Digit:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
    def draw(self, t):
        t.hideturtle()
        t.goto(self.x, self.y)
        t.pendown()
        t.write(self.n)
        t.penup()

class ClockFace:
    def __init__(self,r):
        self.digit = []
        self.r = r
        for i in range(1,13):
            angel = i * 30
            angel = math.radians(angel)
            x = self.r * math.sin(angel)
            y = self.r * math.cos(angel)
            self.digit.append(Digit(i,x,y))
    def setup(self, t):
        t.hideturtle()
        t.penup()
        t.goto(0, -self.r - 20)
        t.pendown()
        t.circle(self.r + 20)
        t.penup()
        for digit in self.digit:
            digit.draw(t)

class Hand:
    def __init__(self, length, color, width):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.color(color)
        self.t.width(width)
        self.length = length

    def draw(self, angle):
        self.t.clear()
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(90 - angle) # 90 градусів - це "північ" у turtle
        self.t.pendown()
        self.t.forward(self.length)
        self.t.penup()

class Clock:
    def __init__(self):
        turtle.tracer(0)
        self.face = ClockFace(150)
        self.hour_hand = Hand(70, "black", 4)
        self.min_hand = Hand(110, "black", 4)
        self.sec_hand = Hand(130, "red", 2)
        self.face.setup(turtle.Turtle())

    def update(self):
        now = datetime.datetime.now()
        s_angle = now.second * 6
        m_angle = now.minute * 6 + now.second * 0.1
        h_angle = (now.hour % 12) * 30 + now.minute * 0.5
        self.hour_hand.draw(h_angle)
        self.min_hand.draw(m_angle)
        self.sec_hand.draw(s_angle)
        turtle.update()
        turtle.ontimer(self.update, 1000)






c = Clock()
c.update()
turtle.done()