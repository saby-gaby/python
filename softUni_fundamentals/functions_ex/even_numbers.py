def filter_even_nums(num):
    return num % 2 == 0


numbers_as_str = input().split()
numbers_list = [int(num) for num in numbers_as_str]
filtered_list = list(filter(filter_even_nums, numbers_list))
print(filtered_list)


# numbers_as_str = input().split()
# numbers_list = [int(num) for num in numbers_as_str]
# filter_even = lambda x: x % 2 == 0
# filtered_list = list(filter(filter_even, numbers_list))
# print(filtered_list)
