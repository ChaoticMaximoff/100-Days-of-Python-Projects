import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move()
    car_manager.optimize_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect player reaching the finish line
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.reset_position()
        car_manager.increase_speed()


screen.exitonclick()
