def get_characters(start, end):
    characters_list = []
    for number in range(start + 1, end):
        characters_list.append(chr(number))
    return ' '.join(characters_list)


start_char = ord(input())
end_char = ord(input())
print(get_characters(start_char, end_char))
