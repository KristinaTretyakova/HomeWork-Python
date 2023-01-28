# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = int(input("Введите номер билета, чтобы узнать счастливый он, или нет: "))

num1 = number // 1000
num2 = number % 1000

start1 = num1 // 100
start3 = num1 % 10
start2 = (num1 //10) % 10

sum1 = start1 + start2 + start3

end1 = num2 // 100
end3 = num2 % 10
end2 = (num2 //10) % 10

sum2 = end1 + end2 + end3

if sum1 == sum2:
    print("Поздравляю, у Вас счастливый билет ведь сумма 3х первых и последних чисел равны")
else:
    print("К сожалению, у Вас несчастливый билет, но ничего страшного Вам еще повезет!!")
