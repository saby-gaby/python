deposit = float(input())
period = int(input())
interest_rate = float(input())

month_rate = deposit * interest_rate / 100 / 12
final_amount = deposit + period * month_rate

print(final_amount)
