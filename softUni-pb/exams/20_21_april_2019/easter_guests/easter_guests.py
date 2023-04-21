from math import ceil

guests = int(input())
budget = int(input())
bread_price = 4
egg_price = 0.45

breads_needed = ceil(guests / 3)
eggs_needed = guests * 2

total_costs = breads_needed * bread_price + eggs_needed * egg_price

if budget >= total_costs:
    print(f'Lyubo bought {breads_needed} Easter bread and {eggs_needed} eggs.')
    print(f'He has {budget - total_costs:.2f} lv. left.')
else:
    print('Lyubo doesn\'t have enough money.')
    print(f'He needs {total_costs - budget:.2f} lv. more.')
