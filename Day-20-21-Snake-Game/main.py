from turtle import Screen
import  time
from SnakeClass import Snake
from food import Food
from scoreboard import Scoreboadr
# ---------- Screen Set up ------------
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off animation

# Create Snake Object
snake = Snake()
food = Food()
scoreboard = Scoreboadr()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# ------ moving all the segments together ------
is_game_on = True

while is_game_on:
    screen.update()  # update the result after doing work
    time.sleep(0.1) # delay this code block 0.1 sec

    snake.move()
    # Collision detect btw food and snake
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend() # extend the snake
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.game_over()
        is_game_on = False

    # Detect collision with own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5 :
            scoreboard.game_over()
            is_game_on = False





screen.exitonclick()