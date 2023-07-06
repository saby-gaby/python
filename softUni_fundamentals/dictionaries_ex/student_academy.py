students_grades = {}
commands_count = int(input())

for _ in range(commands_count):
    student = input()
    grade = float(input())
    if student not in students_grades:
        students_grades[student] = [grade]
    else:
        students_grades[student].append(grade)

filtered_students = {name: sum(grades) / len(grades) \
                     for name, grades in students_grades.items() \
                     if sum(grades) / len(grades) >= 4.5}

for student, grades in filtered_students.items():
    print(f'{student} -> {grades:.2f}')
