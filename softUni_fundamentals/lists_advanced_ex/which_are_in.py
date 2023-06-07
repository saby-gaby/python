def find_in_words(first, second):
    found = [first_word for first_word in first if \
             any(first_word in second_word for second_word in second)]
    return found


first_sequence = input().split(', ')
second_sequence = input().split(', ')
print(find_in_words(first_sequence,second_sequence))
