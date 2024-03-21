from turtle import Turtle, Screen
import random

turtle = Turtle()
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

turtle.pensize(10)
turtle.speed(10)
while True:
    direction = random.randint(0, 3)
    turtle.pencolor(colours[random.randint(0, len(colours) - 1)])
    if direction == 0:
        turtle.forward(25)
    elif direction == 1:
        turtle.left(90)
    elif direction == 2:
        turtle.right(90)
    elif direction == 3:
        turtle.right(180)



screen = Screen()
screen.exitonclick()
