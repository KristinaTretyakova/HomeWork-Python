# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

N = int(input('Введите количество элементов в массиве: '))
list_1 = list()

for i in range(N):
    n = int(input('Введите элемент массива, натуральное целое число: '))
    list_1.append(n)

x = int(input('Введите число, чтобы проверить сколько раз оно встречается в массиве: '))
result = 0

for i in range (len(list_1)):
    if list_1[i] == x:
        result += 1

print(f'Среди введенных Вами чисел {list_1} число {x} встречается {result} раз(-a)') 
