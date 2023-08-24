first_per_hour = int(input())
second_per_hour = int(input())
third_per_hour = int(input())
students = int(input())
students_per_hour = first_per_hour + second_per_hour + third_per_hour
hours_needed = 0

while students > 0:
    students -= students_per_hour
    hours_needed += 1

    if hours_needed % 4 == 0:
        hours_needed += 1

print(f'Time needed: {hours_needed}h.')
