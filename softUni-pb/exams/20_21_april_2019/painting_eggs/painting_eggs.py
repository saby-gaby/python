size = input()
color = input()
count = int(input())

if size == 'Large':
    if color == 'Red':
        profit = count * 16
    elif color == 'Green':
        profit = count * 12
    elif color == 'Yellow':
        profit = count * 9
elif size == 'Medium':
    if color == 'Red':
        profit = count * 13
    elif color == 'Green':
        profit = count * 9
    elif color == 'Yellow':
        profit = count * 7
elif size == 'Small':
    if color == 'Red':
        profit = count * 9
    elif color == 'Green':
        profit = count * 8
    elif color == 'Yellow':
        profit = count * 5

profit *= 0.65

print(f'{profit:.2f} leva.')
