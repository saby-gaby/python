budget = float(input())
season = input()
car_class = ''
car = ''
car_price = 0

if budget <= 100:
    car_class = 'Economy class'

    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.35
    else:
        car = 'Jeep'
        car_price = budget * 0.65
elif budget <= 500:
    car_class = 'Compact class'

    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.45
    else:
        car = 'Jeep'
        car_price = budget * 0.8
else:
    car_class = 'Luxury class'
    car = 'Jeep'
    car_price = budget * 0.9

print(f'{car_class}\n{car} - {car_price:.2f}')
