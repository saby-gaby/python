vacation_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_price = 4.10
minion_price = 8.20
truck_price = 2

toys_count = puzzle_count + doll_count + teddy_count + minion_count + truck_count
toy_costs = \
    puzzle_count * puzzle_price + \
    doll_count * doll_price + \
    teddy_count * teddy_price + \
    minion_count * minion_price + \
    truck_count * truck_price

if toys_count >= 50:
    toy_costs *= 0.75

toy_costs *= 0.9   # Rent 10%

diff = abs(toy_costs - vacation_price)

if toy_costs >= vacation_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
