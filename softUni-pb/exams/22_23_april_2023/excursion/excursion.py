people_count = int(input())
nights_count = int(input())
transport_cards_count = int(input())
museum_tickets = int(input())

costs = people_count * (nights_count * 20 + transport_cards_count * 1.6 + museum_tickets * 6)

total_costs = costs * 1.25

print(f'{total_costs:.2f}')
