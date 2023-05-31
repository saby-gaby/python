def calculate_bill(item_type, qty):
    if item_type == 'coffee':
        return f'{qty * 1.5:.2f}'
    elif item_type == 'coke':
        return f'{qty * 1.4:.2f}'
    elif item_type == 'water':
        return f'{qty:.2f}'
    elif item_type == 'snacks':
        return f'{qty * 2:.2f}'


product = input()
quantity = int(input())
print(calculate_bill(product, quantity))
