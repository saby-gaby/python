product = input()
city = input()
quantity = float(input())
total = 0

if city == 'Sofia':
    if product == 'coffee':
        total = quantity * 0.5
    elif product == 'water':
        total = quantity * 0.8
    elif product == 'beer':
        total = quantity * 1.2
    elif product == 'sweets':
        total = quantity * 1.45
    else:
        total = quantity * 1.6
elif city == 'Plovdiv':
    if product == 'coffee':
        total = quantity * 0.4
    elif product == 'water':
        total = quantity * 0.7
    elif product == 'beer':
        total = quantity * 1.15
    elif product == 'sweets':
        total = quantity * 1.3
    else:
        total = quantity * 1.5
else:
    if product == 'coffee':
        total = quantity * 0.45
    elif product == 'water':
        total = quantity * 0.7
    elif product == 'beer':
        total = quantity * 1.1
    elif product == 'sweets':
        total = quantity * 1.35
    else:
        total = quantity * 1.55

print(total)
