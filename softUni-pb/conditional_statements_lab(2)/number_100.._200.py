number = int(input())

if number < 100:
    print('Less than 100')
elif 200 >= number >= 100:      # number >= 100 and number <= 200
    print('Between 100 and 200')
else:
    print('Greater than 200')
