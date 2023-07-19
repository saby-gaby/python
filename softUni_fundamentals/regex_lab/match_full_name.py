import re
text = input()
pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'

matches = re.findall(pattern, text)
print(*matches)

"""
test:
Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett -> Peter Smith Lily Everett
"""