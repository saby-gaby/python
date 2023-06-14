# remaining_days = int(input())
# m = int(input())
#
# # for num in range(m, n, -1):
# #     if num % n == 0:
# #         print(num)
# #         break
#
# total_spirit = 0 if remaining_days % 10 != 0 else -30
# print(total_spirit)

lst = ['coffee', 'tea', 'water']
print(lst.index('tea'))

is_even = lambda num: num % 2
if is_even(4):
    print('odd')
else:
    print('even')

words = ['kiwi', 'apple']
[print(word) for word in words]

example = [1, 2, 2, 3, 5, 6, 8]
print(*example, sep=', ')
print(f'{*example,}')