from math import sqrt, pow, floor


def calculate_point(x, y):
    return sqrt(pow(x, 2) + pow(y, 2))


def get_line_length(x_1, y_1, x_2, y_2):
    line_length = pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)
    return line_length


def compare_lines(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    line_one = get_line_length(x_1, y_1, x_2, y_2)
    line_two = get_line_length(x_3, y_3, x_4, y_4)
    if line_one >= line_two:
        point_one = calculate_point(x_1, y_1)
        point_two = calculate_point(x_2, y_2)
        if abs(point_one) <= abs(point_two):
            return print(f'({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})')
        else:
            return print(f'({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})')
    point_one = calculate_point(x_3, y_3)
    point_two = calculate_point(x_4, y_4)
    if abs(point_one) <= abs(point_two):
        return print(f'({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})')
    return print(f'({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
compare_lines(x1, y1, x2, y2, x3, y3, x4, y4)
