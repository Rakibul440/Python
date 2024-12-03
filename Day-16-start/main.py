from turtle import Turtle , Screen
# screen class is where turtle object will be shown up

timmy = Turtle() # will be shown up on screen
timmy.shape('classic') # define shape as turtle
timmy.color('red') # set color

def move_square():
    for i in range(4) :
        timmy.forward(100) # move forward
        timmy.left(90) # give angle

# window configuration
my_screen = Screen()
print(my_screen.canvheight)

while True :
    move_square()
