budget = float(input())
category = input()
people = int(input())

vip_price = 499.99
normal_price = 249.99
tickets_money = 0
tickets_price = 0

if people <= 4:
    tickets_money = budget * 0.25
elif people <= 9:
    tickets_money = budget * 0.4
elif people <= 24:
    tickets_money = budget * 0.5
elif people <= 49:
    tickets_money = budget * 0.6
else:
    tickets_money = budget * 0.75

if category == 'VIP':
    tickets_price = people * vip_price
else:
    tickets_price = people * normal_price

if tickets_money >= tickets_price:
    print(f'Yes! You have {tickets_money - tickets_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {tickets_price - tickets_money:.2f} leva.')
