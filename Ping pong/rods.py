import turtle

class Rod(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(5,1)

    def go_up(self):
        self.teleport(self.xcor(),self.ycor()+20)

    def go_down(self):
        self.teleport(self.xcor(),self.ycor()-20)