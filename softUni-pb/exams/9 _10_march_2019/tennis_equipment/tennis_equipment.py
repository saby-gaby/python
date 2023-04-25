from math import floor, ceil

racket_price = float(input())
rackets_count = int(input())
shoes_count = int(input())

rackets_shoes_costs = rackets_count * racket_price + shoes_count * racket_price / 6
total_costs = rackets_shoes_costs + rackets_shoes_costs * 0.2

print(f'Price to be paid by Djokovic {floor(total_costs / 8)}')
print(f'Price to be paid by sponsors {ceil((total_costs / 8) * 7)}')
