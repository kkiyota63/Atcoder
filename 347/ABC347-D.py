a,b,C = map(int, input().split())

#次の5つの条件に全て満たすX,Yの組が存在するか判定
#0<=x<20^60
#0<=y<20^60
#popcount(x)=a
#popcount(y)=b
#XとYの排他的論理和がC

#popcount関数を定義
def popcount(n):
    return bin(n).count("1")

for i in range(1<<20):
    X = i
    Y = X^C
    if popcount(X) == a and popcount(Y) == b:
        print(X, Y)
        exit()
print(-1)


