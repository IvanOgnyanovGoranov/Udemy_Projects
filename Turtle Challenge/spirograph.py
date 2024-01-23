from turtle import Turtle, Screen
import random

colors = ["blue", "lime", "yellow", "red", "purple", "deep pink", "deep sky blue"]

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed(0)

for _ in range(36):
    tim.color(random.choice(colors))
    tim.circle(60)
    tim.left(10)


screen = Screen()
screen.exitonclick()
