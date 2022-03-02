from turtle import*
import time

speed(0)


def drawline(length, recursion):
    if recursion == 0:
        forward(length)
        right(60)
        forward(length)
        left(120)
        forward(length)
        right(60)
        forward(length)
    else:
        drawline(length/3, recursion-1)
        right(60)
        drawline(length/3, recursion - 1)
        left(120)
        drawline(length/3, recursion - 1)
        right(60)
        drawline(length / 3, recursion - 1)

hideturtle()
penup()
left(90)
forward(455)
right(90)
pendown()
length = 300
recursion = 5
right(60)
for x in range(0, 3):
    drawline(length, recursion)
    right(120)

time.sleep(5)