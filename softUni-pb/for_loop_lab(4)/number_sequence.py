input_count = int(input())

max_number = 0
min_number = 0

for i in range(0, input_count):
    num = int(input())

    if i == 0:
        min_number = num
        max_number = num
    else:
        if max_number < num:
            max_number = num
        if min_number > num:
            min_number = num

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
