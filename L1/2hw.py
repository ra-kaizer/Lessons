time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
rest = time_in_sec % 3600
minutes = rest // 60
sec = rest % 60
print(f"Заданное время: {hours:02}:{minutes:02}:{sec:02} ")