N = int(input())
A = list(map(int, input().split()))  # 通貨の初期値を一度に入力

for j in range(N-1):
    s, t = map(int, input().split())
    A[j]-= s
    A[j+1]+=t

print(max(A))
