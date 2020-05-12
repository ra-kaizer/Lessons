def summary():
    try:
        with open('file_5.txt', 'w', encoding="UTF-8") as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Файл утерян')
    except ValueError:
        print('Ошибка! Нужно ввести числа!')


summary()
