from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)  # this method removes every animation from the screen when set to 0
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


def exit_game():
    global game_on
    screen.delay(5)
    game_on = False


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()  # this method ensures that the paddle is at the new position before it pops up on the screen
    """move the ball"""
    ball.move()

    """bounce the ball"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """detect collision with r_paddle and l_paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """detect out of bounds and add a score to opposite player if a paddle misses the ball"""
    if ball.xcor() > 380:  # if right paddle misses
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:  # if left paddle misses
        ball.reset_position()
        scoreboard.r_point()

    screen.onkey(exit_game, "q")



screen.exitonclick()
