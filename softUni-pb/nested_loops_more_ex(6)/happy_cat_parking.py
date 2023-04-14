days = int(input())
hours = int(input())

to_pay = 0

for day in range(1, days + 1):
    current_day_sum = 0

    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            current_day_sum += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            current_day_sum += 1.25
        else:
            current_day_sum += 1

    to_pay += current_day_sum

    print(f'Day: {day} - {current_day_sum:.2f} leva')

print(f'Total: {to_pay:.2f} leva')
