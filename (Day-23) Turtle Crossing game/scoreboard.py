from turtle import Turtle


ALIGNMENT = 'center'
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-290, 265)
        self.update_level()

    def update_level(self):
        text = f"Level: {self.level}"
        self.clear()
        self.write(text, move=False, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

