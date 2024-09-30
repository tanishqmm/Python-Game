import turtle
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.right = 0
        self.left = 0
        self.color("white")
        self.width(10)

    def show(self):
        self.write(f"{self.left} | {self.right}", align="center", font=("Courier", 20, "normal"))

