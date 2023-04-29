from turtle import Turtle, Screen

tim = Turtle()


def move_fwd():
    tim.forward(10)


def move_bwd():
    tim.backward(10)


def counter_clock():
    tim.left(10)


def clock():
    tim.right(10)


screen = Screen()


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(fun=move_fwd, key="w")
screen.onkey(fun=move_bwd, key="s")
screen.onkey(fun=counter_clock, key="a")
screen.onkey(fun=clock, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
