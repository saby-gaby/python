fail_count = int(input())
fail_counter = 0
last_problem = ''
total_grades = 0
grades_counter = 0

while fail_counter < fail_count:
    task_name = input()
    if task_name == 'Enough':
        print(f'Average score: {total_grades / grades_counter:.2f}')
        print(f'Number of problems: {grades_counter}')
        print(f'Last problem: {last_problem}')
        break

    grade = int(input())

    last_problem = task_name
    total_grades += grade
    grades_counter += 1

    if grade <= 4:
        fail_counter += 1
else:
    print(f'You need a break, {fail_count} poor grades.')

