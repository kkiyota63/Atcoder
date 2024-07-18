N = int(input())
x = []
cnt = 0 

for i in range(N):  
    row = list(map(int, input().split()))
    x.append(row)

for j in range(N):
    cnt = 0
    for k in range(N):
        cnt += 1
        if x[j][k]==1:
            print(cnt, end=' ')
    print( )