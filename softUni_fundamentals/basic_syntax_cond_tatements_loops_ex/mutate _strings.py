first_string = input()
second_string = input()

for char in range(len(first_string)):
    if first_string[char] == second_string[char]:
        continue
    else:
        print(second_string[:char + 1] + first_string[char + 1:])
