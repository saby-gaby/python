foods_list = input().split()
foods = {}

for i in range(0, len(foods_list), 2):
    foods[foods_list[i]] = int(foods_list[i + 1])

print(foods)