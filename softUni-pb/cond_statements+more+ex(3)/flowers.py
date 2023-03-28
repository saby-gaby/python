chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = chrysanthemums * 2
    roses_price = roses * 4.1
    tulips_price = tulips * 2.5
    bouquet = chrysanthemums_price + roses_price + tulips_price

    if holiday == 'Y':
        bouquet *= 1.15
    if season == 'Spring' and tulips >= 7:
        bouquet *= 0.95
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.5
    tulips_price = tulips * 4.15
    bouquet = chrysanthemums_price + roses_price + tulips_price

    if holiday == 'Y':
        bouquet *= 1.15
    if season == 'Winter' and roses >= 10:
        bouquet *= 0.9

if chrysanthemums + roses + tulips >= 20:
    bouquet *= 0.8

bouquet += 2

print(f'{bouquet:.2f}')
