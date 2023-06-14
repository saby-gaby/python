list_strings = input().split(', ')
numbers_list = [int(num) for num in list_strings]
count_zeros = numbers_list.count(0)
current_count = 0

for i in range(len(numbers_list)):
    if numbers_list[i] != 0:
        numbers_list[current_count] = numbers_list[i]
        current_count += 1

while current_count < len(numbers_list):
    numbers_list[current_count] = 0
    current_count += 1

print(numbers_list)
