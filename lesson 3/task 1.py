def division (num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = 'нельзя делить на ноль'
    return(result)
x = float(input('введите число Х '))
y = float(input('введите число Y '))
print(f'результат деления: {division(x, y)}')