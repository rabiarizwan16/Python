from turtle import Turtle
import pandas as pd
font=("courier", 24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.score=[]
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=font)

    def increased_level(self):
        self.level += 1
        self.update_scoreboard()
        self.score.append(self.level)
    def game_over(self):
        self.goto(0,0)
        self.score = pd.DataFrame(self.score)
        final_score = self.score.to_csv("score.csv")

        self.write(f"Game Over", align="center", font=font)
