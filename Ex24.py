#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите кол-во кустов: '))

list_1 = list()

for i in range(n):
    x = int(input('Введите кол-во ягод: '))
    list_1.append(x)

list_count = list()

for i in range(len(list_1) - 1):
    list_count.append(list_1[i -1] + list_1[i] + list_1[i + 1])
list_count.append(list_1[-2] + list_1[-1] + list_1[0])

print(max(list_count))