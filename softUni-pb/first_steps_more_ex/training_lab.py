w = float(input()) * 100
h = float(input()) * 100

working_seats_w = w // 120
working_seats_h = (h - 100) // 70

total_working_seats = working_seats_w * working_seats_h - 3

print(int(total_working_seats))
