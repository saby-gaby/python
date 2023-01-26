money = float(input())
year_to_live = int(input())
age = 18
money_needed = 0

for year in range(1800, year_to_live + 1):
    money_needed += 12000

    if year % 2 != 0:
        money_needed += age * 50

    age += 1

diff = abs(money_needed - money)

if money >= money_needed:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')
