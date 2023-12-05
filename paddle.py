from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):  # we initialized the position, so we can call it in main.py by passing a tuple of
        super().__init__()  # ..x and y coordinates

        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        self.forward(20)
        # alternative code:
        # y_cor = self.ycor() + 20
        # self.goto(self.xcor(), y_cor)

    def down(self):
        self.backward(20)
        # alternative code:
        # y_cor = self.ycor() - 20
        # self.goto(self.xcor(), y_cor)
