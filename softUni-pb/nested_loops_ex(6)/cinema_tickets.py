standard, student, kid, projection = 0, 0, 0, 0

while True:
    film = input()

    if film == 'Finish':
        break

    capacity = int(input())

    while projection < capacity:
        type_ticket = input()

        if type_ticket == 'End':
            break
        elif type_ticket == 'standard':
            standard += 1
        elif type_ticket == 'student':
            student += 1
        elif type_ticket == 'kid':
            kid += 1
        projection += 1
    print(f'{film} - {projection / capacity * 100:.2f}% full.')
    projection = 0
total_tickets = standard + student + kid

print(f'Total tickets: {total_tickets}')
print(f'{student / total_tickets * 100:.2f}% student tickets.')
print(f'{standard / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid / total_tickets * 100:.2f}% kids tickets.')
