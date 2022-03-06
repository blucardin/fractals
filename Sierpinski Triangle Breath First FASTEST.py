from turtle import *

hideturtle()
title('Sierpinski Triangle')
speed(0)


def midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def draw_triangle(vertex1, vertex2, vertex3):
    penup()
    goto(vertex1)
    pendown()
    goto(vertex2)
    goto(vertex3)
    goto(vertex1)


def recursion(vertices):
    vertex1 = vertices[0]
    vertex2 = vertices[1]
    vertex3 = vertices[2]

    midpoint1 = midpoint(vertex1, vertex2)
    midpoint2 = midpoint(vertex2, vertex3)
    midpoint3 = midpoint(vertex3, vertex1)
    draw_triangle(midpoint1, midpoint2, midpoint3)

    triangles_todraw.append((vertex3, midpoint3, midpoint2))
    triangles_todraw.append((vertex2, midpoint1, midpoint2))
    triangles_todraw.append((vertex1, midpoint1, midpoint3))


vertex1 = (0, 385)
vertex2 = (-400, -365)
vertex3 = (400, -365)
draw_triangle(vertex1, vertex2, vertex3)

triangles_todraw = [(vertex1, vertex2, vertex3)]


while len(triangles_todraw) > 0:
    recursion(triangles_todraw[0])
    triangles_todraw.pop(0)

done()
