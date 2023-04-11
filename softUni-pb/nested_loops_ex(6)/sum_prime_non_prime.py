sum_prime = 0
sum_non_prime = 0

while True:
    user_input = input()

    if user_input == 'stop':
        break

    number = int(user_input)

    if number < 0:
        print('Number is negative.')
        continue
    else:
        counter = 1

        for num in range(2, number + 1):
            if number % num == 0:
                counter += 1

        if counter > 2:
            sum_non_prime += number
        elif counter == 2:
            sum_prime += number

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
