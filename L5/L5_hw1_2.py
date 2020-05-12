my_list = []  # Задание 1
while True:
    line = input("Введите что-нибудь: ")
    if line == '':
        print("Файл записан!")
        break
    else:
        newline = line + '\n'
        my_list.append(newline)
my_f = open("test_1.txt", "w", encoding="UTF-8")
my_f.writelines(my_list)
my_f.close()

print(100 * "*")
my_f = open('test_1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

print(100 * "*")  # Задание 2

with open("test_1.txt", 'r', encoding="UTF-8") as f:
    content = f.read()
    content = content.split()
    print(f'Общее количество слов: {len(content)}')
for i in range(len(content)):
    print(f'Количество символов {i + 1}-ой строки: {len(content[i])}')
my_f.close()
