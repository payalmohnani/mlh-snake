from turtle import Screen
from snake import Snake
from time import sleep
from score import Score
from food import Food

screen = Screen()
screen.setup(width = 500, height=500)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
score = Score()
food = Food()

screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right, key = "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    
    # Food 
    if snake.head.distance(food) <= 15:
        food.refresh()
        score.change_score()
        score.update_score()
        snake.extend()

    # Wall collision
    if (snake.head.xcor() > 230) or (snake.head.xcor() < -230) or (snake.head.ycor() > 230) or (snake.head.ycor() < -230):
        score.reset()
        snake.reset()
        exit_game = screen.numinput("Game Over", "Press 0 to Exit the game", 1, minval=0, maxval=1000)
        if exit_game == 0:
            game_is_on = False
            break

    
    # Tail collision
    for tail in snake.snake_body[1:]:
        if snake.head.distance(tail) < 10:
            score.reset()
            snake.reset()
            screen.numinput("Game Over", "Press 0 to Exit the game", 1, minval=0, maxval=1000)
            if exit_game == 0:
                game_is_on = False
                break



screen.exitonclick()