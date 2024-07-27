# 入力を受け取る
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def find_min_exceed_count(arr, threshold):
    arr.sort(reverse=True)  # 降順にソート
    total = 0
    count = 0
    for value in arr:
        total += value
        count += 1
        if total > threshold:
            return count
    return N # thresholdを超えることがなければ無限大を返す

# AとBのそれぞれで合計が閾値を超える最小の個数を求める
count_A = find_min_exceed_count(A, X)
count_B = find_min_exceed_count(B, Y)

# 結果の中で最小の個数を出力する
result = min(count_A, count_B)
print(result)
