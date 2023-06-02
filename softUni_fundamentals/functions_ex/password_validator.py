def validate_length(pwd):
    if len(pwd) in range(6, 11):
        return True
    return False


def validate_characters(pwd):
    if pwd.isalnum():
        return True
    return False


def validate_digits(pwd):
    digits_count = len([char for char in pwd if char.isdigit()])
    if digits_count >= 2:
        return True
    return False


def validate_password(pwd):
    message = []
    length_ok = validate_length(pwd)
    characters_ok = validate_characters(pwd)
    digits_ok = validate_digits(pwd)
    if length_ok and characters_ok and digits_ok:
        message.append('Password is valid')
    if not length_ok:
        message.append('Password must be between 6 and 10 characters')
    if not characters_ok:
        message.append('Password must consist only of letters and digits')
    if not digits_ok:
        message.append('Password must have at least 2 digits')
    return '\n'.join(message)


password = input()
print(validate_password(password))
