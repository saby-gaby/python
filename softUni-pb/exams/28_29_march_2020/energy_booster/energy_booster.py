fruit = input()
size = input()
count_ordered = int(input())

total = 0

if fruit == 'Watermelon':
    if size == 'small':
        total = count_ordered * (2 * 56)
    elif size == 'big':
        total = count_ordered * (5 * 28.7)
elif fruit == 'Mango':
    if size == 'small':
        total = count_ordered * (2 * 36.66)
    elif size == 'big':
        total = count_ordered * (5 * 19.6)
elif fruit == 'Pineapple':
    if size == 'small':
        total = count_ordered * (2 * 42.1)
    elif size == 'big':
        total = count_ordered * (5 * 24.8)
elif fruit == 'Raspberry':
    if size == 'small':
        total = count_ordered * (2 * 20)
    elif size == 'big':
        total = count_ordered * (5 * 15.2)

if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5

print(f'{total:.2f} lv.')
