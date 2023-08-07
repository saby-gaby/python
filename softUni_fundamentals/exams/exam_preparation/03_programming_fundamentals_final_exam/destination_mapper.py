import re
text = input()
pattern = r'([=/])(?P<dest>[A-Z][a-zA-Z][a-zA-Z]+)\1'
destinations = re.findall(pattern, text)
locations = []
points = 0
for dest in destinations:
    locations.append(dest[1])
    points += len(dest[1])

print(f'Destinations: {", ".join(locations)}')
print(f'Travel Points: {points}')
