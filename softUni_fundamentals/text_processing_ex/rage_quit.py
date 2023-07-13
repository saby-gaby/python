user_message = input().upper()
result_message = ''
statistic = []
curr_message = ''
curr_repetition = ''

for i, char in enumerate(user_message):
    if not char.isdigit():
        curr_message += char
    else:
        for j in range(i, len(user_message)):
            if not user_message[j].isdigit():
                break
            curr_repetition += user_message[j]
        result_message += int(curr_repetition) * curr_message
        curr_message = ''
        curr_repetition = ''
    if not char.isdigit() and char not in statistic:
        statistic.append(char)

print(f'Unique symbols used: {len(statistic)}')
print(result_message)

"""
tests:
a3 -> Unique symbols used: 1\nAAA
aSd2&5s@1 -> Unique symbols used: 5\nASDASD&&&&&S@
"""