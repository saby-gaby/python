kilometers = int(input())
day_night = input()

if kilometers < 20 and day_night == "day":
    print(f'{kilometers * 0.79 + 0.7:.2f}')
elif kilometers < 20 and day_night == "night":
    print(f'{kilometers * 0.9 + 0.7:.2f}')
elif kilometers < 100:
    print(f'{kilometers * 0.09:.2f}')
else:
    print(f'{kilometers * 0.06:.2f}')
