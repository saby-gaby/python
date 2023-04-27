country = input()
device = input()

grade = 0

if country == 'Russia':
    if device == 'ribbon':
        grade = 9.100 + 9.400
    elif device == 'hoop':
        grade = 9.300 + 9.800
    elif device == 'rope':
        grade = 9.600 + 9.000
elif country == 'Bulgaria':
    if device == 'ribbon':
        grade = 9.600 + 9.400
    elif device == 'hoop':
        grade = 9.550 + 9.750
    elif device == 'rope':
        grade = 9.500 + 9.400
elif country == 'Italy':
    if device == 'ribbon':
        grade = 9.200 + 9.500
    elif device == 'hoop':
        grade = 9.450 + 9.350
    elif device == 'rope':
        grade = 9.700 + 9.150

print(f'The team of {country} get {grade:.3f} on {device}.')
print(f'{(20 - grade) / 20 * 100:.2f}%')
