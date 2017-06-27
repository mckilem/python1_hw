# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

a = 65748392020
for x in str(a):
    print(x)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print('a = ', b, 'b = ', a) - это неправильное решение!

a = int(input('input integer a: '))
b = int(input('input integer b: '))
c = a
a = b
b = c
print('a = ' + str(a))
print('b = ' + str(b))


# Задача-3: Запросите у пользователя год рождения. Если ему есть 18 лет, выведите: 'Доступ разрешени',
# иначе 'Извините, пользование данным ресурсом только с 18 лет'

a = int(input('enter your birthdate: '))
if (a < 0) or (a > 100):
    print('stop cheating')
else:
    if a >= 18:
        print('access granted')
    else:
        print('access denied: only person above 18 yo allowed ti use this resource')
