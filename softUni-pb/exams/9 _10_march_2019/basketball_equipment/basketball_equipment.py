training_fee = int(input())

shoes = training_fee * 0.6
clothes = shoes * 0.8
ball = clothes / 4
accessories = ball / 5

total_costs = training_fee + shoes + clothes + ball + accessories

print(format(total_costs, '.2f'))
