def length_validation(user_name):
    if 3 <= len(user_name) <= 16:
        return True
    return False


def char_validation(user_name):
    for char in user_name:
        if not char.isalnum() and char != '-' and char != '_':
            return False
    return True


def no_redundant_symbols(user_name):
    if ' ' in user_name:
        return False
    return True

def username_is_valid(user_name):
    if all([length_validation(user_name), char_validation(user_name), no_redundant_symbols(user_name)]):
        return True
    return False


usernames = input().split(', ')

for username in usernames:
    if username_is_valid(username):
        print(username)


"""
usernames = input().split(', ')

for username in usernames:
    if 3 <= len(username) <= 16:
        if username.isalnum():
            print(username)
        if '-' in username:
            parts = username.split('-')
            is_valid = True
            for part in parts:
                if not part.isalnum():
                    is_valid = False
                    break
            if is_valid:
                print(username)
        if '_' in username:
            parts = username.split('_')
            is_valid = True
            for part in parts:
                if not part.isalnum():
                    is_valid = False
                    break
            if is_valid:
                print(username)
"""

"""
tests:
sh, too_long_username, !lleg@l ch@rs, jeffbutt -> jeffbutt
Jeff, john45, ab, cd, peter-ivanov, @smith -> Jeff\n john45\npeter-ivanov
"""