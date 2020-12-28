month = int(input('введите месяц в виде целого числа '))
winter = [12 , 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print('время года - зима')
elif month in spring:
    print('время года - весна')
elif month in summer:
    print('время года - лето')
elif month in autumn:
    print('время года - осень')