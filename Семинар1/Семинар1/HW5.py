##Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#str1 = list(input().split())
str1 = str1 = ['абв', 'пдлдляв', 'абвщлли', 'ащдлпоь']
str2 = [str1[x] for x in range(len(str1)) if not str1[x].__contains__("абв")]
strResult = ''
for i in str2:
    strResult += i + ' '
print(strResult.strip())


##Создайте программу для игры с конфетами человек против человека.
##Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
##a) Добавьте игру против бота
##b) Подумайте как наделить бота ""интеллектом""
from random import randint as randint
numsOfCandies = 2021
counter = 0
def playerTurn(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("Введите сколько конфет вы забираете: "))
    while takenCandies <= 0 or takenCandies > 28:
        takenCandies = int(input('Брать можно только от 1 до 28 конфет. Попробуйте снова: '))
        if numsOfCandies < takenCandies:
             print(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:    
            takenCandies = int(input(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}: '))    
    numsOfCandies -= takenCandies   
    return numsOfCandies

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

# С ботом
from random import randint as randint
numsOfCandies = 2021
counter = 0

def pcTurn(numsOfCandies):
    takenCandies = randint(1, 28)
    while takenCandies > numsOfCandies:
        takenCandies = randint(1, 28)
    if numsOfCandies <= 28:
        takenCandies = numsOfCandies
    if 28 < numsOfCandies < 56:
        takenCandies = numsOfCandies - 29
    numsOfCandies -= takenCandies
    print(f'Бот забирает {takenCandies} конфет. Осталось конфет: {numsOfCandies}')
    return numsOfCandies

while numsOfCandies > 0:
        if numsOfCandies > 0:
            print('Ход игрока 1')
            numsOfCandies = playerTurn(numsOfCandies)
            counter += 1
        if numsOfCandies > 0:
            print('Ход Бота')
            numsOfCandies = pcTurn(numsOfCandies)
            counter += 1
if counter % 2 == 0:
    print('Победил Бот')
else:
    print('Победил игрок')


##Создайте программу для игры в ""Крестики-нолики"".

game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True
while game_is_on:
    # Крестик - латинская буква X, нолик - латинская буква O 
    # Ходы принимаются в формате [0][0] = "X" или [2][1] = "О"
    move = input()
    exec("game_matrix" + move)
    for row in game_matrix:
        print(row)
    
    reference_matrix = [
        game_matrix[0],
        game_matrix[1],
        game_matrix[2],
        [i[0] for i in game_matrix],
        [i[1] for i in game_matrix],
        [i[2] for i in game_matrix],
        [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
        [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Game over!")
            game_is_on = False
            break

##Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        with open(r'd:\PyProjects\python_lesson_5\task_42_output_data.txt', '+a') as f:
            f.write(f'Encoded data: {encoding}\n')
        return encoding


def decode(data):
    decoding = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    with open(r'task_42_output_data.txt', '+a') as f:
        f.write(f'Decoded data: {decoding}\n')
    return decoding


with open(r'task_42_encoding_data.txt', 'r') as f:
    encoding_data = f.read()
# encoding_data = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
print(f'Encoded data: {encode(encoding_data)}')

with open(r'task_42_decoding_data.txt', 'r') as f:
    decoding_data = f.read()
# decoding_data = '6A1F2D7C1A17E'
print(f'Decoded data: {decode(decoding_data)}')