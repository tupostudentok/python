from cProfile import label
import random as rd
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
list_vrem=list()
list_n=list()

def bubble_vector(n):

    list_= list(np.random.randint(1, n+1,n))
    l = len(list_)
    for i in range(l-1):
        flag = True
        for j in range(l-i-1):
            if list_[j]>list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
                flag = False
        if flag:
            break
def Quick_sort_v(n):
    list_=[ rd.randint(1, n+1) for _ in range(n)]
    q = rd.choice(list_)
    s_nums = []
    m_nums = []
    e_nums = []
    for i in list_:
           if n < q:
               s_nums.append(i)
           elif n > q:
               m_nums.append(i)
           else:
               e_nums.append(i)
    return s_nums + e_nums + m_nums
def timesort_v(n):
    list_= list(np.random.randint(1, n+1,n))
    left=int(list_[0])
    right=None
    if right is None:
        right = len(list_) - 1
    for i in range(left + 1, right + 1):
        key_item = list_[i]
        j = i - 1
        while j >= left and list_[j] > key_item:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key_item
    return list_
def f_v1(n):
    list_= list(np.random.randint(1, n+1,n))
    return 1
def sum_f(n):
    return sum(list(np.random.randint(1, n+1,n)))
def sum_f2(n):
    list_= list(np.random.randint(1, n+1,n))
    s = (sum(list_) * Decimal(1.5)**n)
    return s
for n in range(1, 2001):
    start=timer()
    sum_f2(n)
    end=timer()
    vrem_y = (end-start)
    list_vrem.append(vrem_y)
    list_n.append(n)
t = np.polyfit(list_n, list_vrem, 4)
f = np.poly1d(t)
plt.ylabel('Время(секунды)')
plt.xlabel('Размерность вектора v')
plt.plot(list_n , list_vrem, color='Blue' , label='Эксперементальные результаты')
plt.plot(list_n, f(list_n),color='Orange', label='Апроксимация на основе теоретических оценок' )
plt.legend(loc = 'best', fancybox = True, shadow = True)
plt.grid(True)
plt.show()


