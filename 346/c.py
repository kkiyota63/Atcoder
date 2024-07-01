N, K = map(int, input().split())
A = list(map(int, input().split()))

# 1からKまでの和を計算する
total_sum_k = (K * (K + 1)) // 2

# リストAの要素の和を計算する
sum_in_A = sum(x for x in A if 1 <= x <= K)

# 1からKまでの和からリストAの要素の和を引く
result = total_sum_k - sum_in_A

print(result)
