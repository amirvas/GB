def analytics(some_list, answer):
    name_list = []
    for key, val in some_list.items():
        for key2, val2 in val.items():
            if key2 == answer:
                name_list.append(val2)
    return name_list
def_list = {
    1: {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'},
    2: {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'},
    3: {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'}
}

user_ques = input('вы можете вывести аналитику о товарах, введите параметр: название/цена/количество ')
print(f'{user_ques} товаров: {analytics(def_list, user_ques)}')
while True:
    decision = input('хотите вывести другой аналитический срез? да/нет ')
    if decision.lower() == 'да':
        user_ques = input('вы можете вывести аналитику о товарах, введите параметр: название/цена/количество ')
        print(f'{user_ques} купленных товаров: {analytics(def_list, user_ques)}')
    elif decision.lower() == 'нет':
        print('конец программы')
        break
    else:
        print('ваша позиция не понятна')