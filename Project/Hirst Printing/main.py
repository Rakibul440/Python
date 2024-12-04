import turtle
from turtle import Turtle,Screen


import colorgram
import random

t = Turtle()
turtle.colormode(255)

# Extract colors
colors = colorgram.extract('img.jpeg',30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    _color = (r,g,b)
    rgb_colors.append(_color)

# Draw a 10 by 10 Hirst Printing
def line():
    for _ in range(9) :
        t.dot(15, random.choice(rgb_colors))
        t.penup()
        t.forward(40)
        t.pendown()

    t.dot(15, random.choice(rgb_colors))

def direction_change(line_number):
    if line_number % 2 == 0:
        t.left(-90)
    else:
        t.left(90)
    t.penup()
    t.forward(40)
    if line_number % 2 == 0:
        t.left(-90)
    else:
        t.left(90)

# hide turtle
t.hideturtle()

# Draw the picture
t.speed("fast")
t.setheading(230)
t.penup()
t.forward(300)
t.pendown()
t.setheading(0)

for i in range(1,11):
    line()
    direction_change(i)



screen = Screen()
screen.exitonclick()