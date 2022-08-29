#�������� ���������, ��������� �� ������ ��� �����, ���������� ""���"".

#str1 = list(input().split())
str1 = ['���', '�������', '�������', '�������']
str2 = [str1[x] for x in range(len(str1)) if not str1[x].__contains__("���")]
strResult = ''
for i in str2:
    strResult += i + ' '
print(strResult.strip())


#�������� ��������� ��� ���� � ��������� ������� ������ ��������.
#������� ������: �� ����� ����� 2021 �������. ������ ��� ������ ����� ��� ���� ����� �����. ������ ��� ������������ �����������. �� ���� ��� ����� ������� �� ����� ��� 28 ������. ��� ������� ��������� ��������� ���������� ��������� ���. ������� ������ ����� ����� ������� ������, ����� ������� ��� ������� � ������ ����������?
#a) �������� ���� ������ ����
#b) ��������� ��� �������� ���� ""�����������""
from random import randint as randint
#numsOfCandies = 2021
#counter = 0
#def playerTurn(numsOfCandies):
#    if numsOfCandies == 0:
#        return -1
#    takenCandies = int(input("Введите сколько конфет вы забираете: "))
#    while takenCandies <= 0 or takenCandies > 28:
#        takenCandies = int(input('Брать можно только от 1 до 28 конфет. Попробуйте снова: '))
#        if numsOfCandies < takenCandies:
#             print(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}')
#    if numsOfCandies < takenCandies:
#        while takenCandies <= 0 or takenCandies > numsOfCandies:    
#            takenCandies = int(input(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}: '))    
#    numsOfCandies -= takenCandies   
#    return numsOfCandies

#while numsOfCandies > 0:
#        if numsOfCandies > 0:
#            print('Ход игрока 1')
#            numsOfCandies = playerTurn(numsOfCandies)
#            counter += 1
#        if numsOfCandies > 0:
#            print('Ход игрока 2')
#            numsOfCandies = playerTurn(numsOfCandies)
#            counter += 1
#if counter % 2 == 0:
#    print('Победил игрок 2')
#else:
#    print('Победил игрок 1')

## С ботом
#from random import randint as randint
#numsOfCandies = 200
#counter = 0
#def playerTurn(numsOfCandies):
#    if numsOfCandies == 0:
#        return -1
#    takenCandies = int(input("Введите сколько конфет вы забираете: "))
#    while takenCandies <= 0 or takenCandies > 28:
#        takenCandies = int(input('Брать можно только от 1 до 28 конфет. Попробуйте снова: '))
#        if numsOfCandies < takenCandies:
#             print(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}')
#    if numsOfCandies < takenCandies:
#        while takenCandies <= 0 or takenCandies > numsOfCandies:    
#            takenCandies = int(input(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}: '))    
#    numsOfCandies -= takenCandies   
#    return numsOfCandies

#def pcTurn(numsOfCandies):
#    takenCandies = randint(1, 28)
#    while takenCandies > numsOfCandies:
#        takenCandies = randint(1, 28)
#    if numsOfCandies <= 28:
#        takenCandies = numsOfCandies
#    if 28 < numsOfCandies < 56:
#        takenCandies = numsOfCandies - 29
#        # print(f'Компьютер забирает {takenCandies} конфет. ', end='')
#    numsOfCandies -= takenCandies
#    print(f'Компьютер забирает {takenCandies} конфет. Осталось конфет: {numsOfCandies}')
#    return numsOfCandies


#���������� RLE ��������: ���������� ������ ������ � �������������� ������.






