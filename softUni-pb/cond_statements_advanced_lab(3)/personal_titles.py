age = float(input())
gender = input().lower()

address = ''

if gender == 'f':
    if age >= 16:
        address = 'Ms.'
    elif 0 <= age < 16:
        address = 'Miss'
elif gender == 'm':
    if age >= 16:
        address = 'Mr.'
    elif 0 <= age < 16:
        address = 'Master'

print(address)
