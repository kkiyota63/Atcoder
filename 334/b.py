A, M, L, R = map(int, input().split())
dist = R - L + 1

if dist == 1:
    print(0)
    exit()

for i in range(10000):
    if (R - A) * M * i < (M - 1): 
        ans = dist/M
        ans +=1
        break
    else:
        ans = dist/M

# print(dist)
# print(M)
print(int(ans))