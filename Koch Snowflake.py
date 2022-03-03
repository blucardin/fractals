from turtle import*


def drawline(length, recursion):
    if recursion == 0:
        forward(length)
    else:
        drawline(length/3, recursion-1)
        left(60)
        drawline(length/3, recursion - 1)
        right(120)
        drawline(length/3, recursion - 1)
        left(60)
        drawline(length / 3, recursion - 1)

hideturtle()
speed(0)

penup()
left(90)
forward(385)
right(90)
pendown()

length = 660
recursion = 5
right(60)

for x in range(0, 3):
    drawline(length, recursion)
    right(120)

done()
