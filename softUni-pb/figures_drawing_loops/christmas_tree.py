num = int(input())

for star in range(num + 1):
    print((num - star) * ' ' + star * '*' + ' | ' + star * '*')
