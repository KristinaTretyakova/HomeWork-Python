# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите кол-во монеток: '))

count0 = 0
count1 = 0

for i in range(n):
    coin = int(input('Введите сторону монетки 1 или 0: '))
    if coin == 0:
        count0 += 1
    if coin == 1:
        count1 += 1

if count0 < count1:
    print(f'{count0} нужно перевернуть, чтобы все монетки были повернуты одной стороной:)')
elif count0 == count1: 
    print(f'{count0} нужно перевернуть, чтобы все монетки были повернуты одной стороной:)') # синтаксически можно использовать и count1, ведь они равны, так что разницы нет..
else:
    print(f'{count1} нужно перевернуть, чтобы все монетки были повернуты одной стороной:)')