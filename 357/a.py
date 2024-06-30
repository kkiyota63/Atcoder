N, M = map(int, input().split())
ans = 0
H = list(map(int, input().split()))
for i in range (N):
    M -= H[i]
    if (M >= 0):
        ans += 1
    else:
        break
print(ans)