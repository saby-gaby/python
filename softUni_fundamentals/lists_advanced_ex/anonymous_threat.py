def merge_divide_str(strings):
    while True:
        command = input().split()

        if command[0] == '3:1':
            break
        elif command[0] == 'merge':
            start_index = int(command[1])
            end_index = int(command[2])
            if start_index < 0:
                start_index = 0
            if end_index > len(strings) - 1:
                end_index = len(strings) - 1
            if start_index >= len(strings) - 1:
                continue
            strings = strings[:start_index:] + \
                      [''.join(strings[start_index:end_index + 1])] + \
                      strings[end_index + 1::]
        elif command[0] == 'divide':
            index = int(command[1])
            partitions = int(command[2])
            divided_word = []
            word = strings[index]
            step = len(word) // partitions
            for i in range(0, len(word), step):
                divided_word.append(word[i:i+step:])
            if len(word) % partitions != 0:
                divided_word[-2] = divided_word[-2] + divided_word[-1]
                divided_word.pop()
            strings = strings[:index] + divided_word + strings[index + 1:]
    print(' '.join(strings))

strings_input = input().split()
merge_divide_str(strings_input)

# Merge by start_index < 0 /and end_index < 0
# def merge_divide_str(strings):
#     while True:
#         command = input().split()
#
#         if command[0] == '3:1':
#             break
#         elif command[0] == 'merge':
#             start_index = int(command[1])
#             end_index = int(command[2])
#             if start_index < 0:
#                 start_index += len(strings)
#             if end_index < 0:
#                 end_index += len(strings)
#             if start_index >= len(strings) - 1 or abs(start_index) > len(strings):
#                 continue
#             if start_index in range(len(strings)) and end_index in range(len(strings)):
#                 strings = strings[:start_index:] + \
#                           [''.join(strings[start_index:end_index + 1])] + \
#                           strings[end_index + 1::]
#             elif end_index > len(strings) - 1:
#                 strings = strings[:start_index:] + \
#                           [''.join(strings[start_index::])]
#         elif command[0] == 'divide':
#             index = int(command[1])
#             partitions = int(command[2])
#             divided_word = []
#             word = strings[index]
#             step = len(word) // partitions
#             for i in range(0, len(word), step):
#                 divided_word.append(word[i:i+step:])
#             if len(word) % partitions != 0:
#                 divided_word[-2] = divided_word[-2] + divided_word[-1]
#                 divided_word.pop()
#             strings = strings[:index] + divided_word + strings[index + 1:]
#     print(' '.join(strings))
#
# strings_input = input().split()
# merge_divide_str(strings_input)

# sample - solution
# strings_input = input().split()
# result = []
# instructions = input()
# while not instructions == "3:1":
#     instructions = instructions.split()
#     command = instructions[0]
#     if command == 'merge':
#         start = int(instructions[1])
#         end = int(instructions[2])
#         if start < 0:
#             start = 0
#         if end > len(strings_input) - 1:
#             end = len(strings_input) - 1
#         for index, string in enumerate(strings_input):
#             if index in range(start + 1, end + 1):
#                 strings_input[start] += strings_input[index]
#         for index in range(end, start, - 1):
#             strings_input.pop(index)
#     elif command == 'divide':
#         index = int(instructions[1])
#         partitions = int(instructions[2])
#         if partitions > len(strings_input[index]):
#             step = 1
#         else:
#             step = len(strings_input[index]) // partitions
#         divide_part = strings_input.pop(index)
#         start = 0
#         for parts in range(partitions):
#             if parts == partitions - 1:
#                 strings_input.insert(index, divide_part[start::])
#                 break
#             else:
#                 strings_input.insert(index, divide_part[start: start + step:])
#             start += step
#             index += 1
#     instructions = input()
# print(' '.join(strings_input))
