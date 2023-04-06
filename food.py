from turtle import Turtle 
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        x = randint(-210,210)
        y = randint(-210,210)
        self.goto(x,y)
        self.refresh()

    def refresh(self):
        x = randint(-210,210)
        y = randint(-210,210)
        self.goto(x,y)



