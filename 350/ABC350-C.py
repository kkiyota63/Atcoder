N = int(input())
A = list(map(int, input().split()))
cnt = 0
sorted_list = []

# バブルソート
for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            # ソートした組を格納
            sorted_list.append([A[j], A[j+1]])
            cnt += 1

# 出力
print(cnt)
#print(sorted_list)
#print(A)
for pair in sorted_list:
    print(*pair)