from turtle import *
from random import randint

hideturtle()
speed(0)
penup()
title('Sierpinski Triangle')

vertex1 = (0, 385)
vertex2 = (-400, -365)
vertex3 = (400, -365)
vertices = [vertex1, vertex2, vertex3]

for i in vertices:
    goto(i)
    dot(5)


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

size = 10
first_point = (randint(0, 500), randint(0, 500))
goto(first_point)
dot(size, 'red')
while True:
    direction = randint(0, 2)
    position = pos()
    for idx, value in enumerate(vertices):
        if direction == idx:
            goto(midpoint(value, pos()))
            dot(size, 'red')
done()
