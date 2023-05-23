string = input()
result_list = []

for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        result_list.append(i)
    else:
        continue
print(result_list)
