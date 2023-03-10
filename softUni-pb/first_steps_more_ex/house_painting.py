x = float(input())
y = float(input())
h = float(input())

door_area = 1.2 * 2
front_back_areas = (x * x) * 2 - door_area
window_area = 1.5 * 1.5
sides_area = (x * y) * 2 - 2 * window_area
green_area = front_back_areas + sides_area
green_consumption = format(green_area / 3.4, '.2f')

print(green_consumption)

roof_side_areas = 2 * x * y
roof_front_back_areas = x * h
red_area = roof_side_areas + roof_front_back_areas
red_consumption = format(red_area / 4.3, '.2f')

print(red_consumption)
