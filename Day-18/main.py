import turtle
from turtle import  *
import  random

t = Turtle()
t.speed("fastest")

# Set the color mode to RGB (0-255)
turtle.colormode(255)

# Generate Random Color
def random_color():
    r = random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r,g,b)

    return random_color

# Random Walk
angle = [0,90,180,270]

def random_walk():
    t.width(5)
    for i in range(200):
        t.color(random_color())
        t.forward(20)
        # t.dot(10, random_color())
        t.right(random.choice(angle))
        
random_walk()

screen = Screen()
screen.exitonclick()