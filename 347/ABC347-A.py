N, K = map(int, input().split())
A = [N]
A = list(map(int, input().split()))

for i in range(N):
    if A[i] % K == 0:
        print(int(A[i]/K), end=" ")
print()