import re

sentence = input()
pattern = r'(?<=\b_)[a-zA-Z0-9]+\b'
names = re.findall(pattern, sentence)
print(*names, sep=",")

"""
alternative:
mport re

sentence = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
found_names = re.findall(pattern, sentence)
print(','.join(found_names))
"""


"""
tests:
The _id and _age variables are both integers. -> id,age
Calculate the _area of the _perfectRectangle object. -> area,perfectRectangle
__invalidVariable _evenMoreInvalidVariable_ _validVariable -> validVariable
"""