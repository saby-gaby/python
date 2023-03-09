nylon_amount = int(input())
paint_amount = int(input())
thinner_amount = int(input())
working_hours = int(input())

nylon_costs = (nylon_amount + 2) * 1.5
paint_costs = (paint_amount * 1.1) * 14.50
thinner_costs = thinner_amount * 5.00

materials_costs = nylon_costs + paint_costs + thinner_costs + 0.40
worker_hour_costs = materials_costs * 0.3

total_costs = materials_costs + working_hours*worker_hour_costs

print(total_costs)

