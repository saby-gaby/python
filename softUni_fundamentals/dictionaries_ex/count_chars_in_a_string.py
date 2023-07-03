text = [char for char in input() if char != " "]
dict_text = dict.fromkeys(text, 0)
for char in text:
    dict_text[char] += 1
for char, occurrences in dict_text.items():
    print(f'{char} -> {occurrences}')
