#Задание 8
#Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
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
#Указав номер четверти прямоугольной системы координат, 
#показать допустимые значения координат для точек этой четверти
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

#Задание 10
#Найти расстояние между двумя точками пространства
import math


print('Введите координаты первой точки')
print('x1 =')
x1 = int(input())
print('y1 =')
y1 = int(input())
print('z1 =')
z1 = int(input())
print('x2 =')
print('Введите координаты второй точки')
x2 = int(input())
print('y2 =')
y2 = int(input())
print('z2 =')
z2 = int(input())
point1 = (x1, y1, z1)
point2 = (x2, y2, z2)

def DistanceBetweenPoint(point1, point2):

    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))     

print(DistanceBetweenPoint(point1, point2))




