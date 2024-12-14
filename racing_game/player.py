from turtle import Turtle
starting_point=[0,-280]
move_distance= 10
finish_line= 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(starting_point)
        self.setheading(90)
    def go_up(self):
        self.forward(move_distance)

    def go_to_start(self):
        self.goto(starting_point)
    def is_at_finish(self):
         if self.ycor() > finish_line:
            return True
         else:
             return False

