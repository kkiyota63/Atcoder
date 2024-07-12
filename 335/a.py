S = input()

S_list = list(S)

S_list[-1]='4'

for i in range(len(S_list)):
    print(S_list[i], end='')
print()