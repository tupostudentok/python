from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random as rd
import numpy as np


def heap_difference(n):
    #_________________СОЗДАНИЕ СПИСКА КАМНЕЙ_________
    N_stones = rd.randint(1, 24)
    list_ = [rd.randint(1, n+1) for i in range(N_stones)]
    list_stones = list()
    for i in range(N_stones):
        list_stones.append(list_[i])
    list_stones.sort()

    #___________ВЫЧИСЛЕНИЕ ОПТИМАЛЬНЫХ КУЧ__________
    heap_1 = list()
    heap_2 = list()
    first_point, last_point = 0, len(list_stones) - 1
    while first_point <= last_point:
        small_pile, big_pile = list_stones[first_point], list_stones[last_point]
        if sum(heap_1) <= sum(heap_2):
            heap_1.append(small_pile)
            first_point += 1
        else:
            heap_2.append(big_pile)
            last_point -= 1

    #______________ВЫВОД МИНИМАЛЬНОЙ РАЗНИЦЫ КУЧ________
    if sum(heap_1) >= sum(heap_2):
        print(sum(heap_1)-sum(heap_2))
    else:
        print(sum(heap_2)-sum(heap_1))

list_time=list()
list_n=list()        
for n in range(1, 2001):
    start=timer()
    heap_difference(n)
    end=timer()
    time_ = (end-start)
    list_time.append(time_)
    list_n.append(n)
t = np.polyfit(list_n, list_time, 4)
f = np.poly1d(t)
plt.ylabel('Время(секунды)')
plt.xlabel('Максимальный размер случайного камня')
plt.plot(list_n , list_time, color='Blue' , label='Эксперементальные результаты')
plt.plot(list_n, f(list_n),color='Orange', label='Апроксимация на основе теоретических оценок' )
plt.legend(loc = 'best', fancybox = True, shadow = True)
plt.grid(True)
plt.show()