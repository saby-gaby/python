def check_perfect_number(num):
    divisors_sum = sum([divisor for divisor in range(1, num) if num % divisor == 0])
    if num == divisors_sum:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


number = int(input())
print(check_perfect_number(number))
