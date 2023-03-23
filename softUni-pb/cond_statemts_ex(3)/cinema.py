type_movie = input()
rows = int(input())
cols = int(input())

cinema_capacity = rows * cols
income = 0

if type_movie == 'Premiere':
    income = cinema_capacity * 12
elif type_movie == 'Normal':
    income = cinema_capacity * 7.5
elif type_movie == 'Discount':
    income = cinema_capacity * 5

print(f'{income:.2f} leva')
