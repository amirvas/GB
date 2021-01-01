def inform (var1, var2, var3, var4, var5, var6):
    return (f'имя:{var1}, фамилия: {var2}, дата рождения: {var3}, город проживания: {var4}, email: {var5}, телефон: {var6}')

name = 'Иван'
surname = 'Иванов'
date_birth = '01.01.1990'
live_in = 'Казань'
email = 'ivanov@gmail.com'
phone = 79871231212
print(inform(name, surname, date_birth, live_in, email, phone))