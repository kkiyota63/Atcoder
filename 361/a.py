N, K, X = map(int, input().split())
A = list(map(int, input().split()))

# K がリストの長さより大きい場合、リストの最後に追加
if K == len(A):
    A.append(X)
else:
    A.insert(K, X)

for i in range(N+1):
    print(A[i], end=' ')
print()
