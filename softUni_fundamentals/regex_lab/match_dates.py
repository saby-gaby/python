import re

pattern = r'\b(?P<day>\d{2})(?P<sep>[-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    date = match.groupdict()
    print(f'Day: {date["day"]}, Month: {date["month"]}, Year: {date["year"]}')

"""
test:
13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016 -> Day: 13, Month: Jul, Year: 1928
                                                                                Day: 10, Month: Nov, Year: 1934
                                                                                Day: 25, Month: Dec, Year: 1937
"""