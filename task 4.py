text = input('введите строку из нескольких слов, разделенной пробелами ')
list_text = text.split()
print('каждое введенное слово с новой строки:')
for i in range(len(list_text)):
    word = list_text[i]
    print(f'{i+1}. {word[:10]}')