N = int(input())
list = []
sum = 0

for i in range(N):
    S,C = input().split()
    list.append([S,int(C)])

#Sの辞書順にソート
list.sort()

for j in range(N):
    #listのCの総和をとる
    sum += list[j][1]

ans = sum % N 
print(list[ans][0])


