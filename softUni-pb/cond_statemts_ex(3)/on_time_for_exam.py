start_hour = int(input())
start_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

start_minutes = start_hour * 60 + start_minutes
arrival_minutes = arrival_hour * 60 + arrival_minutes

diff = start_minutes - arrival_minutes

if diff > 30:
    print('Early')
elif diff < 0:
    print('Late')
else:
    print('On time')

hours = 0
minutes = abs(diff)

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

res = ''

if hours > 0:
    res += str(hours) + ':' + ('0' + str(minutes) if minutes < 10 else str(minutes)) + ' hours'
else:
    res += str(minutes) + ' minutes'

if diff > 0:
    res += ' before the start'
elif diff < 0:
    res += ' after the start'

print(res)
