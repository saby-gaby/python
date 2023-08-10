import re

text = input()
pattern = r'([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
found = re.findall(pattern, text)
mirror_words = []
if found:
    print(f'{len(found)} word pairs found!')
    for pair in found:
        if pair[1] == pair[2][::-1]:
            mirror_words.append(f'{pair[1]} <=> {pair[2]}')
else:
    print('No word pairs found!')
if mirror_words:
    print('The mirror words are:')
    print(*mirror_words, sep=', ')
else:
    print('No mirror words!')
