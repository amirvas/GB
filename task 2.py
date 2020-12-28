def_list = []
while True:
    try:
        len_list = int(input('введите длину создаваемого списка '))
        break
    except ValueError:
        print('длину списка должна быть в виде целого числа. Еще раз:')
i = 0
while i < len_list:
    i += 1
    def_list.append(input(f'введите {i} элемент списка '))
print(f'ваш список {def_list}')
while True:
    decision = input('хотите ли вы реализовать обмен значений соседних элементов? Да/нет ')
    if decision.lower() == 'да':
        for i in range(0, len(def_list)-1, 2):
            def_list[i], def_list[i+1] = def_list[i+1], def_list[i]
        print(f'измененный список {def_list}')
        break
    elif decision.lower() == 'нет':
        print('конец программы')
        break
    else:
        print('ваша позиция не понятна. Еще раз:')