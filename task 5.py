def_list = [7, 5, 3, 3, 2]
list_max = 10
print(f'исходный список: {def_list}')
while list_max > len(def_list):
    new = int(input('введите целое число '))
    for i in def_list:
        if new >= i:
            def_list.insert(def_list.index(i), new)
            break
    if new < def_list[(len(def_list) - 1)]:
        def_list.append(new)
    print(def_list)
print(f'достигнута максимальная длина списка ({list_max} чисел)')