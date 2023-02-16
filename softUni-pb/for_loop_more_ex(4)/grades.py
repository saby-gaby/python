students = int(input())
top, good, weak, fail = 0, 0, 0, 0
sum_grades = 0

for _ in range(students):
    grade = float(input())
    sum_grades += grade

    if grade >= 5:
        top += 1
    elif grade >= 4:
        good += 1
    elif grade >= 3:
        weak += 1
    else:
        fail += 1

top_students_percent = f'{top / students * 100:.2f}%'
good_students_percent = f'{good / students * 100:.2f}%'
weak_students_percent = f'{weak / students * 100:.2f}%'
fail_students_percent = f'{fail / students * 100:.2f}%'
average_grade = f'{sum_grades / students:.2f}'

print('Top students: ' + top_students_percent)
print('Between 4.00 and 4.99: ' + good_students_percent)
print('Between 3.00 and 3.99: ' + weak_students_percent)
print('Fail: ' + fail_students_percent)
print('Average: ' + average_grade)
