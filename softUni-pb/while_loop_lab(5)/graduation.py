student_name = input()

class_counter = 1
fail_counter = 0
grades_sum = 0

while True:
    if class_counter > 12:
        break

    if fail_counter == 2:
        break

    curr_grade = float(input())

    if curr_grade >= 4:
        class_counter += 1
        grades_sum += curr_grade
    else:
        fail_counter += 1

if class_counter > 12:
    average_grade = grades_sum / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{student_name} has been excluded at {class_counter} grade')
