def print_sequence(integer):
    sequence = []
    for _ in range(integer):
        current = sum(sequence[:-4:-1])
        if current == 0:
            sequence.append(1)
        else:
            sequence.append(current)
    return ' '.join(str(num) for num in sequence)


number = int(input())
print(print_sequence(number))
