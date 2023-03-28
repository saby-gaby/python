junior_bikers = int(input())
senior_bikers = int(input())
route = input()
charity_sum = 0

if route == 'trail':
    charity_sum = junior_bikers * 5.5 + senior_bikers * 7
elif route == 'cross-country':
    charity_sum = junior_bikers * 8 + senior_bikers * 9.5

    if junior_bikers + senior_bikers >= 50:
        charity_sum = charity_sum * 0.75
elif route == 'downhill':
    charity_sum = junior_bikers * 12.25 + senior_bikers * 13.75
elif route == 'road':
    charity_sum = junior_bikers * 20 + senior_bikers * 21.5

charity_sum *= 0.95

print(f'{charity_sum:.2f}')
