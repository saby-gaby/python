budget = float(input())
season = input()
price = 0

if season == 'Summer':
    location = 'Alaska'
else:
    location = 'Morocco'

if budget <= 1000:
    stay_type = 'Camp'

    if season == 'Summer':
        price = budget * 0.65
    else:
        price = budget * 0.45

elif budget <= 3000:
    stay_type = 'Hut'

    if season == 'Summer':
        price = budget * 0.8
    else:
        price = budget * 0.6

else:
    stay_type = 'Hotel'
    price = budget * 0.9

print(f'{location} - {stay_type} - {price:.2f}')
