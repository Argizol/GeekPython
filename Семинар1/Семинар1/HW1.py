#������� 8
#�������� � ����� �������� ������������ ��������� ��� �� ����� ��� ��������� ����� � ������������ � � �
print("������� x")
x = int(input())
print("������� y")
y = int(input())

if (x>0) and (y>0):
    print('I ��������')
elif (x>0) and (y<0):
    print('II ��������')
elif (x<0) and (y<0): 
    print('III ��������')
elif (x<0) and (y>0):
    print('IV ��������')
else:
    print('����� ����� �� ���')

#������� 9
#������ ����� �������� ������������� ������� ���������, 
#�������� ���������� �������� ��������� ��� ����� ���� ��������
print("������� ����� ��������")
numOfQuadro = int(input())

def whichCoords(numOfQuadro):
        if numOfQuadro == 1:
            return "�� 1 �� �������������, y = ��  1 �� �������������"
        if numOfQuadro == 2:
            return "�� 1 �� �������������, y = �� -1 �� -�������������"
        if numOfQuadro == 3:
            return "�� -1 �� -�������������, y = �� -1 �� -�������������"
        if numOfQuadro == 3:
            return "�� -1 �� -�������������, y = �� 1 �� �������������"
print(whichCoords(numOfQuadro))

#������� 10
#����� ���������� ����� ����� ������� ������������
import math


print('������� ���������� ������ �����')
print('x1 =')
x1 = int(input())
print('y1 =')
y1 = int(input())
print('z1 =')
z1 = int(input())
print('x2 =')
print('������� ���������� ������ �����')
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




