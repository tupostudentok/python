from random import *

print('Доброй пожаловать в числовую угадайку','\nВведите числа с какого по какое вы хотите угадывать:')

def is_valid(num):
    if num.isdigit() and 1<=int(num)<=100:
        return True
    else:
        return False
def is_valid_num():
    a, b=int(input()), int(input())
    number=randint(a,b+1)
    counter=0
    while True:
        num=input(f'Введите число от {a} до {b}: ')
        print()
        if is_valid(num):
            num=int(num)
            if num<number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter+=1
            elif num>number:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter+=1
            else:
                counter+=1
                print('Вы угадали, поздравляем!',f'\nВаше число попыток: {counter}')
                break             
        else:
            print(f'А может быть все-таки введем целое число от {a} до {b}?')
            counter+=1
is_valid_num()
while True:
    n = input('Хотите еще раз сыграть? (дa/нет):' )
    if n=='да':
        print('Введите числа с какого по какое вы хотите угадывать:')
        is_valid_num()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break