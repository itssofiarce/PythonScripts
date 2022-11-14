import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# Crating and moving the turtle
player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
# creatin and movin the cars
    car_manager.create_car()
    car_manager.move_cars()

# detec collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
# #detec when the side is reach
    if player.ycor() > 299:
        player.restart()
        car_manager.level_up()
        score.increase_level()


# add score
screen.exitonclick()
