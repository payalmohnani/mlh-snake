from turtle import Turtle

FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x = 0, y = 220)
        self.score = 0
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("high_score.txt", "w") as file:
                file.write("0")
                self.high_score = 0

        
        self.write(f"Score: {self.score}  High Score: {self.high_score}",font = FONT, align = ALIGNMENT)
        self.hideturtle()

    def change_score(self):
        self.score += 1


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",font = FONT, align = ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as file:
            file.write(f"{self.high_score}")

        self.score = 0

        self.update_score()