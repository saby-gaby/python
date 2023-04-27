stage = input()
ticket_type = input()
ticket_count = int(input())
photo = input()

costs, discount = 0, 0

if stage == 'Quarter final':
    if ticket_type == 'Standard':
        costs = ticket_count * 55.5
    elif ticket_type == 'Premium':
        costs = ticket_count * 105.2
    elif ticket_type == 'VIP':
        costs = ticket_count * 118.9
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        costs = ticket_count * 75.88
    elif ticket_type == 'Premium':
        costs = ticket_count * 125.22
    elif ticket_type == 'VIP':
        costs = ticket_count * 300.4
elif stage == 'Final':
    if ticket_type == 'Standard':
        costs = ticket_count * 110.1
    elif ticket_type == 'Premium':
        costs = ticket_count * 160.66
    elif ticket_type == 'VIP':
        costs = ticket_count * 400

if costs > 4000:
    discount = costs * 0.25
elif costs > 2500:
    discount = costs * 0.1

if photo == 'Y' and costs <= 4000:
    costs += ticket_count * 40

print(f'{costs - discount:.2f}')
