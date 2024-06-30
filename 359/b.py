N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(2*N-2):
    if (A[2+i]-A[i]==0):
        ans += 1

print(ans)
