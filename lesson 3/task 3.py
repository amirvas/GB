def my_func (var1, var2, var3):
    func_list = [var1, var2, var3]
    func_list = sorted(func_list)
    summ = func_list[-1] + func_list[-2]
    return (summ)
num1 = float(input('введите число 1 '))
num2 = float(input('введите число 2 '))
num3 = float(input('введите число 3 '))
print(my_func(num1, num2, num3))