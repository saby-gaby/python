def sort_numbers(string):
    numbers_list = [int(num) for num in list_str]
    return sorted(numbers_list)    # reversed -> return sorted(numbers_list, reverse=True)


list_str = input().split()
print(sort_numbers(list_str))
