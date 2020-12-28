n = int(input('введите целое положительное число: '))

max = n % 10
number = n // 10

if max == 9:
    print(f'максимальная цифра: {max}')
else:
    while number > 0:
        if number % 10 > max:
            max = number % 10
        number = number // 10
    print(f'максимальная цифра: {max}')