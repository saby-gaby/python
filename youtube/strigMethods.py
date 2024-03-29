# String Methods
s='hello world'
# Capitalize string
print(s.capitalize(), '-> capitalized')
# Make all uppercase
print(s.upper(), '-> uppercase')
# Make all lower
print(s.lower(), '-> lowercase')
# Swap case
print(s.swapcase(), '-> swap case')
# Get length
print(len(s), '-> length')
# Replace 
print(s.replace('world', 'everyone'), '-> replace')
#Count
sub='h'
print(s.count(sub), '-> count "h"')
#Starts with
print(s.startswith('hello'), '-> starts with "hello"')
# Ends with
print(s.endswith("d"), '-> ends with "d"')
# Split into a list
print(s.split(), '-> split')
# Find position
print(s.find('r'), '-> position of "r"')
# Is all alphanumeric
print(s.isalnum(), "-> all alphanumeric?")
# Is all alphabetic
print(s.isalpha(), '-> all alphabetic?')
# Is all numeric
print(s.isnumeric(), '-> all numeric?')