# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

# будем считать, что уравнение дано в статичном виде
# отбрасываем y =
equation = equation[4:]
# делим строку по пробелам для определения знаков
elemArr = equation.split(' ')
# k и b могут быть нулями
if len(elemArr) == 0:
    # оба нули
    print('y={0}'.format(0));
elif (len(elemArr) == 1) and (elemArr[0].find('x') == 0):
    # k=0
    print('y={0}'.format(equation))
elif (len(elemArr) == 1) and (elemArr[0].find('x') != 0):
    # k != 0 and b = 0
    y = x * float(elemArr[0].replace('x', ''))
    print('y={0}'.format(y))
else:
    # оба не равны нулю
    y = x * float(elemArr[0].replace('x', ''))  # первое слагаемое
    y = y + (-1 if elemArr[1] == '-' else 1) * float(elemArr[2].replace('x', ''))  # второе слагаемое со знаком
    print('y={0}'.format(y))

print()
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

# ===== Вариант 1 ========

print('Вариант 1')


def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def CheckIsDateCorrect(date):
    # проверим длину строки
    if len(date) != 10:
        return False
    # разделим строку на 3 согласно точкам
    dtArr = date.split('.')
    if len(dtArr) != 3:
        return False

    # проверим, что все 3 блока - целые числа
    if not IsInt(dtArr[0]) or not IsInt(dtArr[2]) or not IsInt(dtArr[2]):
        return False

    day = int(dtArr[0])
    month = int(dtArr[1])
    year = int(dtArr[2])

    if (day < 1 or day > 31) or (
        month < 1 or month > 12) or (
        year < 1 or year > 9999):   # скобки для смыслового выделения использовал
        return False
    if (month % 2 == 1 and day == 31):
        return False
    return True


dates = ['01.11.1985', '01.22.1001', '1.12.1001', '-2.10.3001']
for dt in dates:
    res = CheckIsDateCorrect(dt)
    print(res)

# ===== Вариант 2 ========
print('Вариант 2')
import datetime

for dtToCheck in dates:
    try:
        if len(dtToCheck) != 10:
            print(False)
            continue
        dt = datetime.datetime.strptime(dtToCheck, '%d.%m.%Y')
        print(True)
    except:
        print(False)

print()
# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

roomNumber = int(input('Введите номер комнаты: '))
#roomNumber = 2000000000
lastRoomNumber = 0
floorSize = 1
# будем искать последнюю комнату на последнем этаже группы этажей в которых находится искомая комната
while lastRoomNumber < roomNumber:
    lastRoomNumber = lastRoomNumber + floorSize ** 2
    floorSize = floorSize + 1
floorSize = floorSize - 1
# найдем первую комнату группы
firstRoomNumber = lastRoomNumber - floorSize ** 2 + 1
# найдем первый этаж
firstFloorNumber = 0
for num in range(floorSize):
    firstFloorNumber = firstFloorNumber + num

# будем искать этаж на котором находится комната
actualFloor = firstFloorNumber
lastRoomNumberOnFloor = firstRoomNumber + floorSize - 1
while lastRoomNumberOnFloor < roomNumber:
    lastRoomNumberOnFloor = lastRoomNumberOnFloor + floorSize
    actualFloor = actualFloor + 1

actualFloor = actualFloor + 1
# найдем первую комнату этажа
firstRoomNumberOnFloor = lastRoomNumberOnFloor - floorSize + 1

# т.к. прирост номера равен 1 находим позицию нужной комнаты вычитанием

actualRoom = roomNumber - firstRoomNumberOnFloor + 1

print('Этаж: {0} комната: {1}'.format(actualFloor, actualRoom))
