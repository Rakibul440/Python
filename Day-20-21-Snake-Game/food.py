from turtle import Turtle
import  random
class Food(Turtle) :
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        rand_x_cord = random.randint(-270,270)
        rand_y_cord = random.randint(-270,270)
        self.goto(rand_x_cord,rand_y_cord)

