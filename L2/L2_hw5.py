user_input = input('Введите последовательность чисел через пробел: ')
array = []
array = user_input.split()
for i, elem in enumerate(array):
    array[i] = int(elem)
n = 1
while n < len(array):
    for i in range(len(array) - n):
        if array[i] < array[i + 1]:
            array[i + 1], array[i] = array[i], array[i + 1]
    n += 1
print(array)
new_numb = int(input("Введите число (для выхода нажмите -'159753')"))
while new_numb != 159753:
    for el in range(len(array)):
        if new_numb >= array[el]:
            array.insert(el, new_numb)
            break
        elif array[0] < new_numb:
            array.insert(0, new_numb)
        elif array[-1] > new_numb:
            array.append(new_numb)
    print(f"текущий список - {array}")
    new_numb = int(input("Введите число "))