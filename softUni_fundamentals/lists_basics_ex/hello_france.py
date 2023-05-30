train_ticket = 150
items = input().split('|')
budget = float(input())
bought_items = []
profit = 0
for item in items:
    type_item, price = item.split('->')
    price = float(price)
    if budget >= price:
        if (type_item == 'Clothes' and 0 < price <= 50) or \
                (type_item == 'Shoes' and 0 < price <= 35) or \
                (type_item == 'Accessories' and 0 < price <= 20.5):
            budget -= price
            profit += price * 0.4
            bought_items.append(price * 1.4)
new_budget = budget + sum(bought_items)
print(" ".join([f"{sell_price:.2f}" for sell_price in bought_items]))
# for item in bought_items:
#     print(f'{item:.2f}', end=' ')
# print()
print(f'Profit: {profit:.2f}')
if new_budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
