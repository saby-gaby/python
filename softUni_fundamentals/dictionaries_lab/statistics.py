stock = {}
while True:
    incoming_product = input()
    if incoming_product == 'statistics':
        break
    product, quantity = incoming_product.split(': ')
    quantity = int(quantity)
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

print('Products in stock:')
for stock_item, qty in stock.items():
    print(f'- {stock_item}: {qty}')
print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')