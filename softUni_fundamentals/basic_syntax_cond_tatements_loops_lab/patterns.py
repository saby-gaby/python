stars_max_count = int(input())

for stars_count in range(1, stars_max_count + 1):
    print(stars_count * '*')

for stars_count in range(stars_max_count -1, 0, -1):
    print(stars_count * '*')
