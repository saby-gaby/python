count_numbers = int(input())
is_odd = False

for _ in range(count_numbers):
    current_number = int(input())
    if current_number % 2 != 0:
        is_odd = True
        break
    else:
        continue
if is_odd:
    print(f'{current_number} is odd!')
else:
    print('All numbers are even.')
