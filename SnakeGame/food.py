from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color("grey")
        self.write('2', font=("Arial", 1, "bold"), align="center")
        self.up()
        number = 42

        
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed('fastest')
        x_coord = randint(-280, 280)
        y_coord = randint(-280, 250)
        self.goto(x=x_coord, y=y_coord)
        self.write(number, align="center", font=("Arial", 16, "normal"))
        self.hideturtle()
    def refresh(self):
        number = 42
        x_coord = randint(-280, 280)
        y_coord = randint(-280, 280)
        self.goto(x=x_coord, y=y_coord)
        self.write(number, align="center", font=("Arial", 16, "normal"))
        self.hideturtle()