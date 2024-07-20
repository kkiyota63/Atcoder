N, T, P = map(int, input().split())
L = list(map(int, input().split()))

# 初期リストで条件を満たしているか確認
cnt = sum(1 for x in L if x >= T)
if cnt >= P:
    print(0)
else:
    iteration = 0
    while True:
        L = [x + 1 for x in L]  # リストのすべての要素に1を足す
        cnt = sum(1 for x in L if x >= T)  # 条件を満たす要素の数を数える
        iteration += 1
        if cnt >= P:
            break

    print(iteration)
