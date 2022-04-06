import random as rd
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


list_time=list()
list_n=list()

for n in range(1,201):
    start=timer()
    matrix1= [ [ rd.randint(1, n+1) for _ in range(1, n+1)] for i in range(1, n+1) ]
    matrix2=[ [ rd.randint(1, n+1) for _ in range(1,n+1)] for i in range(1, n+1) ]
    matrix3=np.matmul(matrix2, matrix1)
    end=timer()
    vrem_y = (end-start)
    list_time.append(vrem_y)
    list_n.append(n)

t = np.polyfit(list_n, list_time, 3)
f = np.poly1d(t)
plt.ylabel('Время(секунды)')
plt.xlabel('Размер матрицы')
plt.plot(list_n , list_time, color='Blue' , label='Эксперементальные результаты')
plt.plot(list_n, f(list_n),color='Orange', label='Апроксимация на основе теоретических оценок' )
plt.legend(loc = 'best', fancybox = True, shadow = True)
plt.grid(True)
plt.show()
