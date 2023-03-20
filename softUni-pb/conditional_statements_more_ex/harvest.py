from math import floor, ceil

winery_area = int(input())
kg_per_m = float(input())
wine_needed = int(input())
workers = int(input())

grapes_for_wine = winery_area * kg_per_m * 0.4
wine = grapes_for_wine / 2.5

difference = abs(wine - wine_needed)

if wine >= wine_needed:
    left = difference / workers
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(left)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(abs(difference))} liters wine needed.')
