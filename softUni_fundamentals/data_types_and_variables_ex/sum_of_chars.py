number_of_lines = int(input())
sum_chars = 0

for _ in range(number_of_lines):
    curr_char = input()
    sum_chars += ord(curr_char)

print(f'The sum equals: {sum_chars}')
