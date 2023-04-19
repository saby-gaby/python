import turtle   # sudo apt-get install python3-tk
import random

pen = turtle.Pen()
turtle.bgcolor('black')

for i in range(1, 361):

    x = random.randint(0, 5)  # and replace x -> l in if

    if x % 6 == 0:
        pen.pencolor('red')
    elif x % 6 == 1:
        pen.pencolor('purple')
    elif x % 6 == 2:
        pen.pencolor('blue')
    elif x % 6 == 3:
        pen.pencolor('green')
    elif x % 6 == 4:
        pen.pencolor('orange')
    elif x % 6 == 5:
        pen.pencolor('yellow')

    pen.width(i // 100 + 1)
    pen.forward(i)
    pen.left(59.25)

turtle.exitonclick()
