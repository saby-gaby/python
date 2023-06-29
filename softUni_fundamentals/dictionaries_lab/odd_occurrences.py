words = input().lower().split()
dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(f'{key}', end=' ')