import time
from turtle import Screen, Turtle
from ball import Ball
from score import Score
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:

    score.draw_middle_line()
    screen.update()
    time.sleep(ball.move_speed)
    score.display_score()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 345:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -345:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_x_score()

    if ball.xcor() < - 380:
        ball.reset_position()
        score.increase_y_score()

    ball.move()

screen.exitonclick()



