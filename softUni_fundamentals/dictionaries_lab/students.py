students = {}
command = input()

while ':' in command:
    name, student_id, course = command.split(':')
    if student_id not in students:
        current_student = {'name': name, 'id' : student_id, 'course': course}
        students[student_id] = current_student

    command = input()

course = command.split('_')
course = ' '.join(course)

for student in students.values():
    if student['course'] == course:
        print(f'{student["name"]} - {student["id"]}')
