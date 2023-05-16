deco_quantity = int(input())
days_left = int(input())
money_spend = 0
christmas_spirit = 0 if days_left % 10 != 0 else -30

for day in range(1, days_left + 1):
    if day % 11 == 0:
        deco_quantity += 2
    if day % 2 == 0:
        money_spend += deco_quantity * 2
        christmas_spirit += 5
    if day % 3 == 0:
        money_spend += deco_quantity * (5 + 3)
        christmas_spirit += 3 + 10
    if day % 5 == 0:
        money_spend += deco_quantity * 15
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spend += 5 + 3 + 15
print(f'Total cost: {money_spend}')
print(f'Total spirit: {christmas_spirit}')
