jury = int(input())
total_grades = 0
grades_counter = 0

while True:
    presentation = input()

    if presentation == 'Finish':
        break

    sum_grades = 0

    for _ in range(jury):
        sum_grades += float(input())
        grades_counter += 1

    total_grades += sum_grades
    print(f'{presentation} - {sum_grades / jury:.2f}.')

print(f'Student\'s final assessment is {total_grades / grades_counter:.2f}.')
