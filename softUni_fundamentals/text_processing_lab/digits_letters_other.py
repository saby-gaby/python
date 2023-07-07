string = input()
numbers = ''
letters = ''
others = ''

for char in string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(f'{numbers}\n{letters}\n{others}')

# test
# Agd#53Dfg^&4F53