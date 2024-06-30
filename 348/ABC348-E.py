import numpy as np

def solve_problem(N, A, B, C):
    # 1以上N以下の相異なる整数kの集合Sを作る
    S = set(range(1, N+1))

    # 整数の集合のmax-minを求める
    max_min_diff = 0
    for k in S:
        Ak = A[k-1]
        Bk = B[k-1]
        max_min_diff = max(max_min_diff, abs(Bk - Ak))
    
    return max_min_diff*C

# 入力の受け取り
N = int(input())
A = []
B = []
for i in range(1,N-1):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

C = [N]
C = list(map(int, input().split()))

# 問題を解く
result = solve_problem(N, A, B, C)
print(result)