budget = float(input())
extras_count = int(input())
clothing_price = float(input())

decor_price = budget * 0.1

if extras_count > 150:
    clothing_price *= 0.9

total_costs = decor_price + extras_count * clothing_price
diff = abs(budget - total_costs)

if budget >= total_costs:
    print(f'Action!\nWingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!\nWingard needs {diff:.2f} leva more.')
