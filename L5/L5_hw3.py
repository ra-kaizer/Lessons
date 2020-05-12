summ = 0
count = 0
surname = []
with open("text_3.txt", 'r', encoding="UTF-8") as f:
    for line in f:
        i = line.split()
        print(line, end=" ")
        if float(i[1]) <= 20000:
            surname.append(i[0])
        summ += float(i[1])
        count += 1
result = summ / count
print(f'\n Оклад меньше 20.000: {surname}, средний оклад: {result}')
f.close()

print(100 * ("-"))

# вариант 2
names, wages = [], []

with open('text_3.txt', 'r', encoding="UTF-8") as f:
    # считываю его
    read_file = f.read()
    # разбиваю считанное по строкам
    lines = read_file.split('\n')
    # для каждой строки
    for line in lines:
        # я формирую список из элементов строки, разбитых черех пробел
        # делаю это через [el for el in line.split()]
        # нулевой элемент - это имя
        names.append([el for el in line.split()][0])
        # второй - з / п
        wages.append([el for el in line.split()][1])
# дальше склеиваю в словарь
my_dict = dict(zip(names, wages))

# чтобы вывести тех, кто больше порога
for key, value in my_dict.items():
    if float(value) < 20000:
        print(key, value)