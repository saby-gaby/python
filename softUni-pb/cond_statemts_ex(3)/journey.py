budget = float(input())
season = input()
destination = None
vacation_type = None
spent = 0

if 0 <= budget <= 100:
    destination = 'Bulgaria'

    if season == 'summer':
        vacation_type = 'Camp'
        spent = budget * 0.3
    else:
        vacation_type = 'Hotel'
        spent = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'

    if season == 'summer':
        vacation_type = 'Camp'
        spent = budget * 0.4
    else:
        vacation_type = 'Hotel'
        spent = budget * 0.8
else:
    destination = 'Europe'
    vacation_type = 'Hotel'
    spent = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{vacation_type} - {spent:.2f}')
