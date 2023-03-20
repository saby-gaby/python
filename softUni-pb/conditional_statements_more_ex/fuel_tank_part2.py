fuel_type = input().lower()
fuel_quantity = float(input())
discount_card = input().lower()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total = 0.0

if discount_card == 'yes':
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08

if fuel_type == "diesel":
    sum_diesel = fuel_quantity * diesel_price
    if fuel_quantity < 20:
        total = sum_diesel
    elif fuel_quantity <= 25:
        total = sum_diesel * 0.92
    else:
        total = sum_diesel * 0.9
elif fuel_type == 'gasoline':
    sum_gasoline = fuel_quantity * gasoline_price
    if fuel_quantity < 20:
        total = sum_gasoline
    elif fuel_quantity <= 25:
        total = sum_gasoline * 0.92
    else:
        total = sum_gasoline * 0.9
elif fuel_type == "gas":
    sum_gas = fuel_quantity * gas_price
    if fuel_quantity < 20:
        total = sum_gas
    elif fuel_quantity <= 25:
        total = sum_gas * 0.92
    else:
        total = sum_gas * 0.9

print(f'{total:.2f} lv.')
