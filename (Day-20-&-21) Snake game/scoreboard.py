from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        text = f"Score: {self.score}"
        self.clear()
        self.write(text, move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

