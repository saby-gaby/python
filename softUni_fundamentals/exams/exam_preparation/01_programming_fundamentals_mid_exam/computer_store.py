price = 0
while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    item_price = float(command)
    if item_price < 0:
        print('Invalid price!')
        continue
    else:
        price += item_price

if price == 0:
    print('Invalid order!')
else:
    total_price = price * 1.2
    taxes = total_price - price
    if command == 'special':
        total_price *= 0.9
    print(f'Congratulations you\'ve just bought a new computer!\n\
    Price without taxes: {price:.2f}$\n\
    Taxes: {taxes:.2f}$\n\
    -----------\n\
    Total price: {total_price:.2f}$')
