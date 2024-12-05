import random
from turtle import Turtle,Screen

# screen set up
screen = Screen()
width = 500
height = 500
screen.setup(width, height)

is_race_on = False

# Input text box
user_bet = screen.textinput("Your bet","Which turtle will win the race?\nEnter the color : ").lower()
print(user_bet)
#Trutle colors and names
colors = ["red","green","blue","black","yellow","purple"]
y_cor = -100

# Store turtles into a list
turtles = []

# creating 6 turtles
for i in range(0,6):
    tim = Turtle(shape="turtle")
    turtles.append(tim)
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230,y_cor)
    y_cor += 50

# check user did any bet or not
if user_bet and user_bet in colors:
    is_race_on = True
else:
    print("Please bet correctly!!")
#Race start
while is_race_on :
    for turtle in turtles:
        rand_dist = random.randint(1,10)

        # Finish the race while one of turtle race the finishing point
        if turtle.xcor() > 230 :
            winner_turtle_color = turtle.color()[0]
            #User's turtle won or not
            if winner_turtle_color == user_bet :
                print("Congratulation!You win the bet.")
            else:
                print(f"You loos the bet!\n{winner_turtle_color} won the race!!")
            is_race_on = False

        turtle.forward(rand_dist)




screen.exitonclick()