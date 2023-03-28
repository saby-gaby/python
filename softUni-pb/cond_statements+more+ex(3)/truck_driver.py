season = input()
km_per_month = float(input())
money = 0

if km_per_month <= 5000:
    if season == 'Summer':
        money = 4 * km_per_month * 0.9
    elif season == 'Winter':
        money = 4 * km_per_month * 1.05
    else:
        money = 4 * km_per_month * 0.75
elif km_per_month <= 10000:
    if season == 'Summer':
        money = 4 * km_per_month * 1.1
    elif season == 'Winter':
        money = 4 * km_per_month * 1.25
    else:
        money = 4 * km_per_month * 0.95
elif km_per_month <= 20000:
    money = 4 * km_per_month * 1.45

money *= 0.9

print(f'{money:.2f}')
