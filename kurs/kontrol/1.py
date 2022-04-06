from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random as rd
import numpy as np

def symmetric_difference(n):
    list_=[rd.randint(1, n+1) for i in range(20)]
    list_result=list()
    if len(list_)!=0:
        for i in range(len(list_)):
                if list_.count(list_[i])==1:
                    list_result.append(list_[i])
        list_result.sort()
    else:
        print('0')
list_time=list()
list_n=list()        
for n in range(1, 20001):
    start=timer()
    symmetric_difference(n)
    end=timer()
    time_ = (end-start)
    list_time.append(time_)
    list_n.append(n)
t = np.polyfit(list_n, list_time, 4)
f = np.poly1d(t)
plt.ylabel('Время(секунды)')
plt.xlabel('Максимум случайного числа')
plt.plot(list_n , list_time, color='Blue' , label='Эксперементальные результаты')
plt.plot(list_n, f(list_n),color='Orange', label='Апроксимация на основе теоретических оценок' )
plt.legend(loc = 'best', fancybox = True, shadow = True)
plt.grid(True)
plt.show()


