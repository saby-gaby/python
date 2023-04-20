budget = float(input())
gender = input()
age = int(input())
sport = input()

card_price = 0

if sport == 'Gym':
    if gender == 'm':
        card_price = 42
    else:
        card_price = 35
elif sport == 'Boxing':
    if gender == 'm':
        card_price = 41
    else:
        card_price = 37
elif sport == 'Yoga':
    if gender == 'm':
        card_price = 45
    else:
        card_price = 42
elif sport == 'Zumba':
    if gender == 'm':
        card_price = 34
    else:
        card_price = 31
elif sport == 'Dances':
    if gender == 'm':
        card_price = 51
    else:
        card_price = 53
elif sport == 'Pilates':
    if gender == 'm':
        card_price = 39
    else:
        card_price = 27

if age <= 19:
    card_price *= 0.8

if budget >= card_price:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${card_price - budget:.2f} more.')
