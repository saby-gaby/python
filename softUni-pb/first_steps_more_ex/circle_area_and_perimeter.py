import math

r = float(input())

area = math.pi * math.pow(r, 2)

print(format(area, '.2f'))

perimeter = 2 * r * math.pi

print(format(perimeter, '.2f'))
