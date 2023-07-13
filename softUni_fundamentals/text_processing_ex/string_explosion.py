string = input()
final_string = ''
strength = 0

for i, char in enumerate(string):
    if strength > 0 and char != '>':
        strength -= 1
    elif char == '>':
        final_string += char
        strength += int(string[i + 1])
    else:
        final_string += char

print(final_string)

"""
tests:
abv>1>1>2>2asdasd -> abv>>>>dasd
pesho>2sis>1a>2akarate>4hexmaster -> pesho>is>a>karate>master
"""