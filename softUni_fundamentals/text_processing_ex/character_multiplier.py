def multiply(res, first_str, second_str):
    for i in range(len(first_str)):
        res += ord(first_str[i]) * ord(second_str[i])
    return res


def add_rest(res, string):
    for character in string:
        res += ord(character)
    return res


first, second = input().split()
len_first = len(first)
len_second = len(second)
result = 0

if len_first == len_second:
    result = multiply(result, first, second)
elif len_first > len_second:
    result = multiply(result, first[:len_second], second)
    result = add_rest(result, first[len_second:])
else:
    result = multiply(result, first, second[:len_first])
    result = add_rest(result, second[len_first:])

print(result)

"""
tests:
George Peter -> 52114
123 522 -> 7647
a aaa -> 9700
"""