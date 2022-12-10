# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 20)
# rgb_list = []
#
# for color in colors:
#     rgb = color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     color_tuple = (red, green, blue)
#     rgb_list.append(color_tuple)
from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
screen = Screen()
colormode(255)
turtle.hideturtle()
turtle.speed("fastest")

colors_hirst = [
    (210, 156, 102), (57, 98, 133), (157, 81, 52), (239, 227, 234),
    (223, 240, 236), (138, 159, 192), (51, 174, 121), (232, 201, 101), (158, 167, 39), (121, 190, 175),
    (202, 135, 153), (66, 39, 33), (75, 113, 88), (26, 48, 67), (133, 29, 48), (127, 81, 91),
    (181, 93, 109), (197, 93, 74)
]
rows = 10
dots_in_a_row = 10
x = -250
y = -250

turtle.penup()
for n in range(rows):
    turtle.goto(x, y)
    for _ in range(dots_in_a_row):
        turtle.dot(20, random.choice(colors_hirst))
        turtle.fd(50)
    y += 50


screen.exitonclick()
