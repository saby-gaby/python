from math import ceil, floor

num = int(input())

roof = int(num / 2) if num % 2 == 0 else ceil(num / 2)
stars = 2 if num % 2 == 0 else 1

for roof_row in range(roof):
    print(floor((num - stars) / 2) * '-' + stars * '*' + floor((num - stars) / 2) * '-')
    stars += 2

for house in range(num - roof):
    print('|' + (num - 2) * '*' + '|')
