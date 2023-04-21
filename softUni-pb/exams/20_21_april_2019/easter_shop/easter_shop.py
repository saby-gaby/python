available_qty = int(input())
is_closed = False
sold = 0

while True:
    action = input()

    if action == 'Close':
        is_closed = True
        break

    egg_count = int(input())

    if action == 'Buy':
        if available_qty >= egg_count:
            available_qty -= egg_count
            sold += egg_count
        else:
            break

    elif action == 'Fill':
        available_qty += egg_count

if is_closed:
    print('Store is closed!')
    print(f'{sold} eggs sold.')
else:
    print('Not enough eggs in store!')
    print(f'You can buy only {available_qty}.')
