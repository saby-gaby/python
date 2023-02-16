moves = int(input())
result = 0
very_small, small, middle, high, top, invalid = 0, 0, 0, 0, 0, 0

for _ in range(moves):
    number = int(input())

    if number > 50 or number < 0:
        result /= 2
        invalid += 1
    elif number < 10:
        result += number * 0.2
        very_small += 1
    elif number < 20:
        result += number * 0.3
        small += 1
    elif number < 30:
        result += number * 0.4
        middle += 1
    elif number < 40:
        result += 50
        high += 1
    else:
        result += 100
        top += 1

print(f'{result:.2f}')
print(f'From 0 to 9: {very_small / moves * 100:.2f}%')
print(f'From 10 to 19: {small / moves * 100:.2f}%')
print(f'From 20 to 29: {middle / moves * 100:.2f}%')
print(f'From 30 to 39: {high / moves * 100:.2f}%')
print(f'From 40 to 50: {top / moves * 100:.2f}%')
print(f'Invalid numbers: {invalid / moves * 100:.2f}%')
