import itertools

N = int(input())
#Nの長さの文字列をinput
A = list(map(int, input().split()))


comb = list(itertools.combinations(A, 2))

cnt = 0

for c in comb:
    C = c[0]*c[1]
    #Cが平方数か判定
    if C**0.5 % 1 == 0:
        cnt +=1

print(cnt)