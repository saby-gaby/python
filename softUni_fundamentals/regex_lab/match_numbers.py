import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
user_input = input()
matches = list(re.finditer(pattern, user_input))
# matches = re.finditer(pattern, user_input)
for match in matches:
    print(match.group(), end=' ')