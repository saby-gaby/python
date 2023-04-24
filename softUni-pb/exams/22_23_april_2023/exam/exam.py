students_count = int(input())

excellent, very_good, good, failed, sum_grades = 0, 0, 0, 0, 0,

for _ in range(students_count):
    grade_current_student = float(input())

    sum_grades += grade_current_student

    if grade_current_student < 3:
        failed += 1
    elif grade_current_student < 4:
        good += 1
    elif grade_current_student < 5:
        very_good += 1
    else:
        excellent += 1

print(f'Top students: {excellent / students_count * 100:.2f}%')
print(f'Between 4.00 and 4.99: {very_good / students_count * 100:.2f}%')
print(f'Between 3.00 and 3.99: {good / students_count * 100:.2f}%')
print(f'Fail: {failed / students_count * 100:.2f}%')
print(f'Average: {sum_grades / students_count:.2f}')
