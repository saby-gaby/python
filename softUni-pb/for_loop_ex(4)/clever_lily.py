age = int(input())
wm_price = float(input())
toy_price = int(input())
toys = 0
collected_money = 0
money = 10 - 1

for years in range(1, age + 1):
    if years % 2 != 0:
        toys += 1
    else:
        collected_money += money
        money += 10

total_money = collected_money + toys * toy_price
diff = abs(wm_price - total_money)

if total_money >= wm_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
