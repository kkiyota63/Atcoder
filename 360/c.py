from collections import Counter

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# 答えを保持する変数を初期化
ans = 0

# 各要素のインデックスを保持する辞書を初期化
index_map = {}

# 各要素を調べてインデックスを記録する
for index, item in enumerate(A):
    if item in index_map:
        index_map[item].append(index)
    else:
        index_map[item] = [index]

# 重複している要素とそのインデックスを見つける辞書を初期化
duplicates = {}

# 重複している要素を探してduplicatesに格納する
for item, indices in index_map.items():
    if len(indices) > 1:
        duplicates[item] = indices

# 重複要素の処理を行う
for item, indices in duplicates.items():
    # 最大のインデックスを持つものを見つける
    max_index = max(indices, key=lambda i: W[i])
    # 残りのインデックスのW値を合計に加える
    indices.remove(max_index)  # 最大のものを除外する
    for index in indices:
        ans += W[index]

print(ans)
