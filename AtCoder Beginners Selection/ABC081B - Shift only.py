N = int(input())
A = list(map(int, input().split()))

cnt = 0

def calc(A):
    global cnt
    divisible = True
    while divisible:
        for i in range(N):
            if A[i] % 2 != 0:  # 奇数が見つかった場合
                divisible = False
                break
        if divisible:  # 全ての要素が偶数だった場合
            A = [a // 2 for a in A]  # 各要素を2で割る
            cnt += 1

calc(A)
print(cnt)
    