from turtle import Screen
import snake as s
import food

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.listen()

game = s.Snake()

screen.onkey(game.left,"Left")
screen.onkey(game.right,"Right")
screen.onkey(game.up,"Up")
screen.onkey(game.down,"Down")
game.newgame()
game.move()
screen.exitonclick()