# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()
# ===================================================

inputArr = ["яблоко", "банан", "киви", "арбуз"]
# найдем самое длинное слово

maxLenStr = len(max(inputArr, key = len))
counter = 0
for el in inputArr:
    counter = counter + 1
    # найдем нужное количество пробелов для вставк®и
    spaceCount = maxLenStr - len(el)
    print(str(str(counter) + ". {0}{1}").format(' ' * spaceCount, el))

# ===================================================

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке
# ===================================================
inputArr = [1, 2, 4, 5, 7, 8, 9]

inputArrTwo = [1, 2, 5]
inputArr = list(m for m in inputArr if m not in inputArrTwo)
print(inputArr)

# ===================================================

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.
# ===================================================

inputArr = [1, 2, 4, 5, 7, 8, 9]
resArr = list((x / 4 if x % 2 == 0 else x * 2) for x in inputArr)
print(resArr)
# ===================================================
