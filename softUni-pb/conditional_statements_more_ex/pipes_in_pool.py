pool_volume = int(input())
debit_pipe1 = int(input())
debit_pipe2 = int(input())
hours = float(input())

liters_from_pipe1 = hours * debit_pipe1
liters_from_pipe2 = hours * debit_pipe2
total_liters = liters_from_pipe1 + liters_from_pipe2

percent_from_pipe1 = liters_from_pipe1 / (total_liters / 100)
percent_from_pipe2 = liters_from_pipe2 / (total_liters / 100)
percent_pool = total_liters / (pool_volume / 100)

if percent_pool <= 100:
    print(f'The pool is {percent_pool:.2f}% full. Pipe 1: {percent_from_pipe1:.2f}%. \
    Pipe 2: {percent_from_pipe2:.2f}%.')
else:
    print(f'For {hours} hours the pool overflows with {total_liters - pool_volume} liters.')
