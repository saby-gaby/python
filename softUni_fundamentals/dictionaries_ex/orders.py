order = {}
command = input()

while command != 'buy':
    name, price, qty = command.split()
    if name not in order:
        order[name] = {'price': float(price), 'quantity': int(qty)}
    else:
        order[name]['price'] = float(price)
        order[name]['quantity'] += int(qty)

    command = input()

for product, details in order.items():
    total_cost_item = details["price"] * details["quantity"]
    print(f'{product} -> {total_cost_item:.2f}')
