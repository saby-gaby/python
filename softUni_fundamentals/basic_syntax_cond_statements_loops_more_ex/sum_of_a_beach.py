from re import findall, IGNORECASE

given_string = input()

words_count = len(findall('sand', given_string, IGNORECASE)) + \
              len(findall('water', given_string, IGNORECASE)) + \
              len(findall('fish', given_string, IGNORECASE)) + \
              len(findall('sun', given_string, IGNORECASE))

print(words_count)
