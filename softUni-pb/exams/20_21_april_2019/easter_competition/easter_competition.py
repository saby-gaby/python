breads_count = int(input())
best_baker = ''
best_baker_points = 0

for bread in range(breads_count):
    points = 0
    baker = input()

    while True:
        grade = input()

        if grade == 'Stop':
            break

        grade = int(grade)
        points += grade

    print(f'{baker} has {points} points.')

    if points > best_baker_points:
        best_baker = baker
        best_baker_points = points
        print(f'{baker} is the new number 1!')

print(f'{best_baker} won competition with {best_baker_points} points!')
