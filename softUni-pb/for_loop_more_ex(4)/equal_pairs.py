count = int(input())
sum_num = 0
prev_sum = 0
diff = 0

for _ in range(count):
    num1 = int(input())
    num2 = int(input())

    sum_num = num1 + num2

    if prev_sum == 0:
        prev_sum = sum_num
    elif prev_sum != sum_num:
        curr_diff = abs(prev_sum - sum_num)
        if curr_diff > diff:
            diff = curr_diff
    prev_sum = sum_num

if not diff:
    print(f'Yes, value={sum_num}')
else:
    print(f'No, maxdiff={diff}')
