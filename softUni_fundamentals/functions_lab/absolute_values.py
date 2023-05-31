def absolute_values(integers_list):
    absolute_list = [abs(num) for num in integers_list]
    print(absolute_list)
    # return absolute_list


values_input = input().split()
values_list = [float(num) for num in values_input]
absolute_values(values_list)
