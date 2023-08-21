import re
text = input()
cool_threshold = 1
cool_emojis = []

pattern = r'([*]{2}|[:]{2})([A-Z][a-z]{2,})(\1)'
emojis = re.findall(pattern, text)

for char in text:
    if char.isdigit():
        cool_threshold *= int(char)
if emojis:
    for emoji in emojis:
        coolness = 0
        for char in emoji[1]:
            coolness += ord(char)
        if coolness > cool_threshold:
            cool_emojis.append(emoji)
print(f'Cool threshold: {cool_threshold}')
if emojis:
    print(f'{len(emojis)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(*emoji, sep='')
