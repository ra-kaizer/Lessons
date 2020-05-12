number = input("Введите целое положительное число: ")
a = 0
for pos_integ in number:
    while int(pos_integ) > a:
        a = int(pos_integ)
print('Самое большое значение в числе: ', a)
