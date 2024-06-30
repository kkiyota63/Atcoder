N = int(input())

# NxNの行列Aを作成
A = []
for i in range(N):
    row = list(input())
    A.append(row)

# NxNの行列Bを作成
B = []
for i in range(N):
    row = list(input())
    B.append(row)
    
# AとBの行列の差の行と列を表示
for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i+1, j+1)

