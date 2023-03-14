degrees = float(input())

if degrees >= 26:
    if degrees <= 35:
        print('Hot')
    else:
        print('unknown')
elif degrees >= 20.1:
    if degrees <= 25.9:
        print('Warm')
    else:
        print('unknown')
elif degrees >= 15:
    if degrees <= 20:
        print('Mild')
    else:
        print('unknown')
elif degrees >= 12:
    if degrees <= 14.9:
        print('Cool')
    else:
        print('unknown')
elif degrees >= 5:
    if degrees <= 11.9:
        print('Cold')
    else:
        print('unknown')
else:
    print('unknown')
