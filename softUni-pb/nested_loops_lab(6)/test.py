for num1 in range(5):
    for num2 in range(5):
        if num1 == num2:
            continue
        for num3 in range(5):
            if num3 == num1 or num3 == num2:
                continue
            for num4 in range(5):
                if num4 == num1 or num4 == num2 or num4 == num3:
                    continue
                for num5 in range(5):
                    if num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                        continue
                    print(f'{num1}{num2}{num3}{num4}{num5}')
