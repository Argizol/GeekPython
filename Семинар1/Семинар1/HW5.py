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

numsOfCandies = 2021
counter = 0
def playerTurn(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("������� ������� ������ �� ���������: "))
    while takenCandies <= 0 or takenCandies > 28:
        takenCandies = int(input('����� ����� ������ �� 1 �� 28 ������. ���������� �����: '))
        if numsOfCandies < takenCandies:
             print(f'�������� {numsOfCandies} ������, ������� ����� �� 1 �� {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:    
            takenCandies = int(input(f'�������� {numsOfCandies} ������, ������� ����� �� 1 �� {numsOfCandies}: '))    
    numsOfCandies -= takenCandies   
    return numsOfCandies

while numsOfCandies > 0:
        if numsOfCandies > 0:
            print('��� ������ 1')
            numsOfCandies = playerTurn(numsOfCandies)
            counter += 1
        if numsOfCandies > 0:
            print('��� ������ 2')
            numsOfCandies = playerTurn(numsOfCandies)
            counter += 1
if counter % 2 == 0:
    print('������� ����� 2')
else:
    print('������� ����� 1')

#�������� ��������� ��� ���� � ""��������-������"".

#���������� RLE ��������: ���������� ������ ������ � �������������� ������.




