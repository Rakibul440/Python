from turtle import Turtle,Screen


t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def counter_clock():
    t.right(10)

def clock_dir():
    t.left(10)

def clear_screen():
    t.clear()
    t.home() # move back the turtle in origin
    t.clear()

screen.listen() # listen screen events
screen.onkey(move_forward ,"w")
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='d',fun=counter_clock)
screen.onkey(key='c',fun=clear_screen)
screen.onkey(clock_dir,'a')

screen.exitonclick()