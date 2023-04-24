people_count = int(input())
season = input()

price_per_person = 0

if people_count <= 5:
    if season == 'spring':
        price_per_person = 50
    elif season == 'summer':
        price_per_person = 48.5 * 0.85
    elif season == 'autumn':
        price_per_person = 60
    elif season == 'winter':
        price_per_person = 86 * 1.08
else:
    if season == 'spring':
        price_per_person = 48
    elif season == 'summer':
        price_per_person = 45 * 0.85
    elif season == 'autumn':
        price_per_person = 49.5
    elif season == 'winter':
        price_per_person = 85 * 1.08

print(f'{people_count * price_per_person:.2f} leva.')
