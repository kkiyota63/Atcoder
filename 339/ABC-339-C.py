N = int(input())
num = 0

A = list(map(int, input().split()))  

for j in range(N):
    if num + A[j] < 0:
        num = -A[j]
    num += A[j]

print(num)

