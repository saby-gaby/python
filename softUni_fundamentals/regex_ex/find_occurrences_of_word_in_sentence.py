import re

sentence = input()
searched_word = input()
pattern = r'\b' + searched_word + r'\b'
occurrences = re.findall(pattern, sentence, re.IGNORECASE)
print(len(occurrences))

"""
tests:
The waterfall was so high, that the child couldn't see its peak.
the
-> 2

How do you plan on achieving that? How? How can you even think of that?
how
-> 3

There was one. Therefore I bought it. I wouldn't buy it otherwise.
there
-> 1
"""