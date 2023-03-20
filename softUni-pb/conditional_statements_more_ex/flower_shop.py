from math import ceil, floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
present_price = float(input())

magnolias_price = 3.25 * magnolias
hyacinths_price = 4 * hyacinths
roses_price = 3.5 * roses
cacti_price = 8 * cacti

order_sum = magnolias_price + hyacinths_price + roses_price + cacti_price
total_order = order_sum * 0.95

diff = total_order - present_price

if present_price <= total_order:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(abs(diff))} leva.')
