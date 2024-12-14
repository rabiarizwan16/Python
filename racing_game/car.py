from turtle import Turtle
import random
colors=["red","yellow","green", "orange","purple","blue"]
start_move=5
increment_move=10

class Car:
    def __init__(self):
        self.all_car=[]
        self.car_speed =start_move

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
          new_car = Turtle("square")
          new_car.shapesize(stretch_wid=1, stretch_len=2)
          new_car.penup()
          new_car.color(random.choice(colors))
          y=random.randint(-250, 250)
          new_car.goto(300,y)
          self.all_car.append(new_car)

    def move_car(self):
        for cars in self.all_car:
            cars.backward(start_move)

    def level_up(self):
        self.car_speed += increment_move



