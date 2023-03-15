# print(1 + '2')  # => error

a = 5
b = 10

print(b == 2 * a)

a = 'Example'
b = 'Example'

print(a == b)

b = a

print(a == b)

# Format
price = 2.855148
product = 'Cola'

print('The price of {} is {:.2f}'.format(product, price))

number = int(input('Give me a number: '))

number *= 2
number += 10
number -= 5
number //= 2

if number > 6:
    print("Hello")
else:
    print('Bye')

# Debugging
# f8 -> step forward
# f9 -> to next breakpoint

number = 44

if number > 40:
    print('Greater than 40')    # is_true => after this if breaks the check
elif number > 30:
    print('Greater than 40')
elif number > 20:
    print('Greater than 20')
else:
    print('Small number')

if number > 30:
    print('Greater than 30')

print('Finish')
