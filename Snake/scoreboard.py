import turtle




class scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.teleport(-20, 280)

    def update(self):
        self.teleport(-20, 260)
        self.clear()
        with open("highscore.txt",mode="r") as file:
            self.write(f"SCORE : {self.score} | High Score: {file.read()}", align="center", font=("Arial", 18, "normal"))
    def inc(self):
        self.score+=1