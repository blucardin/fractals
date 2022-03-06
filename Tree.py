

"""This is not well functioning code. This does not generate a nice fractal."""


from turtle import *

hideturtle()
title('Sierpinski Triangle')
speed(0)
right(90)

def draw_line(vertex1, angle, length):
    setheading(270)
    penup()
    goto(vertex1)
    pendown()

    right(angle)
    forward(length)
    pos1 = pos()

    backward(length)

    setheading(270)
    left(angle)
    forward(length)
    pos2 = pos()

    return pos1, pos2


def recursion(lists):
    vertex = lists[0]
    angle = lists[1]
    length = lists[2]
    pos1, pos2 = draw_line(vertex, angle, length)

    lines_todraw.append((pos2, angle + angle_reduce, length - len_reduce))
    lines_todraw.append((pos1, angle + angle_reduce, length - len_reduce))


vertex1 = (0, 385)
starting_length = 130
starting_angle = 10

penup()
goto(vertex1)
pendown()
forward(starting_length)
starting_pos = pos()

len_reduce = 5
angle_reduce = 10


lines_todraw = [(starting_pos, starting_angle, starting_length - len_reduce)]

while len(lines_todraw) > 0:
    recursion(lines_todraw[0])
    lines_todraw.pop(0)

done()