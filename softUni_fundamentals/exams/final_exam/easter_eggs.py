import re

text_string = input()

pattern = r'[@#]+([a-z]{3,})[@#]+[\W_]*/+(\d+)/+'

valid_combinations = re.findall(pattern, text_string)

for combination in valid_combinations:
    print(f'You found {combination[1]} {combination[0]} eggs!')
