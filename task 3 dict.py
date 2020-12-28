time = {
    'зима': {12, 1, 2},
    'весна': {3, 4, 5},
    'лето': {6, 7, 8},
    'осень': {9, 10, 11}
}
month = int(input('введите месяц в виде целого числа '))
if month <= 12:
    for key, val in time.items():
        if month in val:
            print (f'время года - {key}')
else:
    print('такого месяца не существует')