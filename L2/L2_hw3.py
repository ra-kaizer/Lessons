list = ['зима', 'весна', 'лето', 'осень']
dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите календарный месяц в виде целого числа: "))
if month == 1 or month == 12 or month == 2:
    print(month, "месяц равен времени года - ", dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(month, "месяц равен времени года - ", dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(month, "месяц равен времени года - ", dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(month, "месяц равен времени года - ", dict.get(4))
else:
    print("Такого месяца не существует")
