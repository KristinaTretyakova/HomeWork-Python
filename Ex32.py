# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)


list_1 = list()

N = int(input("Введите размер массива: "))

for i in range(N):
    n = int(input('Введите элемент массива, натуральное целое число: '))
    list_1.append(n)

min_number = int(input('Задайте минимум: '))
max_number = int(input("Задайте максимум: "))

print(list_1)

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)