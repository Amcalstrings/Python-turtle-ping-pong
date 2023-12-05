from turtle import Turtle

"""writing the ball class"""


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.ball_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    """getting the ball to move"""
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # the reason for this is incase we decide to change our self.y_move value, we would not
        # alter the bounce code... hence no self.y_move -= 10

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1


