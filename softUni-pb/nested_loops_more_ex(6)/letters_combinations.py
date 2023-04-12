first_letter = ord(input())
max_letter = ord(input())
exclude_letter = ord(input())
combinations_count = 0

for first in range(first_letter, max_letter + 1):

    for second in range(first_letter, max_letter + 1):

        for last in range(first_letter, max_letter + 1):

            if first == exclude_letter or second == exclude_letter or last == exclude_letter:
                continue

            combinations_count += 1

            print(f'{chr(first)}{chr(second)}{chr(last)}', end=' ')

print(combinations_count)
