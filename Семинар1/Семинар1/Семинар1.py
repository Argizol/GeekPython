## Задание 1
##По двум заданным числам проверить является ли одно квадратом второго 

#print('Введите число a')
#a = int(input())
#print('Введите число b')
#b = int(input())
#if a*a == b:
#    print(f"{b} является квадратом {a}")
#if b*b == a:
#    print(f"{a} является квадратом {b}")
#else:
#    print ("Ни одно число не является квадратов другого")

##Задание 2
##Найти максимальное из пяти чисел
#my_list = (1, 2, 3, 4, 5)
#print(max(my_list))

##Задание 3
##Вывести на экран числа от -N до N
#print('Введите число')
#n = int(input())
#a = range(-n,n)
#for i in a:
#    print(i)

##Задание 4
##Показать первую цифру дробной части числа
#a = 2000.123
#a_string = str(a)
#print(a_string[a_string.find(".")+1])

##Задание 5
##Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
#a = 30
#if (a%5 == 0 and a%10 == 0) or (a%15 == 0 and not a % 30 == 0):
#    print ("Всё ок")

##Задание 6
##Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
#a = int(input('Введите число от 0 до 6: '))
#my_dict = {
#    0: "Понедельник",
#    1: "Вторник",
#    2: "Среда",
#    3: "Четверг",
#    4: "Пятница",
#    5: "Суббота",
#    6: "Воскресенье",
#}
#if a == 5 and a == 6:
#    print(f"{my_dict.get(a)} Выходной")
#else:
#    print(f"{my_dict.get(a)} Не выходной")

##Задание 6.1
##Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
#from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY
#from enum import Enum

#class DayOfWeek(Enum):
#    MONDAY = 1
#    TUESDAY = 2
#    WENDESDAY = 3
#    THURSDAY = 4
#    FRIDAY = 5
#    SATURDAY = 6
#    SUNDAY = 7

#print("Введите число")
#a = int(input())

#if a in (DayOfWeek.SATURDAY.value, DayOfWeek.SUNDAY.value):
#    print (f"{DayOfWeek(a).name} выходной")
#elif a in (DayOfWeek.MONDAY.value, DayOfWeek.TUESDAY.value, DayOfWeek.WENDESDAY.value, DayOfWeek.THURSDAY.value ,DayOfWeek.FRIDAY.value):
#    print(f"{DayOfWeek(a).name} не выходной")

##Задание 7 
##Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
#x = [True, False]
#y = [True, False]
#z = [True, False]
#count = 0
#for i in x:
#    for j in y:
#        for g in z:
#            count += 1
#            print(f"{count} {not (x or y  or z) == (not x and not y and not z)}")



##Задание 8
##Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
#print("Введите x")
#x = int(input())
#print("Введите y")
#y = int(input())

#if (x>0) and (y>0):
#    print('I четверть')
#elif (x>0) and (y<0):
#    print('II четверть')
#elif (x<0) and (y<0): 
#    print('III четверть')
#elif (x<0) and (y>0):
#    print('IV четверть')
#else:
#    print('Точка лежит на оси')

##Задание 9
##Указав номер четверти прямоугольной системы координат, 
##показать допустимые значения координат для точек этой четверти
#print("Введите номер четверти")
#numOfQuadro = int(input())

#def whichCoords(numOfQuadro):
#        if numOfQuadro == 1:
#            return "От 1 до бесконечности, y = От  1 до бесконесности"
#        if numOfQuadro == 2:
#            return "От 1 до бесконечности, y = От -1 до -бесконесности"
#        if numOfQuadro == 3:
#            return "От -1 до -бесконечности, y = От -1 до -бесконесности"
#        if numOfQuadro == 3:
#            return "От -1 до -бесконечности, y = От 1 до бесконесности"
#print(whichCoords(numOfQuadro))

##Задание 10
##Найти расстояние между двумя точками пространства
#import math


#print('Введите координаты первой точки')
#print('x1 =')
#x1 = int(input())
#print('y1 =')
#y1 = int(input())
#print('z1 =')
#z1 = int(input())
#print('x2 =')
#print('Введите координаты второй точки')
#x2 = int(input())
#print('y2 =')
#y2 = int(input())
#print('z2 =')
#z2 = int(input())
#point1 = (x1, y1, z1)
#point2 = (x2, y2, z2)

#def DistanceBetweenPoint(point1, point2):

#    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))     

#print(DistanceBetweenPoint(point1, point2))

#Задание 11
#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

#num = int(input("Введите число: "))
#asd = [(-3)**i for i in range(num)]

#Задание 12
#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#n = int(input())
#dict = {}
#for i in range(1, n + 1): # i < n
#    b = 3 * i + 1        
#    dict.update({b:i})
#print(dict)

#Задание 13
#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#line_1 = str(input("Введите первую строку: "))
#line_2 = str(input("Введите вторую строку: "))

#print(f"Вторая строка входит в первую {line_1.count(line_2)} раз/раза")

#Задание 14 
#Подсчитать сумму цифр в вещественном числе.

#num = input("Введите число с точкой ")
#result = 0
#for i in range(len(num)):
#    if (num[i] == '.'):
#        continue
#    result += int(num[i])
#print(result)

#Задание 15
#-Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]
#num = int(input())
#arr = []
#for i in range(0, num + 1): 
#    if (i == 0):
#        arr.append(1)
#    else:
#        arr.append(arr[i - 1] * (i + 1))
#print(arr)

#Задание 16 
#-Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму
#16.1
#num = int(input())
#listOfNum = []
#result = 0
#for i in range(1, num + 1):
#    listOfNum.append((1 + 1 / i) ** i)
#for j in range(int(len(listOfNum))):
#    result += listOfNum[j]
#print(result)

#16.2
#k=4
#listofnumber=[]
#for i in range(1,k+1):
#    listofnumber.append((1+1/i)**i)
#result=sum(listofnumber)
#print(result)

#Задание 17
# -Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число

#import math

#n = int(input())
#listOfNums = []
#indexes = []
#numsForMultyply = []
#result = 1

#for i in range(-n, n + 1):
#    listOfNums.append(i)
#print(listOfNums)

#with open(r"C:\Users\argiz\source\repos\GeekPython\Семинар1\Семинар1\Files\simple.txt") as f:
#    F = f.read()
#    nums = F.split('\n')

#for n in nums:
#    indexes.append(int(n))
#print(indexes)

##def Mult(indexes, listOfNums):
##    for i in range(len(listOfNums)):
##        for j in range(len(indexes)):
##            if (i == indexes[j]):
##                numsForMultyply.append(listOfNums[i])
##            else:
##                continue
##    return math.prod(numsForMultyply)
##print(Mult(indexes, listOfNums))

#def Mult(indexes, listOfNums):
#    for j in indexes:
#        numsForMultyply.append(listOfNums[j])
           
#    return math.prod(numsForMultyply)
#print(Mult(indexes, listOfNums))



#Задание 18
#Реализовать алгоритм перемешивания списка. 

#import random
#x = list(range(1, 9))
#random.shuffle(x)
#print(x)

#Задание 19
# Реализовать алгоритм задания случайных чисел.
# Без использования встроенного генератора псевдослучайных чисел

#from time import perf_counter

#len_of_num = input('Enter the len of number: ')
#output_number = 0
#if len_of_num.isdigit():
#    current_time = int(str(perf_counter()).split('.', 1)[-1])
#    output_number = (str(current_time ** (int(len_of_num) // 6 + 1)))[:int(len_of_num)]
#    print(output_number)
#else:
#    print('Please check if the entered value is a number')


#Задание 20 
#Определить, присутствует ли в заданном списке строк, некоторое число 

#num = input()
#listOfStrings = ["sfkjfj123", "oopsvl312", "poi0845", "pjhsadj21"]
#for strings in listOfStrings:

#    exist = num in strings
#    print(exist)


# Задание 21 Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1

#listOfStrings = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
#whatFind = "qwe"
#listOfStrings = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
#whatFind = "йцу"
#listOfStrings = ["йцу", "фыв", "ячс", "цук", "йцукен"]
#whatFind = "йцу"
#counter = 0

#for i in range(len(listOfStrings)):
    
#    if listOfStrings[i] == whatFind: 
#        counter += 1
#        if counter == 2:
#            print(i)
#            break
#if counter < 2:
#    print(-1)

    
#Задание 22 
#Найти сумму чисел списка стоящих на нечетной позиции

#listOfNums = [1, 12, 43, 1, 0, 22]
#result = 0

##for i in range(len(listOfNums) // 2):
##    result += listOfNums[2 * i + 1]
#for i in range(len(listOfNums)):

#    if i % 2 != 0:
#        result += listOfNums[i]
#print(result)

#Задание 23
#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
#listOfNum = [2, 3, 4, 5, 6]
#result = []
#listOfNum =[2, 3, 5, 6]
#for i in range(int(len(listOfNum)/2 + len(listOfNum)%2)):
#    #if len(listOfNum) % 2 == 0:
#    #    if i >= len(listOfNum)//2:
#    #        break
#    #    else:
#            result.append(listOfNum[i]*listOfNum[-(i + 1)])
#    #else:
#    #    if i > len(listOfNum)//2:
#    #        break
#    #    else:
#    #        result.append(listOfNum[i]*listOfNum[-(i + 1)])
#print(result)

#Задание 24 
#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#listOfNums = [1.1, 1.2, 3.1, 5, 10.01]
#listOfNumsAfterPoint = []

#for num in listOfNums:
#    if num % 1 != 0:
#        listOfNumsAfterPoint.append(float('0.%s' % str(num).split('.')[1])) #listOfNumsAfterPoint.append(num % 1)
#result = max(listOfNumsAfterPoint) - min(listOfNumsAfterPoint)
#print(result)


#Задание 25
#Написать программу преобразования десятичного числа в двоичное
#num = 45
##45 -> 101101
#def ToBynnary(number):
#    result = ''    
#    while(number != 0):    
#            result = result + str(int(number % 2))
#            number = int(number / 2)
#    return result
#print(ToBynnary(num))

##Задание 26 
##Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
##Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

#a = 8
#def Fibonachi(num):
#    fibonacchiRow = []
#    firstNum = 0
#    secondNum = 1
#    result = 0
#    i = 0
#    while(i < num):
#        if (i == 0):
#            fibonacchiRow.append(0)
#        if (i == 1):
#            fibonacchiRow.append(1)
#            fibonacchiRow.insert(0, -1)
#        else:
#            result = firstNum + secondNum
#            firstNum = secondNum
#            secondNum = result
#            fibonacchiRow.append(result)
#            if fibonacchiRow[0] > 0:
#                fibonacchiRow.insert(0, -result)
#            else: 
#                fibonacchiRow.insert(0, result)
#        i += 1
#    return fibonacchiRow
#print(Fibonachi(8))

#Задание 27 
#Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел

#stringWithNums = "1 25 -6 17 24 15"
#stringNums = stringWithNums.split(' ')
#nums = []
#for num in stringNums:
#    nums.append(int(num))
#print(f"Максимальное число: {max(nums)}\nМинимальное число: {min(nums)}")

#Задание 28 Найти корни квадратного уравнения Ax² + Bx + C = 0
#Математикой
#Используя дополнительные библиотеки*
#print('28. Найти корни квадратного уравнения Ax² + Bx + C = 0'
#      '\n    a) Математикой'
#      '\n    b) Используя дополнительные библиотеки')
## a) Математикой
#a, b, c = list(map(int, input("Enter the variable values separated by a space: ").split()))
#discriminant = D = b ** 2 - 4 a * c
#if D == 0:
#    print('The discriminant is 0.\nThe only root of the equation is x = %.2f' % (-b / (2 * a)))
#elif D < 0:
#    print(f'The discriminant is less than 0.\nThe equation has no material roots.')
#else:
#    print(f'The discriminant is greater than 0.\nThe equation has 2 roots:')
#    print('x_1 = %.2f,' % ((-b + D  0.5) / (2 * a)), 'x_2 = %.2f' % ((-b - D  0.5) / (2 * a)))
## b) Используя дополнительные библиотеки*
#import Mathf

#x, y, z = list(map(int, input("Enter the variable values separated by a space: ").split()))
#discriminant = D = pow(b, 2) - 4 * a * c
#if D == 0:
#    print('The discriminant is 0.\nThe only root of the equation is x = %.2f' % (-b / (2 * a)))
#elif D < 0:
#    print(f'The discriminant is less than 0.\nThe equation has no material roots.')
#else:
#    print(f'The discriminant is greater than 0.\nThe equation has 2 roots:')
#    print('x_1 = %.2f,' % ((-b + Mathf.sqrt(D)) / (2 * a)), 'x_2 = %.2f' % ((-b - Mathf.sqrt(D)) / (2 * a))) 

#Задание 29 
#Найти НОК двух чисел
#print('29. Найти НОК двух чисел')
#import math
## Математикой
#a, b = map(int, input("Enter the variable values separated by a space: ").split())
#least_common_multiple = max(a, b)
#while True:
#    if least_common_multiple % a == 0 and least_common_multiple % b == 0:
#        print(f'The least common multiple is {least_common_multiple}')
#        break
#    else:
#        least_common_multiple += 1
## Библиотекой
#x, y = map(int, input("Enter the variable values separated by a space: ").split())
#print(f'The greatest common divisor is {(x * y) // math.lcm(y, x)}')
#print(f'The least common multiple is {(x * y) // math.gcd(y, x)}')
## Функцией


#def calculate_lcm(m, n):
#    if m > n:
#        greater = m
#    else:
#        greater = n
#    while True:
#        if (greater % m == 0) and (greater % n == 0):
#            lcm = greater
#            break
#        greater += 1
#    return lcm
#j, k = map(int, input("Enter the variable values separated by a space: ").split())
#print('The least common multiple of %s and %s is %s' % (j, k, calculate_lcm(j, k)))

#Задание 30
# Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d10-10
from decimal import  *
import math
from random import randint, random
from unicodedata import decimal 
##ряд Нилоканта
#getcontext().prec  =  1000
#from decimal import Decimal
#from unittest import result
#def nilakantha ( reps ): 
#        result  =  Decimal(3.0) 
#        op  =  1 
#        n  =  2 
#        for  n  in  range ( 2 ,  2 * reps + 1 ,  2 ): 
#                result  +=  4 / Decimal ( n * ( n + 1 ) * ( n + 2 ) * op ) 
#                op  *=  - 1 
#        return result
       

#print("Сколько повторов?") 
#repetitions  =  int(input()) 
#print(nilakantha(repetitions)) 
#print( "3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679" )

#Ряд обратных квадратов

#pi = 0
#userPrecision = int(input('Введите до какого знака после запятой вести расчет: '))
#for i in range(1, 10 ** (userPrecision + 1)):
#    pi += 1 / (i ** 2)
    
#piResult = Decimal((pi * 6)**0.5) 
#print(str(piResult)[:(userPrecision + 2)])
#3.141592644982389881391782182618044316768646240234375

#Задание 30 *** , Подумать, что если точность вычисления до 1000 знаков после запятой / точность 1000 для ряда обратных квадратов



#Задание 31
#Составить список простых множителей натурального числа N

#num = int(input())
#listOfSimpleMultiplier = []
#i = 2
#while num > 1:
#    while num % i == 0:
#        listOfSimpleMultiplier.append(i)
#        num //= i
#    i += 1
#print(listOfSimpleMultiplier)

#Задание 32 Дана последовательность чисел.
#Получить список неповторяющихся элементов исходной последовательности 
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

#listOfNums = [1, 2, 3, 5, 1, 5, 3, 10]
#listOfUnicNums = []
#for i in listOfNums:
#    if i not in listOfUnicNums:
#        listOfUnicNums.append(i)
#print(listOfUnicNums)

#Задание 33 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k. 
#  Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Введите макисмальный коэффициент степени для многочлена: '))
resultString = ' '
if k >= 0:
    while k > 0:
        if k == 1:
            resultString += f'{randint(0, 100)}*x + '
        else:
            resultString += f'{randint(0, 100)}*x^{k} + '
        k -= 1
    resultString += f'{randint(0, 100)} = 0'
else:
    while k < 0:
        resultString += f'{randint(0, 100)}*x^{k} + '
        k += 1
    resultString += f'{randint(0, 100)} = 0'
print(resultString)