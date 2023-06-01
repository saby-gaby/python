def odd_even_sums(num_as_str):
    odd = sum([int(num) for num in num_as_str if int(num) % 2 != 0])
    even = sum([int(num) for num in num_as_str if int(num) % 2 == 0])
    # odd, even = 0, 0
    # for char in num_as_str:
    #     num = int(char)
    #     if num % 2 == 0:
    #         even += num
    #     else:
    #         odd += num
    return f'Odd sum = {odd}, Even sum = {even}'


number = input()
print(odd_even_sums(number))
