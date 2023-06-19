from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

flour_costs = (students - students // 5) * flour_price
egg_costs = students * egg_price * 10
apron_costs = ceil(students * 1.2) * apron_price

total_costs = flour_costs + egg_costs + apron_costs

if total_costs <= budget:
    print(f'Items purchased for {total_costs:.2f}$.')
else:
    print(f'{total_costs - budget:.2f}$ more needed.')