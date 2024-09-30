import turtle
from random import randint

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.turtlesize(0.5,0.5)
        self.teleport(randint(-100,100),randint(-100,100))
        self.head = randint(0,60)
        self.setheading(self.head)
        self.movespeed = 0.08
    def move(self):
        self.forward(5)
    def restart(self):
        self.goto(0,0)
        self.head = 180+self.head
        self.setheading(self.head)
        self.movespeed=0.08