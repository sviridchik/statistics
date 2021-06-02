import random
import numpy as np
import matplotlib.pyplot as plt
# n = int(input())
n = 50
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
    # print(res_x)
    # print(res_y)

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
    # print(data)
    xx = []
    yy = []
    print(data)
    for k,v in data.items():
        xx.append(k)
        yy.append(v/n)
    plt.step(xx,yy,'y',label = "imperical function")
    # plt.show()
    xxx = np.linspace(xx[0],xx[-1] , 10000)
    print(xx)
    yyy = [F(ell) for ell in xxx]
    print(yy)
    print(xxx)
    print(yyy)
    plt.plot(xxx, yyy, 'm',label = "analytic function")
    plt.show()


#
# get_imeric_func(res,n)
def mizes(n):
    const = 0.347
    out = 0
    res = get_n_numbers(n)
    for i in range(len(res)):
        out+=(F(res[i])-(i-0.5)/n)**2
    out += 1/(12*n)
    print("при n = {}".format(n))
    print("Мизеса : {}".format(out))
    if out<const:
        print("{} < {} Следрвательно нет оснований отвергать нулевую гипотезу".format(out,const))
mizes(n)


