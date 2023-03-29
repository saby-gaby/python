season = input()
group_type = input()
students = int(input())
nights = int(input())

price = 0
sport = ''

if group_type == 'boys':
    if season == 'Winter':
        price = students * nights * 9.6
        sport = 'Judo'
    elif season == 'Spring':
        price = students * nights * 7.2
        sport = 'Tennis'
    else:
        price = students * nights * 15
        sport = 'Football'
elif group_type == 'girls':
    if season == 'Winter':
        price = students * nights * 9.6
        sport = 'Gymnastics'
    elif season == 'Spring':
        price = students * nights * 7.2
        sport = 'Athletics'
    else:
        price = students * nights * 15
        sport = 'Volleyball'
elif group_type == 'mixed':
    if season == 'Winter':
        price = students * nights * 10
        sport = 'Ski'
    elif season == 'Spring':
        price = students * nights * 9.5
        sport = 'Cycling'
    else:
        price = students * nights * 20
        sport = 'Swimming'

if students >= 50:
    price *= 0.5
elif students >= 20:
    price *= 0.85
elif students >= 10:
    price *= 0.95

print(f'{sport} {price:.2f} lv.')
