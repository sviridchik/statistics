import random
import numpy as np
from math import sqrt, log10
import matplotlib.pyplot as plt
# n = int(input())
n = 30
a = -6
b = -2
a_y = -1
b_y = -0.2
# e = random.random()
def f_y(x):
    return 1/(1+x)


def get_n_numbers(n):
    res_y = []
    res_x = []
    for i in range(n):
        e = random.uniform(0, 1)
        x_i = e*(b-a)+a
        res_x.append(x_i)
        res_y.append(f_y(x_i))
    #     вариационный ряд
    res_y.sort()
    res_x.sort()

    return res_y

def F(y):
    if y < a_y:
        return 0
    elif y > b_y:
        return 1
    else:
        return -(1/(4*y))-1/4
# res_h_y = []
def get_imeric_func(res,n):
    data = {}
    for index in range(len(res)):
        el = res[index]
        if el in data:
            data[el]+=1
        else:
            data[el] = index
    xx = []
    yy = []
    for k,v in data.items():
        xx.append(k)
        yy.append(v/n)
    plt.step(xx,yy,'y',label = "imperical function")
    xxx = np.linspace(xx[0],xx[-1] , n)
    yyy = [F(ell) for ell in xxx]
    plt.plot(xxx, yyy, 'm',label = "analytic function")

    # plt.show()
    max_diff = -1
    yyy.sort()
    # print(yy)
    # print(xx)
    # print(yyy)
    for index in range(len(yy)):
        max_tmp = abs(yy[index] - F(xx[index]))
        print(max_tmp)
        if max_tmp>max_diff:
            max_diff = max_tmp
    print(max_diff,sqrt(n))
    const = 1.36
    out = sqrt(n)*max_diff
    print("Kolmogorov :{}".format(sqrt(n)*max_diff))
    # поправка большева
    if n < 25:
        out+=1/(sqrt(n)*6)
        print("Применена поправка Большева")

    if out < const:
        print("{} < {} Следрвательно нет оснований отвергать нулевую гипотезу".format(out,const))



#
res = get_n_numbers(n)
get_imeric_func(res,n)


