text_input = input()
result = ''

for i in range(len(text_input)):
    if i + 1 < len(text_input):
        if text_input[i] != text_input[i + 1]:
            result += text_input[i]
result += text_input[-1]

print(result)


"""
tests:
aaaaabbbbbcdddeeeedssaa -> abcdedsa
qqqwerqwecccwd -> qwerqwecwd
"""