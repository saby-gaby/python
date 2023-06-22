def memory_game(elements):
    moves_counter = 0
    while elements:
        user_input = input()
        if user_input == 'end':
            break
        index_1, index_2 = [int(index) for index in user_input.split()]
        moves_counter += 1
        if index_1 == index_2 or (
                index_1 not in range(len(elements)) or index_2 not in range(len(elements))):
            middle_of_seq_index = int(len(elements) / 2)
            elements.insert(middle_of_seq_index, f'-{moves_counter}a')
            elements.insert(middle_of_seq_index, f'-{moves_counter}a')
            print('Invalid input! Adding additional elements to the board')
            continue
        if elements[index_1] == elements[index_2]:
            element = elements[index_1]
            print(f'Congrats! You have found matching elements - {element}!')
            elements.remove(element)
            elements.remove(element)
        else:
            print('Try again!')

    if elements:
        print(f'Sorry you lose :(\n{" ".join(elements)}')
    else:
        print(f'You have won in {moves_counter} turns!')


elements_seq = input().split()
memory_game(elements_seq)
