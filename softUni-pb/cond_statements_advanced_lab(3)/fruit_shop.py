fruit = input()
day = input()
quantity = float(input())
result = ""

if day == 'Monday' \
        or day == 'Tuesday' \
        or day == 'Wednesday' \
        or day == 'Thursday' \
        or day == 'Friday':
    if fruit == 'banana':
        result = quantity * 2.5
    elif fruit == 'apple':
        result = quantity * 1.2
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.7
    elif fruit == 'pineapple':
        result = quantity * 5.5
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        result = 'error'
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        result = quantity * 2.7
    elif fruit == 'apple':
        result = quantity * 1.25
    elif fruit == 'orange':
        result = quantity * 0.9
    elif fruit == 'grapefruit':
        result = quantity * 1.6
    elif fruit == 'kiwi':
        result = quantity * 3
    elif fruit == 'pineapple':
        result = quantity * 5.6
    elif fruit == 'grapes':
        result = quantity * 4.2
    else:
        result = 'error'
else:
    result = 'error'

if type(result) == float:
    print(f'{result:.2f}')
else:
    print(result)
