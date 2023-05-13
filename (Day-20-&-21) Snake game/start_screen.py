from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'bold')


class StartScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(20, 0)
        self.color('white')
        self.write("PRESS", move=False, align=ALIGNMENT, font=FONT)
        self.color('purple')
        self.write("ENTER", move=False, align=ALIGNMENT, font=FONT)
        self.color('white')
        self.write("TO START", move=False, align=ALIGNMENT, font=FONT)
