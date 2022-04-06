from random import*

from numpy import char
digits='0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation='!#$%&*+-=?@^_'
chars=''
colvo=int(input('Сколько вы хотите паролей? '))
len_pass=int(input('Сколько должно быть символов в пароле? '))
propis=input(f'Включать ли прописные буквы {lowercase_letters}?(да/нет) ')
stroch=input(f'Включать ли строчные буквы {uppercase_letters}?(да/нет) ')
num=input(f'Включать ли цифры {digits}?(да/нет) ')
simbols=input(f'Включать ли символы {punctuation}?(да/нет) ')
if propis=='да':
    chars+=lowercase_letters
if stroch=='да':
    chars+=uppercase_letters
if num=='да':
    chars+=digits
if simbols=='да':
    chars+=punctuation
def generate_password(len, chars):
    passw=''
    for i in range(len):
        passw+=choice(chars)
    print(passw)
for i in range(colvo):
    generate_password(len_pass, chars)