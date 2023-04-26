# import colorgram

# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g , b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random


color_list = [(236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

tim = Turtle()
tim.penup()
tim.goto(-240, -225)
tim.speed("fastest")
tim.hideturtle()
colormode(255)

for i in range(10):
    for j in range(10):
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.forward(50)
    new_line = tim.ycor() + 50
    tim.goto(-240, new_line)




screen = Screen()
screen.exitonclick()