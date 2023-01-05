input_count = int(input())
highest_num = 0
sum_numbers = 0

for _ in range(0, input_count):  # _ когато не използваме брояча (i) за нищо
    num = int(input())

    if highest_num == 0:
        highest_num = num
    elif num > highest_num:
        sum_numbers += highest_num
        highest_num = num
    else:
        sum_numbers += num

if highest_num == sum_numbers:
    print(f'Yes\nSum = {sum_numbers}')
else:
    print(f'No\nDiff = {abs(highest_num - sum_numbers)}')
