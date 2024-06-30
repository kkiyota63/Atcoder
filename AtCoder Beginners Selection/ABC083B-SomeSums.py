N,A,B = map(int,input().split())
cnt = 0

for i in range(1,N+1):
    sumi = sum(map(int,str(i)))
    if A <= sumi <= B:
        cnt += i

print(cnt)
