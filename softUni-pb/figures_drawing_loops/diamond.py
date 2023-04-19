num = int(input())

sides = int((num - 2) / 2) if num % 2 == 0 else int((num - 1) / 2)
first_row_stars = 2 if num % 2 == 0 else 1
diamond_range = num if num % 2 == 0 else num + 1

for row in range(1, diamond_range):

    if row == 1 or row == num:
        print(sides * '-' + first_row_stars * '*' + sides * '-')
    else:
        print(sides * '-' + '*' + (num - (2 * sides + 2)) * '-' + '*' + sides * '-')

    if row < num / 2:
        sides -= 1
    else:
        sides += 1
