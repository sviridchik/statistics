import random
import numpy as np
import matplotlib.pyplot as plt
n = int(input())
a = -6
b = -2
a_y = -1
b_y = -0.2
# e = random.random()
def f_y(x):
    return 1/(1+x)

# res = [-6.237 ,-6.229 ,-5.779, -5.139, -4.950 ,-4.919 ,-4.636, -4.560, -4.530, -4.526 ,-4.523 ,-4.511,
# -4.409 ,-4.336, -4.259, -4.055, -4.044, -4.006, -3.972, -3.944 ,-3.829 ,-3.794, -3.716, -3.542,
# -3.541 ,-3.431, -3.406, -3.384, -3.307, -3.181, -3.148, -3.124, -3.116, -2.892, -2.785, -2.734,
# -2.711 ,-2.637, -2.633, -2.428, -2.381 ,-2.339, -2.276, -2.222 ,-2.167 ,-2.111 ,-2.034, -1.958,
# -1.854 ,-1.803, -1.774, -1.755 ,-1.745 ,-1.713 ,-1.709, -1.566, -1.548 ,-1.480 ,-1.448 ,-1.353,
# -1.266, -1.229, -1.179, -1.130, -1.102 ,-1.060, -1.046, -1.035, -0.969, -0.960, -0.903, -0,885,
# -0.866, -0.865, -0.774, -0.721 ,-0.688 ,-0.673 ,-0.662 ,-0.626, -0.543 ,-0.445 ,-0.241 ,-0.174,
# -0.131, 0.115, 0.205, 0.355, 0.577 ,0.591 ,0.795 ,0.986 ,1.068, 1.099, 1.195 ,1.540,
# 2.008, 2.160, 2.534, 2.848 ]
# n = 100
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



res = get_n_numbers(n)
get_imeric_func(res,n)

