import math

figure = input()
area = 0

if figure == 'square':
    side = float(input())
    area = math.pow(side, 2)
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == 'circle':
    r = float(input())
    area = math.pi * math.pow(r, 2)
elif figure == 'triangle':
    side = float(input())
    h = float(input())
    area = side * h / 2

# print(format(area, '.3f'))
print(f'{area:.3f}')
