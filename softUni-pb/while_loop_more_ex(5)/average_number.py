count = int(input())
num_sum = 0

for _ in range(count):
    num_sum += int(input())

print(f'{num_sum / count:.2f}')
