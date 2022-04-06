#фильтр запросов
google_str=[input('Введите пунк списка: ') for i in range(int(input('Введите кол-во пунктов: ')))]
get=[input('Введите запрос: ').lower() for i in range(int(input('Введите кол-во запросов: ')))]
for i in google_str:
    for j in get:
        if j==i.lower():
            print('Верный запрос:', i)