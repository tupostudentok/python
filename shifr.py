print('Добро пожаловать в программу шифровки/дешифровки Цезаря.')
while True:
    shifr=input('Хотите зашифровать или дешифровать?(з/д) ')
    if shifr=='з' or shifr=='д':
        break
    else:
        print('Не понял, что вы хотите сделать...')
lang=input('Какой вы хотите использовать язык алфавита?(en/ru) ')
#zdv=int(input('Введите шаг сдвига(число): '))

def shifr_cez(txt:str):
    zdv=len(txt)
    if lang=='en':
        lang_=[chr(i) for i in range(65,91)]+[chr(j) for j in range(97,123)]
        moch=26
    elif lang=='ru':
        lang_=[chr(i) for i in range(1040, 1104)]
        moch=32
    for i in range(len(txt)):
        if txt[i].isalpha():
            if shifr=='з':
                if txt[i].isupper():
                    print(lang_[(lang_.index(txt[i]) + zdv) % moch], end = '')
                else:
                    print(lang_[(lang_.index(txt[i]) + zdv) % moch + moch], end='')

            elif shifr=='д':
                if txt[i].isupper():
                    print(lang_[(lang_.index(txt[i]) - zdv) % moch], end = '')
                else:
                    print(lang_[(lang_.index(txt[i]) - zdv) % moch + moch], end='')
        else:
            print(txt[i], end='')

shifr_cez(input('Введите свой текст: '))
