input_count = int(input())

odd_sum = 0
even_sum = 0

for i in range(0, input_count):
    num = int(input())

    if i % 2 == 0:
        odd_sum += num
    else:
        even_sum += num

if odd_sum == even_sum:
    print(f'Yes\nSum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print(f'No\nDiff = {diff}')
