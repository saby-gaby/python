def add_course(list_lessons, lesson):
    if lesson not in list_lessons:
        list_lessons.append(lesson)
    return list_lessons


def insert_course(lessons, lesson, index):
    if lesson not in lessons:
        lessons.insert(index, lesson)
    return lessons


def remove_course(lessons, lesson):
    if lesson in lessons:
        index_of_lesson = lessons.index(lesson)
        if index_of_lesson + 1 in range(len(lessons) - 1):
            if 'Exercise' in lessons[index_of_lesson + 1]:
                lessons.pop(index_of_lesson + 1)
        lessons.pop(index_of_lesson)
    return lessons


def swap_course(lessons, lesson1, lesson2):
    if lesson1 in lessons and lesson2 in lessons:
        first_i, second_i = lessons.index(lesson1), lessons.index(lesson2)
        has_ex_one, has_ex_two = False, False
        if first_i + 1 in range(len(lessons)):
            has_ex_one = 'Exercise' in lessons[first_i + 1]
        if second_i + 1 in range(len(lessons)):
            has_ex_two = 'Exercise' in lessons[second_i + 1]
        lessons[first_i], lessons[second_i] = lessons[second_i], lessons[first_i]
        if has_ex_one and has_ex_two:
            lessons[first_i + 1]. lessons[second_i + 1] = \
                lessons[second_i + 1], lessons[first_i + 1]
        elif has_ex_one:
            lessons.insert(second_i + 1, lessons.pop(first_i + 1))
        elif has_ex_two:
            lessons.insert(first_i + 1, lessons.pop(second_i + 1))
    return lessons


def add_exercise(lessons, lesson):
    if lesson in lessons and f'{lesson}-Exercise' not in lessons:
        lesson_index = lessons.index(lesson)
        lessons.insert(lesson_index + 1, f'{lesson}-Exercise')
    if lesson not in lessons:
        lessons.append(lesson)
        lessons.append(f'{lesson}-Exercise')
    return lessons


course_content = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    action = command[0]
    lesson_name = command[1]
    if action == 'Add':
        course_content = add_course(course_content, lesson_name)
    elif action == 'Insert':
        course_content = insert_course(course_content, lesson_name, int(command[2]))
    elif action == 'Remove':
        course_content = remove_course(course_content, lesson_name)
    elif action == 'Swap':
        course_content = swap_course(course_content, lesson_name, command[2])
    elif action == 'Exercise':
        course_content = add_exercise(course_content, lesson_name)

    command = input()

for i, curr_lesson in enumerate(course_content):
    print(f'{i + 1}.{curr_lesson}')
