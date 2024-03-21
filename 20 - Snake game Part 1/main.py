from turtle import Turtle, Screen
import random
import time

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = [Turtle() for _ in range(3)]

def snakeConfiguration(size):
    iteration = 0
    for part in snake:
        part.shape("square")
        part.color('white')
        part.penup()
        part.setx(iteration)
        iteration += size

def moveSnake(direction):
    screen.update()
    for part in snake:
        part.forward(20)
        time.sleep(0.1)
        
        
snakeConfiguration(20)
while True:
    moveSnake("test")

screen.exitonclick()

