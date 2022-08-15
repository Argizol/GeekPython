# Задание 1
a = 9
b = 3
if a*a == b:
    print(f"{b} является квадратом {a}")
if b*b == a:
    print(f"{a} является квадратом {b}")
else:
    print ("Ни одно число не является квадратов другого")

#Задание 2
my_list = (1, 2, 3, 4, 5)
print(max(my_list))

#Задание 3
a = range(-1,20)
for i in a:
    print(i)

#Задание 4
a = 2000.123
a_string = str(a)
print(a_string[a_string.find(".")+1])

#Задание 5
a = 30
if (a%5 == 0 and a%10 == 0) or (a%15 == 0 and not a % 30 == 0):
    print ("Всё ок")

#Задание 6
a = int(input('Введите число от 0 до 6: '))
my_dict = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье",
}
if a == 5 and a == 6:
    print(f"{my_dict.get(a)} Выходной")
else:
    print(f"{my_dict.get(a)} Не выходной")

#Задание 6.1
from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY
from enum import Enum

class DayOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WENDESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print("Введите число")
a = int(input())

if a in (DayOfWeek.SATURDAY.value, DayOfWeek.SUNDAY.value):
    print (f"{DayOfWeek(a).name} выходной")
elif a in (DayOfWeek.MONDAY.value, DayOfWeek.TUESDAY.value, DayOfWeek.WENDESDAY.value, DayOfWeek.THURSDAY.value ,DayOfWeek.FRIDAY.value):
    print(f"{DayOfWeek(a).name} не выходной")

#Задание 7 (не понято ТЗ)
#x = True
#y = False
#z = False
#print(not (x or y  or z) == (not x and not y and not z))

#Задание 8
print("Введите x")
x = int(input())
print("Введите y")
y = int(input())

if (x>0) and (y>0):
    print('I четверть')
elif (x>0) and (y<0):
    print('II четверть')
elif (x<0) and (y<0): 
    print('III четверть')
elif (x<0) and (y>0):
    print('IV четверть')
else:
    print('Точка лежит на оси')

#Задание 9
print("Введите номер четверти")
numOfQuadro = int(input())

def whichCoords(numOfQuadro):
        if numOfQuadro == 1:
            return "От 1 до бесконечности, y = От  1 до бесконесности"
        if numOfQuadro == 2:
            return "От 1 до бесконечности, y = От -1 до -бесконесности"
        if numOfQuadro == 3:
            return "От -1 до -бесконечности, y = От -1 до -бесконесности"
        if numOfQuadro == 3:
            return "От -1 до -бесконечности, y = От 1 до бесконесности"
print(whichCoords(numOfQuadro))