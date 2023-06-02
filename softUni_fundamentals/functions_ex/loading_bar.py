def loading_bar(num):
    message = ''
    if num == 100:
        message = '100% Complete!\n[%%%%%%%%%%]'
    else:
        loaded_count = num // 10
        message = f'{num}% [{loaded_count * "%"}{(10 - loaded_count) * "."}]\nStill loading...'
    return message


number = int(input())
print(loading_bar(number))
