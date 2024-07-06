def min_difference(N, K, A):
    # ソートされたリストを用意
    A.sort()
    
    # 最小の差を初期化
    min_diff = float('inf')
    
    # スライディングウィンドウで差を計算
    for i in range(N - (N - K) + 1):
        current_diff = A[i + (N - K - 1)] - A[i]
        min_diff = min(min_diff, current_diff)
    
    return min_diff

# 入力例
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 結果を出力
result = min_difference(N, K, A)
print(result)
