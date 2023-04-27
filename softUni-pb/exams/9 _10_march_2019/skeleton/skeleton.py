control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_100m = int(input())

time_marin = length / 100 * seconds_100m - length / 120 * 2.5

control_seconds += control_minutes * 60

if control_seconds >= time_marin:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_marin:.3f}.')
else:
    print(f'No, Marin failed! He was {time_marin - control_seconds:.3f} second slower.')
