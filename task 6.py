a = int(input('результат пробежки первого дня в км '))
b = int(input('минимальный требуемый результат '))
day_counter = 0
while a < b:
    day_counter += 1
    print(f'{day_counter}-й день: {a:.2f}')
    a = a * 1.1
else:
    day_counter += 1
    print(f'{day_counter}-й день: {a:.2f}')
    a = a * 1.1
    print(f'на {day_counter}-й день спортсмен достиг результата - не менее {b} км')