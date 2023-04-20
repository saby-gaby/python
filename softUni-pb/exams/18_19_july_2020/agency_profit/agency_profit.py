air_company = input()
adult_tickets = int(input())
kid_tickets = int(input())
net_price_adult = float(input())
service_fee = float(input())

price_kid = net_price_adult * 0.3 + service_fee
price_adult = net_price_adult + service_fee

profit = (adult_tickets * price_adult + kid_tickets * price_kid) * 0.2

print(f'The profit of your agency from {air_company} tickets is {profit:.2f} lv.')
