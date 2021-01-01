def my_func (x ,y):
    result = x**y
    return (result)
num1 = float(input('введите действительное число '))
num2 = int(input('введите целое отрицательное число '))
print(f'результат возведения числа {num1} в степень {num2} = {my_func(num1, num2)}')