user_answer = int(input('введите количество секунд '))
hour = user_answer // 3600
minute = (user_answer - hour * 3600) // 60
second = (user_answer - hour * 3600) - (minute * 60)
print('время в формате ЧЧ:ММ:СС составляет: %02d:%02d:%02d' % (hour, minute, second))