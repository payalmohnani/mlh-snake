from turtle import Turtle
from time import sleep

STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(20,0), (0,0), (-20,0)]

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.snake_body.append(part)

    def extend(self):
        new_pos = self.snake_body[-1].position()
        self.add_part(new_pos)

    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x,new_y)

        self.head.forward(STEPS)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for part in self.snake_body:
            part.hideturtle()

        self.snake_body.clear()
        sleep(0.2)
        self.create_snake()
        self.head = self.snake_body[0]






    