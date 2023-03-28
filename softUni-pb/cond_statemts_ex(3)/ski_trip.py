stay_days = int(input())
room_type = input()
rate = input()
stay_nights = stay_days - 1

single_room = 18
apartment = 25
president_apartment = 35
stay_price = 0

if room_type == 'room for one person':
    stay_price = stay_nights * single_room
elif room_type == 'apartment':
    stay_price = stay_nights * apartment
    if stay_days < 10:
        stay_price *= 0.7
    elif stay_days <= 15:
        stay_price *= 0.65
    else:
        stay_price *= 0.5
elif room_type == 'president apartment':
    stay_price = stay_nights * president_apartment
    if stay_days < 10:
        stay_price *= 0.9
    elif stay_days <= 15:
        stay_price *= 0.85
    else:
        stay_price *= 0.8

if rate == 'positive':
    stay_price *= 1.25
elif rate == 'negative':
    stay_price *= 0.9

print(f'{stay_price:.2f}')
