N,L,R = map(int, input().split())
ans = []

for i in range(1,N+1):
    if L<=i and i <= R:
        ans.append(L+R-i)
    else:
        ans.append(i)

for i in range(N):
    print(ans[i], end=" ")
print()
 
