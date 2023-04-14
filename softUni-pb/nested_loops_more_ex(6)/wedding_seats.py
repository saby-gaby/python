end_sector = ord(input())
rows_sect = int(input())
odd_rows_seats = int(input())
even_rows_seats = odd_rows_seats + 2

start_sect = 65
start_seats = 97
seats_counter = 0

for sector in range(start_sect, end_sector + 1):

    for row in range(1, rows_sect + 1):

        if row % 2 == 0:

            for seat in range(start_seats, start_seats + even_rows_seats):
                seats_counter += 1
                print(chr(sector) + str(row) + chr(seat))
        else:

            for seat in range(start_seats, start_seats + odd_rows_seats):
                seats_counter += 1
                print(chr(sector) + str(row) + chr(seat))

    rows_sect += 1

print(seats_counter)
