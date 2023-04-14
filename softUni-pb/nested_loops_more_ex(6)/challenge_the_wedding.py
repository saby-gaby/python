men = int(input())
women = int(input())
tables = int(input())
table_counter = 0

for men_seat in range(1, men + 1):

    for women_seat in range(1, women + 1):
        table_counter += 1

        if table_counter > tables:
            break

        print(f'({men_seat} <-> {women_seat})', end=' ')
