import  random

def draw(john,shape):
    if shape == "square" :
        draw_shape(john,4)
    elif shape == "pentagon" :
        draw_shape(john,5)
    elif shape == "hexagon" :
        draw_shape(john,6)
    elif shape == "dashed" :
        john.forward(5)
        john.penup()
        john.forward(5)
        john.pendown()

def draw_shape(john,n):
    for _ in range(n):
        john.forward(100)
        john.right(360/n)


# Random wald------------------
colors = ["cyan","blue","pale turquoise","firebrick","goldenrod","lime","black","medium spring green"]

angle = [0,90,180,270]

def random_walk(john):
    john.width(5)
    for i in range(50):
        john.color(random.choice(colors))
        john.forward(20)
        john.dot(10, random.choice(colors))
        john.right(random.choice(angle))
