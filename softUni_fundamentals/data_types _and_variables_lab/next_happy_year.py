year = int(input())

while True:
    year += 1
    year_string = str(year)
    set_year = set(year_string)
    if len(set_year) == len(year_string):
        print(year)
        break
