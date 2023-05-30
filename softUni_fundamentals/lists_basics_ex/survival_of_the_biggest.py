integers_as_strings = input().split()
nums_to_remove = int(input())
integers_as_nums = [int(num) for num in integers_as_strings]
integers_as_nums.sort()
integers_as_nums = integers_as_nums[:nums_to_remove]
result_lst = []
for char in integers_as_strings:
    if int(char) not in integers_as_nums:
        result_lst.append(char)
print(', '.join(result_lst))
