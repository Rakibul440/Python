import random
import turtle
from turtle import *

t = Turtle()
t.speed("fastest")

# Random color Function
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color_ = (r,g,b)
    return color_


# Draw Circle
def spirograph(size):
    for i in range(int(360/size)) :
        t.circle(100)
        t.color(random_color())
        t.setheading(t.heading() + size)

spirograph(6)




screen = Screen()
screen.exitonclick()