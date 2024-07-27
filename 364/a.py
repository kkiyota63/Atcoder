N = int(input())
cnt = 0
result = "Yes"

for i in range(N):
    if i == N-1:
        S = input()
        break  # iがN-1になった時点でループを終了する
    S = input()
    if S == "sweet":
        cnt += 1
        if cnt == 2:
            result = "No"
    else:
        cnt = 0  # 塩辛い料理が出たらカウンタをリセット

print(result)
