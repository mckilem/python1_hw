# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа

a = 1789876521
maxValue = -1
for x in str(a):
    b = int(x)
    if maxValue < b:
        maxValue = b
print(maxValue)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные
a = int(input('input integer a: '))
b = int(input('input integer b: '))
a = a + b
b = (-1) * (b - a)
a = a - b
print('a = ' + str(a))
print('b = ' + str(b))


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
import math
# math.sqrt(4) - вычисляет корень числа 4


# дано уравнение ax2 + bx + c = 0
# вводим a и b
print('we have an equation ax2 + bx + c = 0. Please enter a,b and c')
a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))
if (a==0) or (c==0):
    print('please^ enter correct values for a and c')
else:
    # считаем дискриминант
    dis = b ** 2 - 4 * a * c
    if dis < 0:
        print('D<0: lets not get into irrational values')
    elif dis == 0:
        x = (-1) * b / (2 * a)
        print('D=0: equation has one solution: ' + str(x))
    else:  # D > 0
        x1 = ((-1) * b + math.sqrt(dis)) / (2 * a)
        x2 = ((-1) * b - math.sqrt(dis)) / (2 * a)
        print('D>0: equation has two solutions: ' + str(x1) + ' and ' + str(x2))