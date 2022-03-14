import math
import random


# 得到各自的计算数
def get_calculation(p, a, X):
    Y = (a ** X) % p
    return Y


# 得到交换计算数后的密钥
def get_key(X, Y, p):
    key = (Y ** X) % p
    return key