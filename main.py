from turtle import Turtle , Screen
from paddle import Paddle 
from ball import Ball
import time
from score import Score

screen =Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score = Score()

paddle_1 = Paddle()
paddle_1.goto(350 , 0)

paddle_2 = Paddle()
paddle_2.goto(-350 ,0)

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "a")
screen.onkey(paddle_2.move_down, "s")

game_is_on= True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddle_1) <50 and ball.xcor() >320 or ball.distance(paddle_2) <50 and ball.xcor()< -320:
        ball.bounce_x()
        # ball.increse_speed()

    if ball.xcor()>380 :
        score.r_point()
        ball.refresh()


    if ball.xcor()<-380:
        score.l_point()
        ball.refresh()
        



















screen.exitonclick()

