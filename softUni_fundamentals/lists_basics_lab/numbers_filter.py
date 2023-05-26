integers_count = int(input())
integers = [int(input()) for _ in range(integers_count)]
result = []
# for _ in range(integers_count):
#     curr_int = int(input())
#     integers.append(curr_int)
command = input()
for curr_num in integers:
    if (command == 'positive' and curr_num >= 0) or \
            (command == 'negative' and curr_num < 0) or \
            (command == 'even' and curr_num % 2 == 0) or \
            (command == 'odd' and curr_num % 2 != 0):
        result.append(curr_num)
print(result)

