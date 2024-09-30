import turtle
import ball
import rods
import score
import time

track = score.Score()
rodA = rods.Rod()
rodB = rods.Rod()
rodA.teleport(-350,0)
rodB.teleport(350,0)

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
# screen.onkey()
ball = ball.Ball()
screen.onkeypress(rodB.go_up, "Up")
screen.onkeypress(rodB.go_down, "Down")
screen.onkeypress(rodA.go_up, "w")
screen.onkeypress(rodA.go_down, "s")

game_is_on = True

while game_is_on:
    head = ball.heading()
    time.sleep(ball.movespeed)
    if ball.xcor() > 360 or ball.xcor() < -360:
        if(ball.xcor()>0):
            track.left += 1
        else :
            track.right += 1
        track.clear()
        track.teleport(-50, 250)
        track.show()
        ball.restart()

    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(-head)

    elif ball.xcor()+5 > 330 and abs(ball.ycor()-rodB.ycor()) <= 50:
        ball.setheading(head+180-2*head)
        ball.movespeed *= 0.8
    elif ball.xcor()-5<-330 and abs(ball.ycor()-rodA.ycor())<=50:
        ball.setheading(180 - head)

    ball.move()



screen.exitonclick()

