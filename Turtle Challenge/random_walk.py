from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.width(10)
tim.speed(10)


def move_turtle():
    directions = [0, 90, 180, 270]
    direction = random.choice(directions)

    tim.forward(30)
    tim.setheading(direction)


colors = ["blue", "lime", "yellow", "red", "purple", "deep pink", "deep sky blue"]

for _ in range(200):
    color = random.choice(colors)
    tim.color(color)
    move_turtle()


screen = Screen()
screen.exitonclick()
