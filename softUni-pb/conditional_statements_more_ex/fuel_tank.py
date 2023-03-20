fuel_type = input().lower()
fuel_quantity = float(input())

if fuel_type == 'diesel':
    if fuel_quantity >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
elif fuel_type == 'gasoline':
    if fuel_quantity >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
elif fuel_type == 'gas':
    if fuel_quantity >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
else:
    print('Invalid fuel!')
