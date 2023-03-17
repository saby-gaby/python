from math import ceil

film = input()
episode = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
resting_time = break_duration / 4
time_left = break_duration - lunch_time - resting_time

diff = ceil(abs(episode - time_left))

if time_left >= episode:
    print(f'You have enough time to watch {film} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {film}, you need {diff} more minutes.")
