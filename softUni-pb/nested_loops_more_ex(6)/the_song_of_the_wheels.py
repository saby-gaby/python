control_num = int(input())

counter = 0
password = ''

for a in range(1, 10):

    for b in range(1, 10):

        if a < b:

            for c in range(1, 10):

                for d in range(1, 10):

                    if c > d and a * b + c * d == control_num:
                        if counter < 4:
                            password = str(a) + str(b) + str(c) + str(d)
                            counter += 1

                        print(f'{str(a)}{str(b)}{str(c)}{str(d)}', end=' ')
if password:
    print()

if counter >= 4:
    print(f'Password: {password}')
else:
    print('No!')
