import random
import numpy as np
import matplotlib.pyplot as plt
n = int(input())
a = -1
b = 5

# e = random.random()
def f_y(x):
    return x**3

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
    # print(res_x)
    # print(res_y)

    return res_y


def F(y):
    if y < -1:
        return 0
    elif y > 125:
        return 1
    else:
        return (1/6)*(np.cbrt(y)+1)
# res_h_y = []
def get_imeric_func(res):
    data = {}
    for index in range(len(res)):
        el = res[index]
        if el in data:
            data[el]+=1
        else:
            data[el] = index
    # print(data)
    xx = []
    yy = []
    for k,v in data.items():
        xx.append(k)
        yy.append(v/n)
    plt.step(xx,yy,'y',label = "imperical function")
    # plt.show()
    xxx = np.linspace(-1, 125, 100)
    print(xxx)
    yyy = [F(ell) for ell in xxx]
    plt.plot(xxx, yyy, 'm',label = "analytic function")
    plt.show()



res = get_n_numbers(n)
get_imeric_func(res)

