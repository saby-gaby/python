amounts = input().split(', ')
beggars = int(input())
result_lst = []
for beggar in range(beggars):
    sum_collected = 0
    for i in range(beggar, len(amounts), beggars):
        sum_collected += int(amounts[i])
    result_lst.append(sum_collected)
print(result_lst)
