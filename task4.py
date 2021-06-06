from math import sqrt, log10
import matplotlib.pyplot as plt
from solutiion import *
from scipy import stats

# n = int(input())
n = 20
res = get_n_numbers(n)
# data = []
# for j in range(100):
#     data.append(24.15)
def get_imeric_func(res,n):
    data = {}
    for index in range(len(res)):
        el = res[index]
        if el in data:
            data[el]+=1
        else:
            data[el] = index
    xx = []
    kk = []
    print(data)
    for k,v in data.items():
        xx.append(k)
        kk.append(v)
    return xx,kk

# def dot_eval (xx,kk,n):
#     x_ = 0
#     for i in range(len(xx)):
#         x_ += xx[i]*kk[i]
#     x_*=1/n


def get_dispers(res,n):
    x_ = 0
    s = 0
    for el in res:
        x_+=el
    x_/=n
    for el in res:
        s+= (el-x_)**2
    s/=n
    return s,(s*n)/(n-1),x_
print(res)
r = get_dispers(res,n)
# дисперсия
print("дисперсия",r[1])
# мо
print("mo".format(r[2]))
# xx, kk = get_imeric_func(res, n)
significance = [99,97.5,95,92.5,90,87.5,85,82.5,80]
t_Y = [ 2.58,2.24,1.96,1.78,1.65,1.535,1.44,1.355,1.29]

# significance = [99,97.5,95,90,85,80]
# t_Y = [ 2.58,2.24,1.96,1.65,1.44,1.29]
def get_intervals_mo(mo,s,t_Y,significance,n):
    # среднеквадратичное отклонение
    s = sqrt(s)
    # s = 5
    print(mo,s)
    xx,yy = [],[]
    for i in range(len(t_Y)):
        # коэффициент доверия
        k_y = (t_Y[i]*s)/sqrt(n)
        # print(t_Y[i])
        # print(k_y,mo)
        a,b = mo-k_y,mo+k_y
        print("При уровне значимости {}% доверительный интервал : [{}, {}]".format(significance[i],a,b))
        xx.append(b-a)
        yy.append(significance[i])
    # plt.step(xx,yy)
    plt.plot(xx,yy)
    plt.show()

l = get_dispers(res,n)
print("+",sum(res)/n)
get_intervals_mo(l[2],l[1],t_Y,significance,n)
