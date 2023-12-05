from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.exit_message = "press q to end game"
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        """show left side player's score"""
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        """show right side player's score"""
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        """show end button"""
        self.goto(160, -280)
        self.write(arg=self.exit_message, move=True, align="right", font=("Courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()