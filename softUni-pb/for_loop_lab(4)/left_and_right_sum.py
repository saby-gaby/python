input_count = int(input())

sum_left = 0
sum_right = 0

for i in range(0, input_count):
    num = int(input())
    sum_left += num

for i in range(0, input_count):
    num = int(input())
    sum_right += num

if sum_left == sum_right:
    print(f'Yes, sum = {sum_right}')
else:
    diff = abs(sum_right - sum_left)
    print(f'No, diff = {diff}')
