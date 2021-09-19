import timeit

import numpy as np
from decimal import Decimal
import itertools
from itertools import starmap, product


def v(k, n):
    row = [1 / (k * ((n + 1) ** (2 * k)))]
    return row

# def v(k, row):
#     row = [(1 / (k * ((n + 1) ** (2 * k)))) for n in row]
#     return row


# def doubles(maxk, maxn):
    
#     # row = np.arange(1, maxn + 1)
#     row = [x for x in range(1, maxn + 1)]
#     # S_arr = f(1, row)
#     S_arr = []
    

#     for k in range(1, maxk + 1):
#         # S_arr = np.append(S_arr, f(k, row))
#         S_arr.append(v(k, row))
    
#     S_arr = np.asarray(S_arr)
#     # print(S_arr)
#     return np.sum(S_arr)


def doubles(maxk, maxn):
    lst1 = [k for k in range(1, maxk + 1)]
    lst2 = [n for n in range(1, maxn + 1)]
    lst_tuple = list(itertools.product(lst1, lst2))

    lst = list(starmap(v, lst_tuple))
    arr = np.asarray(lst)
    return np.sum(arr)


print(doubles(20,10000))


# print(timeit.timeit(stmt=test, number=40))
    