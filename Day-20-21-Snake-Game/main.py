from turtle import  Turtle,Screen
import  time
from SnakeClass import Snake

# ---------- Screen Set up ------------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off animation

# Create Snake Object
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# ------ moving all the segments together ------
is_game_on = True

while is_game_on:
    screen.update()  # update the result after doing work
    time.sleep(0.1) # delay this code block 1 sec

    snake.move()









screen.exitonclick()