from turtle import Turtle, position
DOWN = 270
UP = 90
pos = [(370, 0), (-380, 0)]


class Paddle(Turtle):
    def __init__(self, i):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos[i])

    def up(self):
        if self.ycor() < 300 or self.ycor() > -300:
            a = pos[0][0]
            b = pos[0][1] + 50
            pos[0] = (a, b)
            self.goto(pos[0])

    def down(self):
        if self.ycor() < 300 or self.ycor() > -300:
            a = pos[0][0]
            b = pos[0][1] - 50
            pos[0] = (a, b)
            self.goto(pos[0])

    def w(self):
        if self.ycor() < 300 or self.ycor() > -300:
            a = pos[1][0]
            b = pos[1][1] + 50
            pos[1] = (a, b)
            self.goto(pos[1])

    def s(self):
        if self.ycor() < 300 or self.ycor() > -300:
            a = pos[1][0]
            b = pos[1][1] - 50
            pos[1] = (a, b)
            self.goto(pos[1])
