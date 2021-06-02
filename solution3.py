from math import sqrt, log10
import matplotlib.pyplot as plt
import numpy as np

from solutiion import *

# n = int(input())
# # n = 1000000
# res = get_n_numbers(n)
# print(res)
#
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
def get_m(n):
    if n <= 100:
        M = int(sqrt(n))
        return M
    else:
        M1 = int(3 * log10(n))
        M2 = int(3 * log10(n))
        M3 = int(3 * log10(n))
        if M1 % n == 0:
            return M1
        elif M2 % n == 0:
            return M2
        else:
            return M3
def f(y):
    if y<a_y or y>b_y:
        return 0
    else:
        return 1/(4*y**2)

def draw_a_table(n):
    M = get_m(n)
    h = abs(res[0] - res[-1]) / M
    h = round(h,4)
    result = []
    j = 0
    a_i = res[0]
    b_i = (res[n//(M-1)]+res[n//M])/2
    bins = []
    ff = []
    v_i = n / M
    bins.append(a_i)
    bb = None
    for i in range(1,M):
        h = abs(a_i-b_i)
        f_i = v_i / (h * n)
        ff.append(f_i)
        ss = "i = {:.1f}\tAi = {:.4f}\t Bi = {:.4f}\tvi = {}\th = {:.4f}\tfi = {:.4f}\t".format(round(i,4),a_i,round(b_i,4),round(v_i,4),round(h,4),round(f_i,4))
        # print(ss)
        bins.append(b_i)
        a_i = b_i
        if (i+1)*M+1 > len(res)-1:
            b_i = res[-1]
        else:
            b_i = (res[(i+1)*(n//M)-1]+res[(i+1)*(n//M)])/2

            # b_i = (res[(i+1)*M-1]+res[(i+1)*M])/2
        bb = b_i
    if res[-1] != bins[-1]:
        i = len(bins)
        b_i = res[-1]
        h = abs(a_i - b_i)
        f_i = v_i / (h * n)
        ff.append(f_i)
        # print("aaaaa")
        ss = "i = {:.1f}\tAi = {:.4f}\t Bi = {:.4f}\tvi = {}\th = {:.4f}\tfi = {:.4f}\t".format(round(i, 4), a_i, round(b_i, 4),
                                                                                            round(v_i, 4), round(h, 4),                                                          round(f_i, 4))
        # print(ss)
        bins.append(b_i)
    return ff, bins, v_i, M


# ff,bins = l[0],l[1],l[2],l[3]

# def calc_kolmogorov(l):
#     ff, bins, n_i, m = l[0], l[1], l[2], l[3]
#     max_global = []
#     h = 0.01
#     for i in range(len(ff)):
#         max_local = -1
#         j = bins[i]
#         while j <bins[i+1]:
#             max_tmp = abs(F(bins[i] + j * h) - F(max_local))
#             if max_tmp > max_local:
#                 max_local = max_tmp
#             j+=1
#         max_global.append(max_local)
#     print("Колмогоров :{}".format(sqrt(n)*max(max_global))  )


def calc_hi_2(l):
    ff, bins, n_i, m = l[0], l[1], l[2], l[3]
    pi_star = n_i / n
    k = m - 1
    hi_2 = 0
    for i in range(1, len(bins)):
        pi = F(bins[i]) - F(bins[i-1])
        hi_2 += ((pi-pi_star)**2)/(pi)
    hi_2 = n*hi_2
    result ={5:[15.1,12.8,11.1],4:[13.3,11.1,9.5],6:[16.8,14.4,12.6]}
    probability = [99,97.5,95]
    print(hi_2,k)
    for i in range(3):
        if hi_2<result[k][i]:
            print("{} < {} Следрвательно нет оснований отвергать нулевую гипотезу c вероятностью {}%".format(hi_2,result[k][i],probability[i]))
            break


for o in range(1):
    # n = int(input())
    n = 200
    res = get_n_numbers(n)
    l = draw_a_table(n)
    calc_hi_2(l)
    # calc_kolmogorov(l)

    # 1000 hi2 і графік

