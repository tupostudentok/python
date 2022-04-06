#вывод буквы с заданным номером
set_line=[input('Введите строку: ') for i in range(int(input('Введите количество строк: ')))]

number_letter=int(input('Введите номер буквы: '))-1
for i in set_line:
    print(i[number_letter])