bag_price = float(input())
weight_bag = float(input())
days_left = int(input())
bags_count = int(input())

if weight_bag < 10:
    bag_price *= 0.2
elif weight_bag <= 20:
    bag_price *= 0.5

if days_left < 7:
    bag_price *= 1.4
elif days_left <= 30:
    bag_price *= 1.15
else:
    bag_price *= 1.1

print(f'The total price of bags is: {bags_count * bag_price:.2f} lv.')
