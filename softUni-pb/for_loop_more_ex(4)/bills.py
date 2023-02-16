months = int(input())
water = 0
internet = 0
other = 0
total_electricity = 0

for _ in range(months):
    electricity = float(input())
    total_electricity += electricity
    water += 20
    internet += 15
    other += (electricity + 35) * 1.2

average = (total_electricity + water + internet + other) / months

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
