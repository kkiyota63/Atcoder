N = int(input())
A = list(map(int, input().split()))
B = []

for i in range(N-1):
    B = A[i]*A[i+1]
    print(B, end=" ")
print()