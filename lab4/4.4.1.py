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
        self.t.setheading(90 - angle)
        self.t.pendown()
        self.t.forward(self.length)
        self.t.penup()


class Watch:
    def __init__(self):
        self.t = turtle.Turtle()
    @staticmethod
    def get_current_time():
        return datetime.datetime.now().time()
    def update(self):
        pass
    def run(self):
        self.update()

class AnalogWatch(Watch):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.face = ClockFace(150)
        self.hour_hand = Hand(70, "black", 4)
        self.min_hand = Hand(110, "black", 4)
        self.sec_hand = Hand(130, "red", 2)
        self.face.setup(self.t)

    def update(self):
        now = self.get_current_time()
        s_angle = now.second * 6
        m_angle = now.minute * 6 + now.second * 0.1
        h_angle = (now.hour % 12) * 30 + now.minute * 0.5
        self.hour_hand.draw(h_angle)
        self.min_hand.draw(m_angle)
        self.sec_hand.draw(s_angle)
        turtle.update()
        turtle.ontimer(self.update, 1000)

class DigitalWatch(Watch):
    def __init__(self, x=0, y=0, format = "24", color="black"):
        super().__init__()
        self.format = format
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(x, y)
        self.t.color(color)

    def update(self):
        now = self.get_current_time()
        hour, minute, second = now.hour, now.minute, now.second
        if self.format == "12":
            if hour < 12:
                suf = " AM"
            else:
                suf = " PM"
            display_h = hour % 12
            if display_h == 0:
                display_h = 12
            time_str = f"{display_h:02d}:{minute:02d}:{second:02d}{suf}"
        else:
            time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
        self.t.clear()
        self.t.write(time_str, align="center", font=("Courier", 80, "bold"))
        turtle.ontimer(self.update, 1000)


a = AnalogWatch()
a.update()
turtle.done()

# d = DigitalWatch()
# d.run()
# turtle.done()