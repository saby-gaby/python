countries = input().split(', ')
capitals = input().split(', ')

# res_dict = {country: capitals[i] for i, country in enumerate(countries)}
res_dict = dict(zip(countries, capitals))

for country, capital in res_dict.items():
    print(f'{country} -> {capital}')
