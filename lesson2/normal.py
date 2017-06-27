# Задача-1:
# Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
inputArr = [2, -5, 8, 9, -25, 25, 4]
resArr = list(int(math.sqrt(x)) for x in inputArr if (x > 0) and (math.sqrt(x) % 1 == 0))
print(resArr)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
import datetime
inputDate = '05.06.2017'
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
days = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое'] # не заполнил до конца и не ставил проверок

dt = datetime.datetime.strptime(inputDate, '%d.%m.%Y')
print('{0} {1} {2} года'.format(days[dt.day], months[dt.month], dt.year))

# Задача-3: Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random

import random
listArr = []
n = 10
for x in range(n):
    listArr.append(random.randint(-100, 100))
print(listArr)

# Задача-4: Дан список заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного

listArr = list(set(listArr))
print(listArr)