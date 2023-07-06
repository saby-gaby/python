strings = input().split()

print(''.join([len(word) * word for word in strings]))

# tests
# hi abc add
# work
# ball