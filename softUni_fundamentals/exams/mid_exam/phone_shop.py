def add_phone(storage, phone):
    if phone not in storage:
        storage.append(phone)
    return storage


def remove_phone(storage, phone):
    if phone in storage:
        storage.pop(storage.index(phone))
    return storage


def add_bonus_phone(storage, bonus):
    old_phone, new_phone = bonus.split(':')
    if old_phone in storage:
        storage.insert(storage.index(old_phone) + 1, new_phone)
    return storage


def send_phone_to_the_end(storage, phone):
    if phone in storage:
        storage.append(storage.pop(storage.index(phone)))
    return storage


def phone_shop():
    phones = input().split(', ')

    while True:
        command = input()

        if command == 'End':
            break
        command, item = command.split(' - ')

        if command == 'Add':
            phones = add_phone(phones, item)
        elif command == 'Remove':
            phones = remove_phone(phones, item)
        elif command == 'Bonus phone':
            phones = add_bonus_phone(phones, item)
        elif command == 'Last':
            phones = send_phone_to_the_end(phones, item)

    return ', '.join(phones)

print(phone_shop())