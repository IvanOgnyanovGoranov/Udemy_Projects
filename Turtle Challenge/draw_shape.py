from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

colors = ["blue", "lime", "yellow", "red", "purple", "deep pink", "deep sky blue"]


def draw_shape(sides_number: int):
    angle = 360 / sides_number
    for _ in range(sides_number):
        tim.forward(100)
        tim.right(angle)


for n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(n)

draw_shape(5)
screen = Screen()
screen.exitonclick()