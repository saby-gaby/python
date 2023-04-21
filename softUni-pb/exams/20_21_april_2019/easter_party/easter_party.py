guests = int(input())
price_person = float(input())
budget = float(input())

cake = budget * 0.1

if 10 <= guests <= 15:
    price_person *= 0.85
elif 15 < guests <= 20:
    price_person *= 0.8
elif guests > 20:
    price_person *= 0.75

costs = guests * price_person + cake

if budget >= costs:
    print(f'It is party time! {budget - costs:.2f} leva left.')
else:
    print(f'No party! {costs - budget:.2f} leva needed.')
