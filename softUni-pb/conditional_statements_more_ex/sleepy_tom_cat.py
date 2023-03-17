days_off = int(input())

norm_per_year = 30000
regular_days_play_time = 63
off_days_play_time = 127

total_regular_days_play_time = (365 - days_off) * regular_days_play_time
total_off_days_play_time = days_off * off_days_play_time
total_play_time = total_regular_days_play_time + total_off_days_play_time

diff = norm_per_year - total_play_time
hours = abs(diff) // 60
mins = abs(diff) % 60

if diff >= 0:
    print(f'Tom sleeps well\n{hours} hours and {mins} minutes less for play')
else:
    print(f'Tom will run away\n{hours} hours and {mins} minutes more for play')
