from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random as rd
import numpy as np

def identical_elements(n):
    range_n1=rd.randint(1, n+1)
    range_n2=rd.randint(1, n+1)
    n1=[rd.randint(1, n+1) for _ in range(range_n1)]
    n2=[rd.randint(1, n+1) for _ in range(range_n2)]
    count=0
    for i in range(len(set(n1))):
        for j in range(len(set(n2))):
            if n1[i]==n2[j]:
                count+=1


list_time=list()
list_n=list()        
for n in range(1, 2001):
    start=timer()
    identical_elements(n)
    end=timer()
    time_ = (end-start)
    list_time.append(time_)
    list_n.append(n)
t = np.polyfit(list_n, list_time, 4)
f = np.poly1d(t)
plt.ylabel('Время(секунды)')
plt.xlabel('Размер множества случайных чисел')
plt.plot(list_n , list_time, color='Blue' , label='Эксперементальные результаты')
plt.plot(list_n, f(list_n),color='Orange', label='Апроксимация на основе теоретических оценок' )
plt.legend(loc = 'best', fancybox = True, shadow = True)
plt.grid(True)
plt.show()