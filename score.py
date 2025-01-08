from turtle import Turtle
FONT = ("Courier", 15, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()

    def draw_middle_line(self):
        self.goto(0, -300)
        self.seth(90)
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def increase_x_score(self):
        self.player_1_score += 1

    def increase_y_score(self):
        self.player_2_score += 1

    def display_score(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score: {self.player_1_score}", False, align="right", font=FONT)
        self.goto(100, 270)
        self.write(f"Score: {self.player_2_score}", False, align="left", font=FONT)
