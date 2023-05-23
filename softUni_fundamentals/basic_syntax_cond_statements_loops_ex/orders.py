orders_count = int(input())
total_price = 0

for _ in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    daily_needed_capsules = int(input())

    if not 0.01 <= capsule_price <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= daily_needed_capsules <= 2000:
        continue

    price = capsule_price * days * daily_needed_capsules
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')
