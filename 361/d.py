N = int(input())
S = input()
T = input()

# 最小操作回数を保存する変数
min_operations = float('inf')

# 文字列 S の各位置で分割し、それぞれの分割に対して操作回数を計算
for i in range(len(S)):
    rotated_S = S[i:] + S[:i]  # 文字列 S を分割して結合し、新しい文字列を生成
    operations = 0

    # 生成した新しい文字列が T と一致するか確認
    if rotated_S == T:
        min_operations = min(min_operations, operations)
    else:
        # 生成した新しい文字列に対してペア操作を実行
        while rotated_S != T and operations < len(S):
            operations += 1
            rotated_S = rotated_S[1:] + rotated_S[0]  # 文字列の最初の文字を最後に移動

            if rotated_S == T:
                min_operations = min(min_operations, operations)
                break

# 結果を表示
if min_operations == float('inf'):
    print(-1)  # 一致する場合がない場合
else:
    print(min_operations)
