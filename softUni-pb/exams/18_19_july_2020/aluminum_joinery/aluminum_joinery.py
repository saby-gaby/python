joinery_count = int(input())
size_joinery = input()
delivery = input()

single_price = 0

if joinery_count < 10:
    print('Invalid order')
else:
    if size_joinery == '90X130':
        single_price = 110

        if 30 < joinery_count <= 60:
            single_price *= 0.95
        elif joinery_count > 60:
            single_price *= 0.92

    elif size_joinery == '100X150':
        single_price = 140

        if 40 < joinery_count <= 80:
            single_price *= 0.94
        elif joinery_count > 80:
            single_price *= 0.9

    elif size_joinery == '130X180':
        single_price = 190

        if 20 < joinery_count <= 50:
            single_price *= 0.93
        elif joinery_count > 50:
            single_price *= 0.88

    elif size_joinery == '200X300':
        single_price = 250

        if 25 < joinery_count <= 50:
            single_price *= 0.91
        elif joinery_count > 50:
            single_price *= 0.86

    total_price = joinery_count * single_price

    if delivery == 'With delivery':
        total_price += 60

    if joinery_count > 99:
        total_price *= 0.96

    print(f'{total_price:.2f} BGN')
