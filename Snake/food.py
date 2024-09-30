import random
import turtle as t
class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(1)
        self.screen = t.Screen()


    def changeloc(self):

        newx = random.randint(-280,280)
        newy = random.randint(-280,280)
        self.teleport(newx, newy)

