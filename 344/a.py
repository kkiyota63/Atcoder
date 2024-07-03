S = input()
flg = 0

for i in range(len(S)):
    if flg == 2:
        print(S[i], end='')
    if S[i] == '|':
        flg += 1
    if flg == 0:
        print(S[i], end='')
print()