from turtle import  Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 8, 'normal')
FONT2 = ('Arial',15, 'normal')
class Scoreboadr(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,283)
        self.update_score()

    def update_score(self):
        self.write(f"Total Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT2)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
