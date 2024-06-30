N, Q = map(int, input().split())
T = list(map(int, input().split()))

cnt = []

#N -= 1
for i in range(0, Q):
    if T[i] in cnt:
        N += 1
        cnt.remove(T[i])
    else:
        N -= 1
        #T[i]をcntに追加
        cnt.append(T[i])
    #print(N)
    
print(N)
