import turtle
from turtle import *

color('red', 'yellow')
turtle.speed(2500)
begin_fill()
while True:
    forward(400)
    left(123)
    right(234)

    if abs(pos()) < 1:
        break
end_fill()
done()
