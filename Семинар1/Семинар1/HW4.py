#Задание 31
#Составить список простых множителей натурального числа N

from ntpath import join


num = int(input())
listOfSimpleMultiplier = []
i = 2
while num > 1:
    while num % i == 0:
        listOfSimpleMultiplier.append(i)
        num //= i
    i += 1
print(listOfSimpleMultiplier)

#Задание 32 Дана последовательность чисел.
#Получить список неповторяющихся элементов исходной последовательности 
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

listOfNums = [1, 2, 3, 5, 1, 5, 3, 10]
listOfUnicNums = []
for i in listOfNums:
    if i not in listOfUnicNums:
        listOfUnicNums.append(i)
print(listOfUnicNums)

#Задание 33 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k. 
#  Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Введите макисмальный коэффициент степени для многочлена: '))
resultString = ''
if k >= 0:
    while k > 0:
        if k == 1:
            resultString += f'{randint(0, 100)}*x + '
        else:
            resultString += f'{randint(0, 100)}*x^{k} + '
        k -= 1

else:
    while k < 0:
        resultString += f'{randint(0, 100)}*x^{k} + '
        k += 1
resultString += f'{randint(0, 100)} = 0'
with open(r'C:\Users\argiz\source\repos\GeekPython\Семинар1\Семинар1\Files\hw4.txt','+a') as f:
    f.write(resultString + '\n')
print(resultString)





