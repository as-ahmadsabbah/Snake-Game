from turtle import Turtle

Starting_Positions = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_DISTENSE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake :
    def __init__(self) :
        self.segments = []
        self.create_Snake()
        self.head=self.segments[0]

    def create_Snake (self):
        for position in Starting_Positions:
            t = Turtle("square")
            t.color("#C6C61E")
            t.penup()
            t.goto(position)
            self.segments.append(t)

    def move (self):
        for seg in range(len(self.segments)-1,0,-1):
            x=self.segments[seg-1].xcor()
            y=self.segments[seg-1].ycor()
            self.segments[seg].goto(x,y)
        self.head.forward(SNAKE_DISTENSE)

    def up (self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down (self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left (self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right (self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def clr():
        Turtle.clear()

    def create_Snake2 (self):
        for position in Starting_Positions:
            t = Turtle("square")
            t.color("#C6C61E")
            t.penup()
            t.goto(self.segments[-1].xcor(),self.segments[-1].ycor())
            self.segments.append(t)
