def sort_to_do_notes():
    curr_note = input()
    tasks = []
    while curr_note != 'End':
        tasks.append(curr_note)
        curr_note = input()
    sorted_tasks = sorted(tasks, key=lambda x: int(x.split('-')[0]))
    sorted_tasks = [task.split('-')[1] for task in sorted_tasks]
    return sorted_tasks
print(sort_to_do_notes())

# curr_note = input()
# sorted_tasks = [0] * 10
#
# while curr_note != 'End':
#     note = curr_note.split('-')
#     importance, curr_note = int(note[0]), note[1]
#     sorted_tasks[importance - 1] = curr_note
#
#     curr_note = input()
# sorted_tasks = [task for task in sorted_tasks if task]
# print(sorted_tasks)
