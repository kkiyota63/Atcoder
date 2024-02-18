# import math

# N = int(input())
# TK = []
# total = 0

# def calc(N):
#     if N >=2:
#         x = N
#         N1 = math.ceil(x/2) #切り上げ
#         N2 = math.floor(x/2) #切り捨て
#         TK.append(x)
#         calc(N1)
#         calc(N2)
#     else:
#         return 

# calc(N)

# for i in range(len(TK)):
#     total += TK[i]


# print(total)


# import math
# from functools import cache

# N = int(input())

# @cache
# def calc(N):
#     if N < 2:
#         return 0
#     else:
#         N1 = math.ceil(N / 2)  # 切り上げ
#         N2 = math.floor(N / 2)  # 切り捨て
#         return N + calc(N1) + calc(N2)  # 再帰的に呼び出し、その都度Nを加算

# total = calc(N)
# print(total)


# def f(N):
#     return 0 if N == 1 else f(N // 2) + f((N + 1) // 2) + N
# print(f(int(input())))

#################################

import math
from functools import cache

@cache
def f(N):
    if N<2:
        return 0
    else:
        return f(N//2) + f((N+1)//2) + N
    
print(f(int(input())))

#################################

# import math
# from functools import cache

# N = int(input())

# @cache
# def calc(N):
#     if N < 2:
#         return 0
#     else:
#         N1 = math.ceil(N / 2)  # 切り上げ
#         N2 = math.floor(N / 2)  # 切り捨て
#         return N + calc(N1) + calc(N2)  # 再帰的に呼び出し、その都度Nを加算

# total = calc(N)
# print(total)
