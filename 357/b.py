S = input()

low_cnt = 0
up_cnt = 0

for i in range(len(S)):
    if(S[i].islower()):
        low_cnt += 1
    elif(S[i].isupper()):
        up_cnt += 1
    
if(low_cnt > up_cnt):
    print(S.lower())
elif(up_cnt >= low_cnt):
    print(S.upper())
