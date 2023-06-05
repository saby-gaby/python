from math import sqrt, pow, floor


def calculate_point(x, y):
    return sqrt(pow(x, 2) + pow(y, 2))


def closest_point(x_1, y_1, x_2, y_2):
    first_point = abs(calculate_point(x_1, y_1))
    second_point = abs(calculate_point(x_2, y_2))
    if first_point <= second_point:
        return print(f'({floor(x_1)}, {floor(y_1)})')
    return print(f'({floor(x_2)}, {floor(y_2)})')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
closest_point(x1, y1, x2, y2)
