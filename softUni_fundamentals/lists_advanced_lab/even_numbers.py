def find_even_nums_indices(nums_list):
    # found = [nums_list.index(num) for num in nums_list if num % 2 == 0]
    found_even_nums_list = map(
        lambda i: i if nums_list[i] % 2 == 0 else None,
        range(len(nums_list))
    )
    index_list = list(filter(lambda x: x is not None, found_even_nums_list))
    print(index_list)

# numbers = list(map(int, input().split(', ')))
numbers = [int(num) for num in input().split(', ')]
find_even_nums_indices(numbers)
