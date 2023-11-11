from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            random_color = random.choice(COLORS)
            random_ycor = random.randint(-250, 250)
            car.setheading(180)
            car.color(random_color)
            car.setposition(300, random_ycor)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def optimize_cars(self):
        self.cars = [car for car in self.cars if car.xcor() > -320]

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

