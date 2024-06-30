N = int(input())
A = list(map(int, input().split()))
cnt = 0
sorted_list = []

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if A[j] < A[min_idx]:
            min_idx = j
    if min_idx != i:
        A[i], A[min_idx] = A[min_idx], A[i]
        sorted_list.append([A[i], A[min_idx]])
        cnt += 1

print(cnt)
for pair in sorted_list:
    print(*pair)
#print(*A)