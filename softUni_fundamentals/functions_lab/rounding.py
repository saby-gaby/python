def rounding(nums_list):
    return [round(num) for num in nums_list]


input_as_str = input().split()
values_list = [float(num) for num in input_as_str]
print(rounding(values_list))
