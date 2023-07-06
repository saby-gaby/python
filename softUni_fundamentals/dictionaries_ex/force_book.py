players_sides = {}
book = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if force_side not in book:
            book[force_side] = []
        if force_user not in players_sides:
            players_sides[force_user]= force_side
            book[force_side].append(force_user)

    else:
        force_user, force_side = command.split(" -> ")
        if force_side not in book:
            book[force_side] = []
        book[force_side].append(force_user)
        if force_user in players_sides:
            old_side = players_sides[force_user]
            book[old_side].remove(force_user)
            players_sides[force_user] = force_side
        else:
            players_sides[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for side, users in book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")

# book = {}
#
# while True:
#     command = input()
#
#     if command == 'Lumpawaroo':
#         break
#     has_user = False
#
#     if ' | ' in command:
#         force_data = command.split(' | ')
#         for users in book.values():
#             if force_data[1] in users:
#                 has_user = True
#                 break
#
#         if not has_user and force_data[0] not in book:
#             book[force_data[0]] = [force_data[1]]
#         elif not has_user:
#             book[force_data[0]].append(force_data[1])
#
#     elif ' -> ' in command:
#         force_data = command.split(' -> ')
#         for users in book.values():
#             if force_data[0] in users:
#                 has_user = True
#                 break
#
#         if has_user and force_data[0] not in book[force_data[1]]:
#             for user in book.values():
#                 if force_data[0] in user:
#                     user.pop(user.index(force_data[0]))
#                     break
#             book[force_data[1]].append(force_data[0])
#         elif not has_user and force_data[1] not in book:
#             book[force_data[1]] = [force_data[0]]
#         elif not has_user:
#             book[force_data[1]].append(force_data[0])
#         print(f'{force_data[0]} joins the {force_data[1]} side!')
#
# for side, users in book.items():
#     if users:
#         print(f'Side: {side}, Members: {len(users)}')
#         for user in users:
#             print(f'! {user}')

#
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
#
# 90/100 -> runtime error
