from turtle import Turtle, Screen
import time
from player import Player
from car import Car
from scoreboard import Score

screen=Screen()
screen.setup(height=630 , width=600)
screen.tracer(0)

player=Player()
car=Car()
scoreboard=Score()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()
    for cars in car.all_car:
      if cars.distance(player)<20:
         game_is_on=False
         scoreboard.game_over()

    #succesful crossing
    if player.is_at_finish():
        player.go_to_start()
        car.level_up()
        scoreboard.increased_level()

screen.exitonclick()
