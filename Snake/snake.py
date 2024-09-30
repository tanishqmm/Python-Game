import turtle as t
import time
import food
import scoreboard
track = scoreboard.scoreboard()
screen = t.Screen()
screen.delay()
f=food.Food()
class Snake:
    def __init__(self):
        # self.score = 0
        self.turtle1=t.Turtle()
        self.turtle_list=[ self.turtle1]
        self.turtle1.color("white")
        self.turtle1.shape("square")
        self.turtle1.penup()

    def collision(self):
        t=self.turtle1
        if t.xcor()>290:
            return False
        elif t.xcor()<-290:
            return False
        elif t.ycor()>290:
            return False
        elif t.ycor()<-290:
            return False
        else:
            return True
    def createnew(self):
        turtle = t.Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        self.turtle_list.append(turtle)
        head = self.turtle_list[-2].heading()
        turtle.setheading(head)
        x = self.turtle_list[-2].xcor()
        y = self.turtle_list[-2].ycor()
        if head == 0:
            turtle.teleport(x-21,y)
        elif head == 90:
            turtle.teleport(x, y-21)
        elif head == 180:
            turtle.teleport(x + 21, y)
        else:
            turtle.teleport(x, y+21)

    def newgame(self):
        self.createnew()
    def move(self):
        l = self.turtle_list
        f.changeloc()

        while True:
            track.update()
            while (self.collision()):
                screen.update()
                time.sleep(0.1)

                if(l[0].distance(f.pos())<15):
                    f.changeloc()
                    self.createnew()
                    track.inc()
                    track.update()

                else:
                    for i in range(len(self.turtle_list)-1,0,-1):
                        newx = l[i-1].xcor()
                        newy = l[i-1].ycor()
                        l[i].goto(newx,newy)
                    l[0].forward(20)
            with open("highscore.txt",mode="r") as file:
                high=int(file.read())
            with open("highscore.txt", mode="w") as file:
                if high<track.score:
                    file.write(f"{track.score}")
                else:
                    file.write(f"{high}")
            track.score = 0
            for t in self.turtle_list[1:]:
                t.hideturtle()
            self.turtle_list = []
            self.turtle1.home()
            self.turtle_list.append(self.turtle1)
            self.createnew()
            self.move()



    def left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)
    def right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)
    def up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)
    def down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)