def word_decipher(word):
    first_letter_number = ''.join([char for char in word if char.isdigit()])
    deciphered_list = list(chr(int(first_letter_number)) + word.replace(first_letter_number, ''))
    deciphered_list[1],deciphered_list[-1] = deciphered_list[-1],deciphered_list[1]
    deciphered_word = ''.join(deciphered_list)
    return deciphered_word


secret_message = input().split()
deciphered_secret_message = list(map(word_decipher, secret_message))
print(' '.join(deciphered_secret_message))
