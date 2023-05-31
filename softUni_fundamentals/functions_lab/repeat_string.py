# input_string = input()
# count = int(input())
# repeat_string = lambda text, repeat: text * repeat
# print(repeat_string(input_string, count))


input_string = input()
count = int(input())


def repeat_string(text, repeat):
    return text * repeat


print(repeat_string(input_string, count))
