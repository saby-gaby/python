words_count = int(input())
synonyms = {}

for _ in range(words_count):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym in synonyms.items():
    print(f'{word} - {", ".join(synonyms[word])}')
