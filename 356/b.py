N, M = map(int, input().split())
A = list(map(int, input().split()))

total_X = 0
cnt = 0
X = [list(map(int,input().split())) for _ in range(N)]

for i in range(M):
    for j in range(N):
        total_X += X[j][i]
    if total_X >= A[i]:
        cnt += 1
    total_X = 0 #reset total_X

if(cnt==M):
    print("Yes")
elif(cnt<M):
    print("No")

# for j in range(M):
#   s = 0
#   for i in range(N):
#     s += X[i][j]
#   if s < A[j]:
#     print("No")
#     exit()
# print("Yes")


