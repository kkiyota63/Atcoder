N = int(input())
#Nの長さの文字列をinput
S = input()
Q = int(input())

#Q個のc,dをinput
for i in range(Q):
    c, d = map(str, input().split())
    S = S.replace(c, d)

print(S)