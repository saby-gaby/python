tank_capacity = 255
number_of_lines = int(input())
liters_in_tank = 0

for _ in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water > tank_capacity:
        print('Insufficient capacity!')
        continue
    liters_in_tank += liters_of_water
    tank_capacity -= liters_of_water
print(liters_in_tank)
