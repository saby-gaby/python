pocket_money = float(input())
daily_profit = float(input())
costs = float(input())
present_price = float(input())

saved_money = 5 * pocket_money + 5 * daily_profit - costs

if saved_money >= present_price:
    print(f'Profit: {saved_money:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {present_price - saved_money:.2f} BGN.')