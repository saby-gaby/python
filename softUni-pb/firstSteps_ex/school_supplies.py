pen_packs = int(input())
marker_packs = int(input())
detergent = int(input())
discount = int(input()) / 100

pen_costs = pen_packs * 5.8
marker_costs = marker_packs * 7.2
detergent_costs = detergent * 1.2
sum_costs = pen_costs + marker_costs + detergent_costs

# total = sum_costs * ((100 - discount)/100)
total = sum_costs - sum_costs * discount

print(total)
