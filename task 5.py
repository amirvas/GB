income = float(input('введите полученную выручку '))
costs = float(input('введите понесенные издержки '))
if income > costs:
    print('ваша компания работает в плюс')
    R = ((income - costs) / income) * 100
    print(f'рентабельность составила {R:.2f} %')
elif income == costs:
    print('ваша компания находится в точке безубыточности')
else:
    print('ваша компания работает в минус')
staff = int(input('введите численность сотрудников '))
profit_per_staff = (income - costs) / staff
print(f'прибыль фирмы в расчете на одного сотрудника составила: {profit_per_staff:.2f} рублей')
