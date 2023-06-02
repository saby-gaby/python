def min_max_sum(string):
    numbers_string = string.split()
    sequence_list = [int(num) for num in numbers_string]
    min_num = min(sequence_list)
    max_num = max(sequence_list)
    sum_nums = sum(sequence_list)
    return f'The minimum number is {min_num}\n\
    The maximum number is {max_num}\n\
    The sum number is: {sum_nums}'


print(min_max_sum(input()))
