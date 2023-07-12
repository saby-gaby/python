text = input()

for i in range(len(text)):
    if text[i] == ':':
        print(text[i] + text[i + 1])

# result = [print(':' + text_input[i][0]) for i in range(1, len(text_input))]

# for i in range(1, len(text_input)):
#     print(':' + text_input[i][0])

"""
test:
There are so many emoticons nowadays :P. I have many ideas :O what input to place here :) -> :P\n:O\n:)
"""

