searched_book = input()
book_counter = 0

while True:
    current_book = input()

    if current_book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {book_counter} books.')
        break
    elif current_book == searched_book:
        print(f'You checked {book_counter} books and found it.')
        break
    else:
        book_counter += 1
